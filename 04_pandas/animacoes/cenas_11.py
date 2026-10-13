"""Animações da aula 11 - fechamento anual da produção."""

from pandas_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# O fluxo completo do fechamento
# -----------------------------------------------------------------------------
def fluxo_fechamento(ax, q):
    titulo(ax, "Fechamento: do arquivo bruto ao relatório")

    etapas = [
        (1.6, 5.8, "12 planilhas", "producao_mensal/", "xlsx"),
        (4.9, 5.8, "concat", "base única", None),
        (8.2, 5.8, "fillna + merge", "+ cadastros", None),
        (11.5, 5.8, "colunas", "custo, mês...", None),
        (14.4, 5.8, "groupby", "indicadores", None),
    ]
    saidas = [(4.2, 2.0, "fechamento.xlsx", "xlsx"), (8.0, 2.0, "grafico.png", "png"), (11.8, 2.0, "resumo.txt", "txt")]
    passo = 12

    for k, (x, y, nome, detalhe, icone) in enumerate(etapas):
        q0 = 6 + k * passo
        a = progresso(q, q0, q0 + 5)
        ativo = janela(q, q0, q0 + passo, 2, 2)
        if icone:
            for i in range(3):
                icone_arquivo(ax, x - 0.35 + i * 0.35, y + 0.1 - i * 0.12, "", icone, alpha=a)
            texto(ax, x, y - 1.2, nome, tamanho=11, ha="center", negrito=True, alpha=a)
            texto(ax, x, y - 1.6, detalhe, tamanho=9.5, ha="center", cor=SUAVE, mono=True, alpha=a)
        else:
            retangulo(ax, x - 1.35, y - 0.55, 2.7, 1.1, fc=DESTAQUE if ativo > 0.5 else "#EEF2FF", ec=CORES["func"], lw=2,
                      alpha=a, raio=0.12)
            texto(ax, x, y + 0.15, nome, tamanho=10.5, ha="center", negrito=True, mono=True, alpha=a)
            texto(ax, x, y - 0.25, detalhe, tamanho=9.5, ha="center", cor=SUAVE, alpha=a)
        if k > 0:
            seta(ax, etapas[k - 1][0] + (0.9 if k == 1 else 1.4), y, x - 1.4, y, cor=SUAVE, alpha=a)

    q_saida = 6 + len(etapas) * passo
    for k, (x, y, nome, tipo) in enumerate(saidas):
        a = progresso(q, q_saida + k * 6, q_saida + k * 6 + 6)
        seta(ax, 14.4, 5.2, x + 0.4, y + 0.7, cor=SUAVE, alpha=a, curva=0.15)
        icone_arquivo(ax, x, y, nome, tipo, alpha=a)

    fim = q_saida + 3 * 6 + 6
    balao(ax, 8.0, 0.55, "tudo isso em menos de 1 segundo · e de novo no mês que vem, com um clique",
          alpha=progresso(q, fim, fim + 6), tamanho=11.5, mono=False)


ANIMACOES = {
    "fluxo_fechamento": (fluxo_fechamento, 120),
}
