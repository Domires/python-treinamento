"""Animações da aula 05 - cadastrando (POST)."""

from api_comum import *  # noqa: F401,F403

BASE = [[9, "MAT-0009", "Feijão", 6], [10, "MAT-0010", "Vinagre", 450]]
LARG = (0.6, 1.4, 2.1, 0.8)


# -----------------------------------------------------------------------------
# POST: cadastrando
# -----------------------------------------------------------------------------
def post_cadastro(ax, q):
    titulo(ax, "POST: enviando um produto novo no corpo (body)")

    campos = [('"codigo_material"', '"MAT-9999"'), ('"nome_material"', '"Produto de Teste"'),
              ('"quantidade"', "100"), ('"unidade_medida"', '"KG"'), ('"data_producao"', '"2026-10-01"')]
    texto(ax, 0.6, 7.25, "produto = {", tamanho=11.5, mono=True)
    for i, (k, v) in enumerate(campos):
        texto(ax, 0.9, 6.8 - i * 0.42, f"{k}: {v},", tamanho=10.5, mono=True, alpha=progresso(q, 2 + i * 2, 6 + i * 2))
    texto(ax, 0.6, 4.65, "}", tamanho=11.5, mono=True)
    codigo(ax, 0.6, 4.0, 'requests.post(url, json=produto, headers=headers)', tamanho=11, destaque=janela(q, 14, 50, 2, 2))

    servidor(ax, 13.8, 6.2, destaque=janela(q, 30, 38, 2, 2))
    ida = viagem(q, 18, 12)
    if 16 <= q and ida < 1:
        pacote(ax, mix(7.4, 10.4, ida), 5.6, "POST /api/produtos", ['{"codigo_material": "MAT-9999",', ' "nome_material": ..., ...}'],
               cor=CORES_VERBO["POST"], w=5.2)

    entra = progresso(q, 34, 42)
    linhas = BASE + [[11, "MAT-9999", "Teste", 100]]
    banco(ax, 10.8, 3.6, linhas, larguras=LARG, alphas={2: entra}, destaques={2: ("#DCFCE7", VERDE)}, titulo_banco="banco")
    texto(ax, 10.8, 1.5, "id 11 gerado pelo SISTEMA", tamanho=10.5, cor=VERDE, alpha=progresso(q, 42, 46))

    volta = viagem(q, 46, 12)
    if q >= 46:
        pacote(ax, mix(10.8, 5.0, volta), 2.0, "201 Created", ['{"id": 11, "codigo_material": "MAT-9999",',
                                                                ' "criado_em": "2026-10-12T10:10", ...}'], cor=COR_RESP, w=6.4)
    texto(ax, 0.6, 0.65, 'resposta.json()["id"]  →  11', tamanho=12, mono=True, alpha=progresso(q, 64, 70))


# -----------------------------------------------------------------------------
# 422: dados inválidos
# -----------------------------------------------------------------------------
def erro_422(ax, q):
    titulo(ax, "422: a API confere os dados e explica o erro")

    campos = [("fabrica", '"Fábrica São Paulo"', True), ("codigo_material", '"MAT-9999"', True),
              ("data_producao", '"01/10/2026"', False), ("quantidade", "100", True), ("unidade_medida", '"CX"', False)]
    servidor(ax, 13.8, 6.2, destaque=janela(q, 18, 60, 2, 2))
    texto(ax, 0.6, 7.3, "produto_errado = {", tamanho=11.5, mono=True)
    for i, (k, v, ok) in enumerate(campos):
        y = 6.75 - i * 0.55
        q_check = 20 + i * 7
        verificado = q >= q_check
        if verificado and not ok:
            retangulo(ax, 0.8, y - 0.22, 7.2, 0.44, fc="#FEE2E2", ec=VERMELHO, lw=1.5, raio=0.05)
        texto(ax, 0.95, y, f'"{k}": {v},', tamanho=11, mono=True)
        if verificado:
            texto(ax, 8.4, y, "✓" if ok else "✗", tamanho=15, cor=VERDE if ok else VERMELHO, ha="center", negrito=True)
    texto(ax, 0.6, 3.9, "}", tamanho=11.5, mono=True)
    texto(ax, 9.0, 4.4, "a API valida\ncampo por campo", tamanho=11, cor=SUAVE, alpha=janela(q, 18, 60, 2, 2))

    volta = viagem(q, 58, 12)
    if q >= 58:
        pacote(ax, mix(11.5, 7.8, volta), 2.0, "422 Unprocessable Entity",
               ['data_producao  -> data inválida (use AAAA-MM-DD)', "unidade_medida -> use 'KG', 'T' ou 'L'"],
               cor=LARANJA, w=8.6)
    texto(ax, 0.6, 0.55, "Nada foi cadastrado: leia o 'detail' da resposta para corrigir", tamanho=11, cor=SUAVE,
          alpha=progresso(q, 76, 82))


ANIMACOES = {
    "post_cadastro": (post_cadastro, 100),
    "erro_422": (erro_422, 105),
}
