"""Animações da aula 04 - seleção, filtros e ordenação."""

from pandas_comum import *  # noqa: F401,F403

COLS = ["id_ordem", "unidade", "turno", "produzido"]
LARG = [1.6, 1.85, 0.95, 1.85]


def linhas_amostra():
    return [[l[0], l[1], l[2], fmt(l[5])] for l in AMOSTRA]


def badge_bool(ax, x, y, valor, alpha=1.0, tamanho=10.5):
    etiqueta(ax, x, y, "True" if valor else "False", VERDE if valor else VERMELHO, alpha=alpha, tamanho=tamanho)


# -----------------------------------------------------------------------------
# A máscara de True/False
# -----------------------------------------------------------------------------
def filtro_mascara(ax, q):
    titulo(ax, "Filtro: uma condição gera True/False para cada linha")

    codigo(ax, 0.6, 7.25, digitado('condicao = producao["unidade"] == "Unidade_B"', q, 2, 12), tamanho=12.5)
    x0, y0, h = 0.9, 6.0, 0.48
    mascara = [l[1] == "Unidade_B" for l in AMOSTRA]
    some = progresso(q, 52, 60)

    def estilo(r, c):
        if q >= 16 + r * 4 and c == 1:
            return {"fc": VERDE_CLARO if mascara[r] else VERMELHO_CLARO}
        return None

    grade(ax, x0, y0, COLS, linhas_amostra(), LARG, indice=list(range(6)), estilo=estilo, h=h, tamanho=10.5,
          alpha_linha=lambda r: 1.0 if mascara[r] else 1 - 0.75 * some)
    texto(ax, 8.15, y0, "condicao", tamanho=10.5, mono=True, negrito=True, ha="center", alpha=progresso(q, 14, 18))
    for r, ok in enumerate(mascara):
        badge_bool(ax, 8.15, y0 - (r + 1) * h, ok, alpha=progresso(q, 16 + r * 4, 19 + r * 4))

    codigo(ax, 0.6, 2.4, digitado("producao[condicao]", q, 44, 52), tamanho=13.5)
    texto(ax, 0.6, 1.75, "→ ficam só as linhas onde a condição é True", tamanho=11.5, cor=SUAVE, alpha=progresso(q, 52, 56))

    # resultado
    selecionadas = [r for r, ok in enumerate(mascara) if ok]
    for i, r in enumerate(selecionadas):
        voo = progresso(q, 58 + i * 5, 70 + i * 5)
        if voo > 0:
            y_origem = y0 - (r + 1) * h
            y_destino = 4.6 - i * h
            linha = linhas_amostra()[r]
            grade(ax, mix(x0, 9.3, voo), 0, COLS, [linha], LARG, h=h, tamanho=10.5, cabecalho=False,
                  y_linha=lambda _r, yo=y_origem, yd=y_destino, v=voo: mix(yo, yd, v),
                  estilo=lambda rr, cc: {"fc": VERDE_CLARO})
    texto(ax, 9.3, 5.2, "resultado", tamanho=11, negrito=True, cor=VERDE, alpha=progresso(q, 70, 74))


# -----------------------------------------------------------------------------
# Várias condições: & e |
# -----------------------------------------------------------------------------
def filtro_e_ou(ax, q):
    titulo(ax, "Várias condições:  & (E)  e  | (OU)")

    x0, y0, h = 0.9, 6.0, 0.5
    cols = ["id_ordem", "unidade", "turno"]
    larg = [1.6, 1.85, 0.95]
    linhas = [[l[0], l[1], l[2]] for l in AMOSTRA]
    c1 = [l[1] == "Unidade_B" for l in AMOSTRA]
    c2 = [l[2] == "C" for l in AMOSTRA]
    e = [a and b for a, b in zip(c1, c2)]
    ou = [a or b for a, b in zip(c1, c2)]

    passo = 26
    etapa = int((q - 6) // passo) if q >= 6 else -1   # 0: c1, 1: c2, 2: &, 3: |
    colunas_bool = [(6.7, 'unidade=="B"', c1), (8.9, 'turno=="C"', c2), (10.9, "&", e), (12.7, "|", ou)]
    resultado = e if etapa == 2 else (ou if etapa >= 3 else None)

    def estilo(r, c):
        if resultado is not None and resultado[r] and q >= 6 + etapa * passo + 14:
            return {"fc": VERDE_CLARO}
        return None

    grade(ax, x0, y0, cols, linhas, larg, indice=list(range(6)), estilo=estilo, h=h, tamanho=10.5)
    for k, (x, rotulo, valores) in enumerate(colunas_bool):
        q0 = 6 + k * passo
        aparece = progresso(q, q0, q0 + 4)
        texto(ax, x, y0, rotulo, tamanho=10.5 if k < 2 else 15, mono=True, negrito=True, ha="center", alpha=aparece,
              cor=TINTA if k < 2 else LARANJA)
        for r, v in enumerate(valores):
            badge_bool(ax, x, y0 - (r + 1) * h, v, alpha=progresso(q, q0 + 4 + r * 1.5, q0 + 7 + r * 1.5))

    if etapa == 2:
        texto(ax, 0.9, 2.0, "&  → True só se as DUAS forem True", tamanho=13, negrito=True, cor=LARANJA)
    elif etapa >= 3:
        texto(ax, 0.9, 2.0, "|  → True se PELO MENOS UMA for True", tamanho=13, negrito=True, cor=LARANJA)
    codigo(ax, 0.6, 7.25, 'producao[(producao["unidade"] == "Unidade_B") & (producao["turno"] == "C")]', tamanho=10.5)
    legenda(ax, "Cada condição entre PARÊNTESES · use & e | (e não and / or)", progresso(q, 30, 36))


# -----------------------------------------------------------------------------
# Ordenando
# -----------------------------------------------------------------------------
def ordenacao(ax, q):
    titulo(ax, "sort_values: ordenando a tabela")

    codigo(ax, 0.6, 7.25, digitado('producao.sort_values("produzido", ascending=False)', q, 2, 14), tamanho=12.5)
    x0, y0, h = 3.2, 6.0, 0.55
    ordem = sorted(range(6), key=lambda r: -AMOSTRA[r][5])
    p = progresso(q, 26, 50)

    def y_linha(r):
        return mix(y0 - (r + 1) * h, y0 - (ordem.index(r) + 1) * h, p)

    def estilo(r, c):
        if c == 3:
            return {"fc": DESTAQUE}
        return None

    grade(ax, x0, y0, COLS, linhas_amostra(), LARG, h=h, tamanho=11, y_linha=y_linha, estilo=estilo)
    for i in range(6):
        texto(ax, x0 - 0.5, y0 - (i + 1) * h, f"{i + 1}º", tamanho=11, cor=LARANJA, ha="center", negrito=True,
              alpha=progresso(q, 52, 58))
    texto(ax, 10.2, 5.0, "ascending=False\n→ do MAIOR para o menor", tamanho=12, alpha=progresso(q, 16, 22))
    texto(ax, 10.2, 3.6, "ascending=True (padrão)\n→ do menor para o maior", tamanho=12, cor=SUAVE, alpha=progresso(q, 56, 62))


ANIMACOES = {
    "filtro_mascara": (filtro_mascara, 105),
    "filtro_e_ou": (filtro_e_ou, 125),
    "ordenacao": (ordenacao, 90),
}
