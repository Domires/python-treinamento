"""Animações da aula 01 - introdução ao pandas."""

from pandas_comum import *  # noqa: F401,F403

PRODUTOS = [["Produto_A", 2.35, 12000], ["Produto_B", 2.80, 8500], ["Produto_C", 4.10, 3000]]


# -----------------------------------------------------------------------------
# Dicionário -> DataFrame
# -----------------------------------------------------------------------------
def dict_para_dataframe(ax, q):
    titulo(ax, "Do dicionário para a tabela (DataFrame)")

    linhas_codigo = ['dataset = {', '    "produto": ["Produto_A", "Produto_B", "Produto_C"],',
                     '    "custo_kg": [2.35, 2.80, 4.10],', '    "estoque_kg": [12000, 8500, 3000],', '}']
    ys = [7.3, 6.85, 6.4, 5.95, 5.5]
    passo = 22
    for i, (y, linha) in enumerate(zip(ys, linhas_codigo)):
        k = i - 1
        ativo = janela(q, 6 + k * passo, 6 + (k + 1) * passo, 2, 2) if 0 <= k < 3 else 0
        codigo(ax, 0.6, y, linha, tamanho=11.5, destaque=ativo)
    codigo(ax, 0.6, 4.8, "df = pd.DataFrame(dataset)", tamanho=12, alpha=progresso(q, 2, 6))

    larguras = [2.3, 2.0, 2.4]
    x0, y0 = 5.5, 3.9
    colunas = ["produto", "custo_kg", "estoque_kg"]
    xs = x_colunas(x0, larguras)

    def estilo(r, c):
        return None

    # cabeçalho e valores aparecem coluna por coluna
    for c, nome in enumerate(colunas):
        q0 = 6 + c * passo
        celula(ax, xs[c], y0, larguras[c], 0.48, nome, fc=COR_CAB, ec="none", negrito=True, alpha=progresso(q, q0, q0 + 5),
               tamanho=11)
        for r, linha in enumerate(PRODUTOS):
            voo = progresso(q, q0 + 4 + r * 3, q0 + 12 + r * 3)
            valor = linha[c] if c == 0 else (f"{linha[c]:.2f}" if c == 1 else linha[c])
            y_destino = y0 - (r + 1) * 0.48
            if voo >= 1:
                celula(ax, xs[c], y_destino, larguras[c], 0.48, valor, tamanho=11)
            elif voo > 0:
                trecho = f'"{linha[0]}"' if c == 0 else str(valor)
                x_origem = x_do_trecho(0.6, linhas_codigo[c + 1], trecho, tamanho=11.5) if trecho in linhas_codigo[c + 1] else 4
                valor_solto(ax, mix(x_origem, xs[c] + larguras[c] / 2, voo), mix(ys[c + 1], y_destino, voo), str(valor),
                            cor=CORES["dict"], tamanho=11)

    # índice
    q_indice = 6 + 3 * passo + 4
    for r in range(3):
        celula(ax, x0 - 0.6, y0 - (r + 1) * 0.48, 0.6, 0.48, r, fc=COR_INDICE, ec="none", cor=SUAVE,
               alpha=progresso(q, q_indice, q_indice + 5), tamanho=10.5)
    texto(ax, x0 - 0.3, y0 - 2.15, "↑ índice criado\n   automaticamente", tamanho=10, cor=SUAVE,
          alpha=progresso(q, q_indice + 4, q_indice + 9))
    legenda(ax, "Cada CHAVE vira uma COLUNA · cada LISTA vira os valores da coluna", progresso(q, q_indice + 8, q_indice + 14))


# -----------------------------------------------------------------------------
# Anatomia de um DataFrame
# -----------------------------------------------------------------------------
def anatomia_dataframe(ax, q):
    titulo(ax, "As partes de um DataFrame")

    x0, y0, h = 1.0, 6.6, 0.5
    larguras = LARGURAS_AMOSTRA
    xs = x_colunas(x0, larguras)
    largura_total = sum(larguras)
    linhas = [[fmt(v) for v in linha] for linha in AMOSTRA]

    passo = 20
    etapa = int((q - 8) // passo) if q >= 8 else -1

    def estilo(r, c):
        if etapa == 2 and c == 5:
            return {"fc": DESTAQUE}
        if etapa == 3 and r == 2:
            return {"fc": DESTAQUE}
        return None

    grade(ax, x0, y0, COLUNAS_AMOSTRA, linhas, larguras, indice=list(range(6)), estilo=estilo, tamanho=10, h=h)
    y_fundo = y0 - 6.5 * h

    x_rotulo = x0 + largura_total + 0.4
    if etapa >= 0:
        notas = [("columns", "nomes das colunas", y0), ("index", "o \"número\" de cada linha", y0 - 3 * h),
                 ("Series", "uma COLUNA da tabela", y0 - 4 * h), ("linha", "um registro (uma ordem)", y0 - 3 * h)]
        nome, explicacao, y_nota = notas[min(etapa, 3)]
        if etapa == 0:
            retangulo(ax, x0 - 0.05, y0 - h / 2 - 0.03, largura_total + 0.1, h + 0.06, fc="none", ec=LARANJA, lw=2.5, raio=0.05)
        elif etapa == 1:
            retangulo(ax, x0 - 0.65, y_fundo + h / 2 - 0.02, 0.62, 6 * h + 0.04, fc="none", ec=LARANJA, lw=2.5, raio=0.05)
        elif etapa == 2:
            retangulo(ax, xs[5] - 0.03, y_fundo + h / 2 - 0.03, larguras[5] + 0.06, 7 * h + 0.06, fc="none", ec=LARANJA, lw=2.5, raio=0.05)
        elif etapa == 3:
            retangulo(ax, x0 - 0.05, y0 - 3 * h - h / 2 - 0.03, largura_total + 0.1, h + 0.06, fc="none", ec=LARANJA, lw=2.5, raio=0.05)
        if etapa <= 3:
            texto(ax, x_rotulo, y_nota + 0.2, nome, tamanho=14, mono=True, negrito=True, cor=LARANJA)
            texto(ax, x_rotulo, y_nota - 0.25, explicacao, tamanho=10.5, cor=SUAVE)

    q_shape = 8 + 4 * passo
    balao(ax, 7.0, 1.6, "df.shape  →  (6, 6)   = (linhas, colunas)", alpha=progresso(q, q_shape, q_shape + 6), tamanho=13)


# -----------------------------------------------------------------------------
# Nova coluna: for (linha a linha) x pandas (tudo de uma vez)
# -----------------------------------------------------------------------------
def coluna_calculada(ax, q):
    titulo(ax, "Coluna calculada: sem for, para todas as linhas")

    dados = [["Produto_A", 2.35, 12000], ["Produto_B", 2.80, 8500], ["Produto_C", 4.10, 3000],
             ["Produto_D", 3.65, 15000], ["Produto_E", 5.20, 700]]
    larguras = [2.1, 1.9, 2.3, 2.8]
    x0, y0, h = 1.0, 5.6, 0.52
    xs = x_colunas(x0, larguras)

    passo = 11
    fim_for = 10 + len(dados) * passo
    inicio_pandas = fim_for + 22
    fase_pandas = q >= inicio_pandas - 6

    if not fase_pandas:
        texto(ax, 0.6, 7.2, "Com for: uma linha de cada vez", tamanho=13, negrito=True, cor=CORES["func"])
        codigo(ax, 0.6, 6.6, "for i in range(5): valor[i] = custo[i] * estoque[i]", tamanho=11)
    else:
        texto(ax, 0.6, 7.2, "Com pandas: todas as linhas de uma vez", tamanho=13, negrito=True, cor=VERDE)
        codigo(ax, 0.6, 6.6, 'df["valor_estoque"] = df["custo_kg"] * df["estoque_kg"]', tamanho=11)

    linhas = []
    for r, (prod, custo, estoque) in enumerate(dados):
        valor = custo * estoque
        if fase_pandas:
            preenchido = q >= inicio_pandas
        else:
            preenchido = q >= 10 + r * passo + 7
        linhas.append([prod, f"{custo:.2f}".replace(".", ","), fmt(estoque), fmt(round(valor)) if preenchido else ""])

    atual = int((q - 10) // passo) if 10 <= q < fim_for else -1

    def estilo(r, c):
        if c == 3 and fase_pandas and q >= inicio_pandas:
            return {"fc": VERDE_CLARO}
        if not fase_pandas and r == atual:
            return {"fc": DESTAQUE}
        return None

    grade(ax, x0, y0, ["produto", "custo_kg", "estoque_kg", "valor_estoque"], linhas, larguras, estilo=estilo, h=h, tamanho=10.5,
          alpha_coluna=lambda c: 1.0 if c < 3 else progresso(q, 4, 8))
    if atual >= 0:
        prod, custo, estoque = dados[atual]
        ponteiro(ax, x0 - 0.3, y0 - (atual + 1) * h, tamanho=13)
        balao(ax, 12.9, y0 - (atual + 1) * h, f"{custo:.2f} × {estoque} = {custo * estoque:,.0f}".replace(",", "."),
              tamanho=11.5)
    if fase_pandas and q >= inicio_pandas:
        texto(ax, 9.6, y0 - 3 * h, "←  as 5 contas\n     de uma vez só", tamanho=12, cor=VERDE, negrito=True)
    legenda(ax, "Igual a arrastar uma fórmula no Excel: e MUITO mais rápido em bases grandes",
            progresso(q, inicio_pandas + 6, inicio_pandas + 12))


ANIMACOES = {
    "dict_para_dataframe": (dict_para_dataframe, 110),
    "anatomia_dataframe": (anatomia_dataframe, 115),
    "coluna_calculada": (coluna_calculada, 120),
}
