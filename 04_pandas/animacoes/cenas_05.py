"""Animações da aula 05 - limpeza de dados."""

from pandas_comum import *  # noqa: F401,F403

PARADAS = [["OP-0001", "0.0", None], ["OP-0002", "2.0", "Setup"], ["OP-0003", "0.0", None],
           ["OP-0004", "4.0", "Falta de energia"], ["OP-0005", "0.0", None]]
COLS = ["id_ordem", "horas_paradas", "motivo_parada"]
LARG = [1.6, 2.3, 3.0]


# -----------------------------------------------------------------------------
# fillna x dropna
# -----------------------------------------------------------------------------
def fillna_dropna(ax, q):
    titulo(ax, "Valores vazios: preencher (fillna) ou remover (dropna)?")

    x0, y0, h = 1.6, 5.9, 0.52
    b = 64
    vazias = [r for r, l in enumerate(PARADAS) if l[2] is None]

    if q < b:
        codigo(ax, 0.6, 7.25, digitado('producao["motivo_parada"].fillna("Sem parada")', q, 2, 12), tamanho=12.5)
        preenche = progresso(q, 22, 34)

        def estilo(r, c):
            if c == 2 and r in vazias:
                return {"fc": VERDE_CLARO if preenche >= 1 else VERMELHO_CLARO, "cor": VERDE if preenche >= 1 else VERMELHO}
            return None

        linhas = [[a, b_, m if m else ("Sem parada" if preenche >= 1 else "NaN")] for a, b_, m in PARADAS]
        grade(ax, x0, y0, COLS, linhas, LARG, indice=list(range(5)), estilo=estilo, h=h, tamanho=11)
        texto(ax, 9.3, 4.6, "fillna: as linhas FICAM\ne o vazio ganha um valor", tamanho=12.5, cor=VERDE, negrito=True,
              alpha=progresso(q, 34, 40))
    else:
        codigo(ax, 0.6, 7.25, digitado('producao.dropna(subset=["motivo_parada"])', q, b, b + 10), tamanho=12.5)
        some = progresso(q, b + 18, b + 28)
        sobe = progresso(q, b + 28, b + 38)
        restantes = [r for r in range(5) if r not in vazias]

        def y_linha(r):
            if r in restantes:
                return mix(y0 - (r + 1) * h, y0 - (restantes.index(r) + 1) * h, sobe)
            return y0 - (r + 1) * h

        def estilo(r, c):
            if r in vazias:
                return {"fc": VERMELHO_CLARO, "cor": VERMELHO if c == 2 else TINTA}
            return None

        linhas = [[a, b_, m if m else "NaN"] for a, b_, m in PARADAS]
        grade(ax, x0, y0, COLS, linhas, LARG, indice=list(range(5)), estilo=estilo, h=h, tamanho=11, y_linha=y_linha,
              alpha_linha=lambda r: 1 - some if r in vazias else 1)
        texto(ax, 9.3, 4.6, "dropna: as linhas SOMEM\n(perdemos 3 de 5 ordens!)", tamanho=12.5, cor=VERMELHO, negrito=True,
              alpha=progresso(q, b + 28, b + 34))
    legenda(ax, "Antes de remover, pense: esse vazio é um ERRO ou uma INFORMAÇÃO?", progresso(q, b + 40, b + 46))


# -----------------------------------------------------------------------------
# Duplicados
# -----------------------------------------------------------------------------
def duplicados(ax, q):
    titulo(ax, "Duplicados: duplicated() encontra · drop_duplicates() remove")

    linhas = [["OP-0001", "Unidade_A", "18.500"], ["OP-0002", "Unidade_B", "12.100"], ["OP-0003", "Unidade_A", "18.300"],
              ["OP-0002", "Unidade_B", "12.100"], ["OP-0004", "Unidade_C", "9.800"]]
    dup = [False, False, False, True, False]
    x0, y0, h = 1.6, 5.9, 0.52
    cols, larg = ["id_ordem", "unidade", "produzido"], [1.6, 1.85, 1.85]

    some = progresso(q, 52, 60)
    sobe = progresso(q, 60, 68)

    def y_linha(r):
        if r == 4:
            return mix(y0 - 5 * h, y0 - 4 * h, sobe)
        return y0 - (r + 1) * h

    def estilo(r, c):
        if q >= 20 and r in (1, 3):
            return {"fc": DESTAQUE if r == 1 else VERMELHO_CLARO}
        return None

    codigo(ax, 0.6, 7.25, "producao.duplicated()", tamanho=13, destaque=janela(q, 4, 46, 2, 2))
    grade(ax, x0, y0, cols, linhas, larg, indice=list(range(5)), estilo=estilo, h=h, tamanho=11, y_linha=y_linha,
          alpha_linha=lambda r: 1 - some if r == 3 else 1)
    texto(ax, 8.1, y0, "duplicated()", tamanho=10.5, mono=True, negrito=True, ha="center", alpha=progresso(q, 10, 14))
    for r, d in enumerate(dup):
        if r == 3 and some > 0:
            continue
        etiqueta(ax, 8.1, y_linha(r), "True" if d else "False", VERMELHO if d else SUAVE, tamanho=10.5,
                 alpha=progresso(q, 12 + r * 3, 15 + r * 3))
    texto(ax, 9.3, y0 - 4 * h, "← a 2ª vez que a linha aparece\n    é marcada como duplicada", tamanho=11, cor=VERMELHO,
          alpha=janela(q, 28, 52, 3, 3))

    codigo(ax, 0.6, 1.9, "producao = producao.drop_duplicates()", tamanho=13, alpha=progresso(q, 44, 48),
           destaque=janela(q, 46, 999, 2, 1))
    texto(ax, 0.6, 1.2, "subset=[\"id_ordem\"] → considera só algumas colunas", tamanho=11, cor=SUAVE, alpha=progresso(q, 70, 76))


# -----------------------------------------------------------------------------
# Convertendo textos: nomes, números e datas
# -----------------------------------------------------------------------------
def conversao_textos(ax, q):
    titulo(ax, "Tratando textos: nomes, números e datas")

    cadeias = [
        ("nome", [('"  unidade_a"', CORES["str"]), (".str.strip()", None), ('"unidade_a"', CORES["str"]),
                  (".str.title()", None), ('"Unidade_A"', CORES["str"])]),
        ("número", [('"12.345,5"', CORES["str"]), ('.replace(".", "").replace(",", ".")', None), ('"12345.5"', CORES["str"]),
                    (".astype(float)", None), ("12345.5", CORES["float"])]),
        ("data", [('"05/01/2025"', CORES["str"]), ("pd.to_datetime(..., dayfirst=True)", None), ("2025-01-05", CORES["int"])]),
    ]
    passo_item = 7
    q_atual = 4
    for k, (nome, itens) in enumerate(cadeias):
        y = 6.4 - k * 2.0
        texto(ax, 0.6, y + 0.75, nome, tamanho=12, negrito=True, cor=SUAVE, alpha=progresso(q, q_atual, q_atual + 4))
        x = 0.6
        for i, (conteudo, cor) in enumerate(itens):
            aparece = progresso(q, q_atual, q_atual + 5)
            q_atual += passo_item
            if cor is None:   # método (seta)
                largura = len(conteudo) * 0.15 + 0.35
                texto(ax, x + largura / 2, y + 0.38, conteudo, tamanho=9, mono=True, cor=LARANJA, ha="center", alpha=aparece)
                seta(ax, x + 0.05, y, x + largura - 0.05, y, cor=LARANJA, alpha=aparece, lw=1.8)
                x += largura
            else:
                largura = len(conteudo) * 0.18 + 0.4
                bloco(ax, x + largura / 2, y, conteudo, cor, w=largura, h=0.6, tamanho=11, alpha=aparece)
                x += largura + 0.1
        q_atual += 6

    legenda(ax, "texto (verde) → número (laranja) ou data (azul): só assim dá para fazer contas e filtros", progresso(q, q_atual, q_atual + 6))


ANIMACOES = {
    "fillna_dropna": (fillna_dropna, 125),
    "duplicados": (duplicados, 100),
    "conversao_textos": (conversao_textos, 140),
}
