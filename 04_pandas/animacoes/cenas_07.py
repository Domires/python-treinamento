"""Animações da aula 07 - agrupamentos e tabelas dinâmicas."""

from pandas_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# groupby: separar -> calcular -> juntar
# -----------------------------------------------------------------------------
def groupby_soma(ax, q):
    titulo(ax, "groupby: separa em grupos, calcula e junta")
    codigo(ax, 0.6, 7.25, 'producao.groupby("unidade")["produzido"].sum()', tamanho=13)

    linhas = [(l[1], l[5]) for l in AMOSTRA]
    unidades = ["Unidade_A", "Unidade_B", "Unidade_C"]
    h, larg = 0.48, [1.95, 1.75]
    x_base, y_base = 0.6, 5.9

    separa = progresso(q, 16, 32)
    calcula = progresso(q, 40, 50)
    junta = progresso(q, 58, 70)

    etapas = [("1. separa", 16), ("2. calcula", 40), ("3. junta", 58)]
    for k, (nome, q0) in enumerate(etapas):
        etiqueta(ax, 9.0 + k * 2.3, 6.6, nome, LARANJA if q >= q0 else BORDA, tamanho=11, alpha=1)

    # posição de cada linha nos grupos
    contagem = {u: 0 for u in unidades}
    destino = []
    for u, _ in linhas:
        g = unidades.index(u)
        destino.append((5.2, 5.9 - g * 1.55 - contagem[u] * h))
        contagem[u] += 1

    if junta < 1:
        texto(ax, x_base, y_base + 0.45, "unidade      produzido", tamanho=10, mono=True, negrito=True, alpha=1 - separa)
        for r, (u, v) in enumerate(linhas):
            cor = CORES_UNIDADE[u]
            x = mix(x_base, destino[r][0], separa)
            y = mix(y_base - r * h, destino[r][1], separa)
            alpha = 1 - junta
            celula(ax, x, y, larg[0], h, u, fc="white", ec=cor, cor=cor, lw=2, alpha=alpha, tamanho=10.5)
            celula(ax, x + larg[0], y, larg[1], h, fmt(v), ec=cor, lw=2, alpha=alpha, tamanho=10.5)
        for g, u in enumerate(unidades):
            soma = sum(v for uu, v in linhas if uu == u)
            yg = 5.9 - g * 1.55 - 0.24
            texto(ax, 9.1, yg, "soma →", tamanho=11, cor=SUAVE, alpha=calcula * (1 - junta))
            texto(ax, 10.3, yg, fmt(soma), tamanho=14, mono=True, negrito=True, cor=CORES_UNIDADE[u], alpha=calcula * (1 - junta))

    if junta > 0:
        resultado = [[u, fmt(sum(v for uu, v in linhas if uu == u))] for u in unidades]
        grade(ax, 5.2, 5.4, ["unidade", "produzido"], resultado, larg, h=0.55, tamanho=12, alpha=junta,
              estilo=lambda r, c: {"cor": CORES_UNIDADE[unidades[r]], "negrito": True})
        texto(ax, 9.4, 4.4, "uma linha por grupo", tamanho=12, cor=SUAVE, alpha=junta)
    legenda(ax, "É a Tabela Dinâmica do Excel: troque .sum() por .mean(), .count(), .max()...", progresso(q, 72, 78))


# -----------------------------------------------------------------------------
# pivot_table
# -----------------------------------------------------------------------------
def pivot_tabela(ax, q):
    titulo(ax, "pivot_table: linhas x colunas, como no Excel")

    longa = [[1, "Unidade_A", 362], [1, "Unidade_B", 196], [1, "Unidade_C", 133],
             [2, "Unidade_A", 316], [2, "Unidade_B", 291], [2, "Unidade_C", 152]]
    codigo(ax, 0.6, 7.25, 'pd.pivot_table(producao, index="mes", columns="unidade",', tamanho=11)
    codigo(ax, 0.6, 6.8, '               values="produzido_t", aggfunc="sum", margins=True)', tamanho=11)

    x0, y0, h = 0.6, 5.6, 0.48
    larg = [0.9, 1.85, 1.6]
    grade(ax, x0, y0, ["mes", "unidade", "produzido_t"], [[m, u, v] for m, u, v in longa], larg, h=h, tamanho=10.5)
    texto(ax, x0, 2.0, "formato \"longo\":\numa linha por mês e unidade", tamanho=10.5, cor=SUAVE)

    # grade dinâmica
    gx, gy = 7.8, 5.6
    unidades = ["Unidade_A", "Unidade_B", "Unidade_C"]
    gl = [0.9, 1.65, 1.65, 1.65, 1.25]
    gxs = x_colunas(gx, gl)
    aparece = progresso(q, 8, 14)
    celula(ax, gxs[0], gy, gl[0], h, "mes", fc=COR_CAB, ec="none", negrito=True, alpha=aparece, tamanho=10.5)
    for k, u in enumerate(unidades):
        celula(ax, gxs[k + 1], gy, gl[k + 1], h, u, fc=COR_CAB, ec="none", negrito=True, alpha=aparece, tamanho=10.5)
    for i, m in enumerate([1, 2]):
        celula(ax, gxs[0], gy - (i + 1) * h, gl[0], h, m, fc=COR_INDICE, ec="none", alpha=aparece, tamanho=10.5)

    for r, (m, u, v) in enumerate(longa):
        q0 = 18 + r * 7
        voo = progresso(q, q0, q0 + 8)
        c = unidades.index(u) + 1
        i = [1, 2].index(m)
        xd, yd = gxs[c] + gl[c] / 2, gy - (i + 1) * h
        xo, yo = x0 + larg[0] + larg[1] + larg[2] / 2, y0 - (r + 1) * h
        if voo >= 1:
            celula(ax, gxs[c], yd, gl[c], h, v, tamanho=10.5)
        elif voo > 0:
            valor_solto(ax, mix(xo, xd, voo), mix(yo, yd, voo), str(v), cor=CORES["int"], tamanho=11)

    # margens (Total)
    q_total = 18 + 6 * 7 + 6
    total = progresso(q, q_total, q_total + 6)
    celula(ax, gxs[4], gy, gl[4], h, "Total", fc="#FEF3C7", ec="none", negrito=True, alpha=total, tamanho=10.5)
    for i, m in enumerate([1, 2]):
        celula(ax, gxs[4], gy - (i + 1) * h, gl[4], h, sum(v for mm, _, v in longa if mm == m), fc="#FEF3C7", alpha=total, tamanho=10.5)
    celula(ax, gxs[0], gy - 3 * h, gl[0], h, "Total", fc="#FEF3C7", ec="none", negrito=True, alpha=total, tamanho=9.5)
    for k, u in enumerate(unidades):
        celula(ax, gxs[k + 1], gy - 3 * h, gl[k + 1], h, sum(v for _, uu, v in longa if uu == u), fc="#FEF3C7", alpha=total, tamanho=10.5)
    celula(ax, gxs[4], gy - 3 * h, gl[4], h, sum(v for *_, v in longa), fc="#FDE68A", alpha=total, tamanho=10.5, negrito=True)
    texto(ax, gx, 3.2, "index → linhas · columns → colunas\nvalues → o que é calculado", tamanho=10.5, cor=SUAVE,
          alpha=progresso(q, 20, 26))
    texto(ax, gx, 2.2, "margins=True → linha e coluna de Total", tamanho=10.5, cor=LARANJA, alpha=total)


ANIMACOES = {
    "groupby_soma": (groupby_soma, 105),
    "pivot_tabela": (pivot_tabela, 100),
}
