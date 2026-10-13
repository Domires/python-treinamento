"""
Site de Treinamento - Cadastro de Produtos
==========================================

Backend FastAPI com:
- Autenticação JWT Bearer (usuário "treinamento" / senha "12345678")
- CRUD de produtos persistido em SQLite (arquivo produtos.db)
- Documentação Swagger em /docs (e ReDoc em /redoc)
- Páginas HTML estáticas: /login, /cadastro e /produtos

Executar:
    python main.py
ou
    uvicorn main:app --reload
"""

import os
import sqlite3
from contextlib import asynccontextmanager
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Literal

import jwt
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, model_validator

# ---------------------------------------------------------------------------
# Configurações
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DB_PATH = BASE_DIR / "produtos.db"

USUARIO = "treinamento"
SENHA = "12345678"

SECRET_KEY = os.getenv("JWT_SECRET", "chave-secreta-do-treinamento-troque-em-producao")
ALGORITHM = "HS256"
TOKEN_EXPIRA_MINUTOS = int(os.getenv("JWT_EXPIRA_MINUTOS", "480"))  # 8 horas

# ---------------------------------------------------------------------------
# Banco de dados (SQLite)
# ---------------------------------------------------------------------------


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS produtos (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                fabrica         TEXT    NOT NULL,
                codigo_material TEXT    NOT NULL,
                nome_material   TEXT    NOT NULL,
                lote            TEXT    NOT NULL,
                data_producao   TEXT    NOT NULL,
                data_validade   TEXT    NOT NULL,
                quantidade      INTEGER NOT NULL,
                unidade_medida  TEXT    NOT NULL,
                observacao      TEXT    NOT NULL DEFAULT '',
                criado_em       TEXT    NOT NULL,
                atualizado_em   TEXT    NOT NULL
            )
            """
        )
        # Migração: bancos criados antes dos novos campos
        colunas = {r["name"] for r in conn.execute("PRAGMA table_info(produtos)")}
        if "unidade_medida" not in colunas:
            conn.execute("ALTER TABLE produtos ADD COLUMN unidade_medida TEXT NOT NULL DEFAULT 'KG'")
        if "observacao" not in colunas:
            conn.execute("ALTER TABLE produtos ADD COLUMN observacao TEXT NOT NULL DEFAULT ''")


# ---------------------------------------------------------------------------
# Schemas (Pydantic)
# ---------------------------------------------------------------------------


class LoginRequest(BaseModel):
    usuario: str = Field(..., examples=["treinamento"])
    senha: str = Field(..., examples=["12345678"])


class TokenResponse(BaseModel):
    access_token: str = Field(..., description="Token JWT a ser enviado no header Authorization")
    token_type: str = Field("bearer", examples=["bearer"])
    expira_em: datetime = Field(..., description="Data/hora (UTC) de expiração do token")


class UsuarioResponse(BaseModel):
    usuario: str = Field(..., examples=["treinamento"])
    expira_em: datetime


UnidadeMedida = Literal["KG", "T", "L"]


class ProdutoBase(BaseModel):
    fabrica: str = Field(..., min_length=1, max_length=100, description="Fábrica", examples=["Fábrica São Paulo"])
    codigo_material: str = Field(..., min_length=1, max_length=50, description="Código do Material", examples=["MAT-0001"])
    nome_material: str = Field(..., min_length=1, max_length=200, description="Nome do Material", examples=["Parafuso Sextavado M8"])
    lote: str = Field(..., min_length=1, max_length=50, description="Lote", examples=["L2026-10"])
    data_producao: date = Field(..., description="Data de Produção (AAAA-MM-DD)", examples=["2026-10-01"])
    data_validade: date = Field(..., description="Data de Validade (AAAA-MM-DD)", examples=["2027-10-01"])
    quantidade: int = Field(..., ge=0, description="Quantidade (inteiro >= 0)", examples=[150])
    unidade_medida: UnidadeMedida = Field(..., description="Unidade de Medida: KG, T ou L", examples=["KG"])
    observacao: str = Field("", max_length=1000, description="Observação (opcional)", examples=["Armazenar em local seco"])

    @model_validator(mode="after")
    def validar_datas(self):
        if self.data_validade < self.data_producao:
            raise ValueError("A Data de Validade não pode ser anterior à Data de Produção")
        return self


class ProdutoCreate(ProdutoBase):
    pass


class ProdutoUpdate(ProdutoBase):
    pass


class ProdutoPatch(BaseModel):
    """Todos os campos são opcionais: envie apenas os que deseja alterar."""

    fabrica: str | None = Field(None, min_length=1, max_length=100, description="Fábrica")
    codigo_material: str | None = Field(None, min_length=1, max_length=50, description="Código do Material")
    nome_material: str | None = Field(None, min_length=1, max_length=200, description="Nome do Material")
    lote: str | None = Field(None, min_length=1, max_length=50, description="Lote")
    data_producao: date | None = Field(None, description="Data de Produção (AAAA-MM-DD)")
    data_validade: date | None = Field(None, description="Data de Validade (AAAA-MM-DD)")
    quantidade: int | None = Field(None, ge=0, description="Quantidade (inteiro >= 0)")
    unidade_medida: UnidadeMedida | None = Field(None, description="Unidade de Medida: KG, T ou L")
    observacao: str | None = Field(None, max_length=1000, description="Observação")

    model_config = {"json_schema_extra": {"examples": [{"quantidade": 200}]}}


class Produto(ProdutoBase):
    id: int = Field(..., examples=[1])
    criado_em: datetime
    atualizado_em: datetime


class Mensagem(BaseModel):
    detail: str


def row_to_produto(row: sqlite3.Row) -> Produto:
    return Produto(**dict(row))


def para_db(dados: dict) -> dict:
    """Converte os valores do schema para gravação no SQLite."""
    valores = {}
    for k, v in dados.items():
        if isinstance(v, str):
            v = v.strip()
        elif isinstance(v, date):
            v = v.isoformat()
        valores[k] = v
    return valores


# ---------------------------------------------------------------------------
# Autenticação JWT
# ---------------------------------------------------------------------------
bearer_scheme = HTTPBearer(
    scheme_name="JWT Bearer",
    description="Faça login em POST /api/auth/login, copie o access_token e cole aqui (sem a palavra 'Bearer').",
    auto_error=False,
)


def criar_token(usuario: str) -> tuple[str, datetime]:
    expira = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_EXPIRA_MINUTOS)
    payload = {"sub": usuario, "exp": expira, "iat": datetime.now(timezone.utc)}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM), expira


def usuario_atual(
    credenciais: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> dict:
    erro = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido ou ausente",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if credenciais is None or credenciais.scheme.lower() != "bearer":
        raise erro
    try:
        payload = jwt.decode(credenciais.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        erro.detail = "Token expirado"
        raise erro
    except jwt.InvalidTokenError:
        raise erro
    if payload.get("sub") != USUARIO:
        raise erro
    return payload


# ---------------------------------------------------------------------------
# Aplicação
# ---------------------------------------------------------------------------
@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


tags_metadata = [
    {"name": "Autenticação", "description": "Obtenção e validação do token JWT."},
    {"name": "Produtos", "description": "Operações CRUD de produtos. **Requer token JWT Bearer.**"},
]

app = FastAPI(
    title="API - Cadastro de Produtos (Treinamento)",
    version="1.0.0",
    description=(
        "API de treinamento para automação com **PyAutoGUI** e **Rest API**.\n\n"
        "### Como autenticar no Swagger\n"
        "1. Execute `POST /api/auth/login` com `usuario=treinamento` e `senha=12345678`.\n"
        "2. Copie o valor de `access_token`.\n"
        "3. Clique no botão **Authorize** (cadeado) e cole o token.\n\n"
        "### Formato das datas\n"
        "Na API as datas usam o formato ISO `AAAA-MM-DD` (ex.: `2026-10-12`)."
    ),
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)


# ----------------------------- Autenticação --------------------------------


@app.post(
    "/api/auth/login",
    response_model=TokenResponse,
    tags=["Autenticação"],
    summary="Realiza login e retorna o token JWT",
    responses={401: {"model": Mensagem, "description": "Usuário ou senha inválidos"}},
)
def login(dados: LoginRequest):
    if dados.usuario != USUARIO or dados.senha != SENHA:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
    token, expira = criar_token(dados.usuario)
    return TokenResponse(access_token=token, token_type="bearer", expira_em=expira)


@app.get(
    "/api/auth/me",
    response_model=UsuarioResponse,
    tags=["Autenticação"],
    summary="Retorna o usuário do token (útil para verificar se ainda está logado)",
    responses={401: {"model": Mensagem}},
)
def me(payload: dict = Depends(usuario_atual)):
    return UsuarioResponse(
        usuario=payload["sub"],
        expira_em=datetime.fromtimestamp(payload["exp"], tz=timezone.utc),
    )


# ------------------------------- Produtos -----------------------------------


@app.get(
    "/api/produtos",
    response_model=list[Produto],
    tags=["Produtos"],
    summary="Lista os produtos (com filtros opcionais)",
    responses={401: {"model": Mensagem}},
)
def listar_produtos(
    codigo_material: str | None = Query(None, description="Filtra por código (contém)"),
    lote: str | None = Query(None, description="Filtra por lote (contém)"),
    fabrica: str | None = Query(None, description="Filtra por fábrica (contém)"),
    _: dict = Depends(usuario_atual),
):
    sql = "SELECT * FROM produtos WHERE 1=1"
    params: list = []
    for coluna, valor in (("codigo_material", codigo_material), ("lote", lote), ("fabrica", fabrica)):
        if valor:
            sql += f" AND {coluna} LIKE ?"
            params.append(f"%{valor}%")
    sql += " ORDER BY id DESC"
    with get_conn() as conn:
        rows = conn.execute(sql, params).fetchall()
    return [row_to_produto(r) for r in rows]


@app.get(
    "/api/produtos/{produto_id}",
    response_model=Produto,
    tags=["Produtos"],
    summary="Consulta um produto pelo ID",
    responses={401: {"model": Mensagem}, 404: {"model": Mensagem}},
)
def obter_produto(produto_id: int, _: dict = Depends(usuario_atual)):
    with get_conn() as conn:
        row = conn.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return row_to_produto(row)


@app.post(
    "/api/produtos",
    response_model=Produto,
    status_code=status.HTTP_201_CREATED,
    tags=["Produtos"],
    summary="Cadastra um novo produto",
    responses={401: {"model": Mensagem}},
)
def criar_produto(produto: ProdutoCreate, _: dict = Depends(usuario_atual)):
    agora = datetime.now().isoformat(timespec="seconds")
    valores = {**para_db(produto.model_dump()), "criado_em": agora, "atualizado_em": agora}
    colunas = ", ".join(valores)
    marcadores = ", ".join("?" for _ in valores)
    with get_conn() as conn:
        cur = conn.execute(f"INSERT INTO produtos ({colunas}) VALUES ({marcadores})", tuple(valores.values()))
        row = conn.execute("SELECT * FROM produtos WHERE id = ?", (cur.lastrowid,)).fetchone()
    return row_to_produto(row)


@app.put(
    "/api/produtos/{produto_id}",
    response_model=Produto,
    tags=["Produtos"],
    summary="Atualiza todos os dados de um produto",
    responses={401: {"model": Mensagem}, 404: {"model": Mensagem}},
)
def atualizar_produto(produto_id: int, produto: ProdutoUpdate, _: dict = Depends(usuario_atual)):
    valores = {**para_db(produto.model_dump()), "atualizado_em": datetime.now().isoformat(timespec="seconds")}
    sets = ", ".join(f"{k} = ?" for k in valores)
    with get_conn() as conn:
        cur = conn.execute(f"UPDATE produtos SET {sets} WHERE id = ?", (*valores.values(), produto_id))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        row = conn.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
    return row_to_produto(row)


@app.patch(
    "/api/produtos/{produto_id}",
    response_model=Produto,
    tags=["Produtos"],
    summary="Atualiza parcialmente um produto (somente os campos enviados)",
    responses={401: {"model": Mensagem}, 404: {"model": Mensagem}, 422: {"model": Mensagem}},
)
def atualizar_parcial_produto(produto_id: int, alteracoes: ProdutoPatch, _: dict = Depends(usuario_atual)):
    campos = alteracoes.model_dump(exclude_unset=True)
    if any(valor is None for valor in campos.values()):
        raise HTTPException(status_code=422, detail="Os campos enviados não podem ser nulos")

    with get_conn() as conn:
        row = conn.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
        if row is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        if not campos:
            return row_to_produto(row)

        # Combina os dados atuais com as alterações e valida o resultado (ex.: datas)
        atual = ProdutoBase(**{k: row[k] for k in ProdutoBase.model_fields})
        try:
            novo = ProdutoBase(**{**atual.model_dump(), **campos})
        except ValueError as e:
            raise HTTPException(status_code=422, detail=str(e.errors()[0]["msg"]).removeprefix("Value error, "))

        valores = para_db({k: getattr(novo, k) for k in campos})
        valores["atualizado_em"] = datetime.now().isoformat(timespec="seconds")

        sets = ", ".join(f"{k} = ?" for k in valores)
        conn.execute(f"UPDATE produtos SET {sets} WHERE id = ?", (*valores.values(), produto_id))
        row = conn.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,)).fetchone()
    return row_to_produto(row)


@app.delete(
    "/api/produtos/{produto_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Produtos"],
    summary="Exclui um produto",
    responses={401: {"model": Mensagem}, 404: {"model": Mensagem}},
)
def excluir_produto(produto_id: int, _: dict = Depends(usuario_atual)):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM produtos WHERE id = ?", (produto_id,))
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


# ------------------------------ Páginas HTML --------------------------------
# A autenticação das páginas é feita no navegador (token salvo no localStorage).

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/login")


@app.get("/login", include_in_schema=False)
def pagina_login():
    return FileResponse(STATIC_DIR / "login.html")


@app.get("/cadastro", include_in_schema=False)
def pagina_cadastro():
    return FileResponse(STATIC_DIR / "cadastro.html")


@app.get("/produtos", include_in_schema=False)
def pagina_produtos():
    return FileResponse(STATIC_DIR / "produtos.html")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=False)
