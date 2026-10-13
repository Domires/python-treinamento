"""Animações da aula 10 - gráficos."""

import math

from pandas_comum import *  # noqa: F401,F403

POR_UNIDADE = [("Unidade_A", 4355), ("Unidade_B", 3077), ("Unidade_D", 2078), ("Unidade_C", 1756), ("Unidade_E", 1213),
               ("Unidade_F", 241)]


# -----------------------------------------------------------------------------
# Da tabela para o gráfico
# -----------------------------------------------------------------------------
def tabela_para_grafico(ax, q):
    titulo(ax, "Da tabela para o gráfico em poucas linhas")

    linhas_codigo = ['por_unidade.plot(kind="bar")', 'plt.title("Produção por Unidade")', 'plt.ylabel("Produção (t)")',
                     'plt.savefig("grafico.png")']
    tempos = [(0, 6, 40), (1, 40, 52), (2, 52, 64), (3, 64, 999)]
    destaque_codigo(ax, 0.9, [7.25, 6.8, 6.35, 5.9], linhas_codigo, q, tempos, tamanho=11)

    grade(ax, 0.6, 5.1, ["unidade", "produzido_t"], [[u, fmt(v)] for u, v in POR_UNIDADE], [1.85, 1.85], h=0.44, tamanho=10.5)

    # eixos do gráfico
    gx, gy, gw, gh = 6.6, 1.5, 8.6, 4.2
    ax.plot([gx, gx, gx + gw], [gy + gh, gy, gy], color=TINTA, lw=1.5)
    largura_barra = gw / len(POR_UNIDADE) * 0.6
    for k, (u, v) in enumerate(POR_UNIDADE):
        cresce = progresso(q, 10 + k * 4, 22 + k * 4)
        altura = gh * 0.9 * v / POR_UNIDADE[0][1] * cresce
        xb = gx + (k + 0.5) * gw / len(POR_UNIDADE) - largura_barra / 2
        if altura > 0:
            retangulo(ax, xb, gy, largura_barra, altura, fc="steelblue", ec="none", raio=0.02)
        texto(ax, xb + largura_barra / 2, gy - 0.3, u.replace("Unidade_", ""), tamanho=10, ha="center")
        if cresce >= 1:
            texto(ax, xb + largura_barra / 2, gy + altura + 0.2, fmt(v), tamanho=8.5, ha="center", cor=SUAVE)

    texto(ax, gx + gw / 2, gy + gh + 0.35, "Produção por Unidade", tamanho=13, negrito=True, ha="center", alpha=progresso(q, 44, 50))
    if q >= 56:
        ax.text(gx - 0.45, gy + gh / 2, "Produção (t)", rotation=90, fontsize=10.5, va="center", ha="center",
                alpha=progresso(q, 56, 62), family=FONTE)
    flash = janela(q, 70, 73, 1, 4)
    if flash > 0:
        retangulo(ax, gx - 0.6, gy - 0.6, gw + 0.8, gh + 1.2, fc="white", ec="none", alpha=flash * 0.8)
    icone_arquivo(ax, 14.9, 6.8, "grafico.png", "png", alpha=progresso(q, 74, 80), tamanho=9)


# -----------------------------------------------------------------------------
# Qual gráfico usar?
# -----------------------------------------------------------------------------
def qual_grafico(ax, q):
    titulo(ax, "Qual gráfico usar? Depende da PERGUNTA")

    paineis = [(0.5, 4.2, "barras", "comparar categorias", 'kind="bar"'),
               (8.2, 4.2, "linha", "evolução no tempo", 'kind="line"'),
               (0.5, 0.6, "pizza", "partes de um todo", 'kind="pie"'),
               (8.2, 0.6, "histograma", "distribuição dos valores", 'kind="hist"')]
    for k, (x, y, nome, pergunta, kind) in enumerate(paineis):
        q0 = 4 + k * 22
        a = progresso(q, q0, q0 + 5)
        p = progresso(q, q0 + 4, q0 + 18)
        retangulo(ax, x, y, 7.3, 3.3, fc=CAIXA, ec=BORDA, alpha=a, raio=0.1)
        texto(ax, x + 0.3, y + 2.95, nome, tamanho=13, negrito=True, alpha=a)
        texto(ax, x + 0.3, y + 2.5, pergunta, tamanho=11, cor=SUAVE, alpha=a)
        texto(ax, x + 0.3, y + 0.35, kind, tamanho=10.5, mono=True, cor=CORES["func"], alpha=a)
        if a <= 0:
            continue
        cx, cy = x + 4.9, y + 1.35
        if nome == "barras":
            for i, v in enumerate([1.0, 0.75, 0.5, 0.42, 0.3]):
                retangulo(ax, x + 3.4 + i * 0.75, y + 0.45, 0.5, 1.7 * v * p + 0.001, fc="steelblue", ec="none", raio=0.02)
        elif nome == "linha":
            pontos = [0.5, 0.7, 0.55, 0.85, 0.75, 1.0, 0.9]
            n = max(1, int(len(pontos) * p))
            xs = [x + 3.4 + i * 0.6 for i in range(n)]
            ys = [y + 0.5 + 1.7 * v for v in pontos[:n]]
            ax.plot(xs, ys, color="steelblue", lw=2.5, marker="o", markersize=5)
        elif nome == "pizza":
            from matplotlib.patches import Wedge
            fatias = [0.35, 0.25, 0.2, 0.12, 0.08]
            cores = ["#2563EB", "#16A34A", "#EA580C", "#9333EA", "#DB2777"]
            inicio = 90
            for f, c in zip(fatias, cores):
                angulo = 360 * f * p
                if angulo > 0:
                    ax.add_patch(Wedge((cx, cy), 1.1, inicio - angulo, inicio, fc=c, ec="white", lw=1.5))
                inicio -= 360 * f
        else:
            alturas = [math.exp(-((i - 4) ** 2) / 6) for i in range(9)]
            for i, v in enumerate(alturas):
                retangulo(ax, x + 3.2 + i * 0.42, y + 0.45, 0.4, 1.9 * v * p + 0.001, fc="gray", ec="white", raio=0.0)


ANIMACOES = {
    "tabela_para_grafico": (tabela_para_grafico, 100),
    "qual_grafico": (qual_grafico, 110),
}
