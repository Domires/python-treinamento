"""Desenhos usados nas animações de pandas: tabelas (DataFrames) animadas e ícones de arquivos."""

from base import *  # noqa: F401,F403

COR_CAB = "#E0F2FE"         # cabeçalho
COR_INDICE = "#F3F4F6"      # coluna do índice
VERDE_CLARO = "#DCFCE7"
VERMELHO_CLARO = "#FEE2E2"
AZUL_CLARO = "#DBEAFE"
CORES_UNIDADE = {"Unidade_A": "#2563EB", "Unidade_B": "#16A34A", "Unidade_C": "#EA580C", "Unidade_D": "#9333EA",
                 "Unidade_E": "#DB2777", "Unidade_F": "#6B7280"}

# Amostra usada em várias animações
AMOSTRA = [
    ["OP-0001", "Unidade_A", "A", "Produto_A", 20000, 18500],
    ["OP-0002", "Unidade_B", "C", "Produto_E", 15000, 12100],
    ["OP-0003", "Unidade_A", "B", "Produto_C", 18000, 18300],
    ["OP-0004", "Unidade_C", "C", "Produto_B", 12000, 9800],
    ["OP-0005", "Unidade_B", "A", "Produto_H", 16000, 15200],
    ["OP-0006", "Unidade_C", "B", "Produto_F", 14000, 13100],
]
COLUNAS_AMOSTRA = ["id_ordem", "unidade", "turno", "produto", "planejado", "produzido"]
LARGURAS_AMOSTRA = [1.6, 1.85, 0.95, 1.85, 1.85, 1.85]


def celula(ax, x, y, w, h, conteudo, fc="white", ec=BORDA, cor=TINTA, alpha=1.0, tamanho=10, negrito=False, lw=1.0,
           ha="left"):
    """Uma célula (x, y = CANTO ESQUERDO, centro vertical)."""
    if alpha <= 0:
        return
    ax.add_patch(FancyBboxPatch((x + 0.02, y - h / 2 + 0.02), w - 0.04, h - 0.04, boxstyle="round,pad=0,rounding_size=0.04",
                                fc=fc, ec=ec, lw=lw, alpha=alpha))
    if conteudo is not None and conteudo != "":
        xt = x + 0.1 if ha == "left" else x + w / 2
        # reduz a fonte se o texto não couber na célula (1 caractere mono = 0,0167 x tamanho)
        tamanho = min(tamanho, (w - 0.18) / (max(len(str(conteudo)), 1) * 0.0167))
        ax.text(xt, y, str(conteudo), fontsize=tamanho, family=MONO, color=cor, va="center", ha=ha, alpha=alpha,
                weight="bold" if negrito else "normal")


def grade(ax, x, y, colunas, linhas, larguras, indice=None, h=0.46, tamanho=10, alpha=1.0, estilo=None,
          alpha_linha=None, y_linha=None, cabecalho=True, largura_indice=0.6, alpha_coluna=None):
    """Desenha um DataFrame.

    x, y        -> canto esquerdo e centro vertical do CABEÇALHO (o índice fica à esquerda de x)
    estilo      -> função (linha, coluna) -> dict(fc=..., ec=..., cor=..., negrito=...) ou None
    alpha_linha -> função (linha) -> alpha
    y_linha     -> função (linha) -> y do centro da linha (para animar linhas trocando de lugar)
    alpha_coluna-> função (coluna) -> alpha
    """
    xs = [x]
    for w in larguras[:-1]:
        xs.append(xs[-1] + w)
    if cabecalho:
        for c, (nome, xc, w) in enumerate(zip(colunas, xs, larguras)):
            a = alpha * (alpha_coluna(c) if alpha_coluna else 1)
            celula(ax, xc, y, w, h, nome, fc=COR_CAB, ec="none", alpha=a, tamanho=tamanho, negrito=True)
    for r, linha in enumerate(linhas):
        yr = y_linha(r) if y_linha else y - (r + 1) * h
        a_l = alpha * (alpha_linha(r) if alpha_linha else 1)
        if a_l <= 0:
            continue
        if indice is not None:
            celula(ax, x - largura_indice, yr, largura_indice, h, indice[r], fc=COR_INDICE, ec="none", cor=SUAVE, alpha=a_l,
                   tamanho=tamanho - 0.5)
        for c, (valor, xc, w) in enumerate(zip(linha, xs, larguras)):
            a = a_l * (alpha_coluna(c) if alpha_coluna else 1)
            e = (estilo(r, c) if estilo else None) or {}
            celula(ax, xc, yr, w, h, valor, fc=e.get("fc", "white"), ec=e.get("ec", BORDA), cor=e.get("cor", TINTA),
                   alpha=a, tamanho=tamanho, negrito=e.get("negrito", False), lw=e.get("lw", 1.0))
    return xs


def x_colunas(x, larguras):
    """Posição x do início de cada coluna."""
    xs = [x]
    for w in larguras[:-1]:
        xs.append(xs[-1] + w)
    return xs


def fmt(valor):
    """Número com separador de milhar no padrão brasileiro."""
    if isinstance(valor, float):
        return f"{valor:,.3f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if isinstance(valor, int):
        return f"{valor:,}".replace(",", ".")
    return valor


def icone_arquivo(ax, x, y, nome, tipo="xlsx", alpha=1.0, tamanho=10):
    """Ícone de arquivo (x, y = CENTRO do ícone) com o nome embaixo."""
    if alpha <= 0:
        return
    cores = {"xlsx": "#16A34A", "csv": "#0891B2", "png": "#9333EA", "txt": "#6B7280", "json": "#CA8A04"}
    cor = cores.get(tipo, SUAVE)
    retangulo(ax, x - 0.45, y - 0.55, 0.9, 1.1, fc="white", ec=cor, lw=2, alpha=alpha, raio=0.06)
    retangulo(ax, x - 0.45, y - 0.55, 0.9, 0.38, fc=cor, ec="none", alpha=alpha, raio=0.06)
    texto(ax, x, y - 0.36, tipo.upper(), tamanho=8.5, cor="white", ha="center", negrito=True, alpha=alpha)
    for i in range(3):
        ax.plot([x - 0.3, x + 0.3], [y + 0.32 - i * 0.16] * 2, color=cor, lw=1, alpha=alpha * 0.7)
    texto(ax, x, y - 0.85, nome, tamanho=tamanho, ha="center", mono=True, alpha=alpha)
