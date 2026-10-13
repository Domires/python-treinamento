"""Animações da aula 06 - if / elif / else."""

from base import *  # noqa: F401,F403


def badge_bool(ax, x, y, valor, alpha=1.0, tamanho=12):
    etiqueta(ax, x, y, "True" if valor else "False", VERDE if valor else VERMELHO, alpha=alpha, tamanho=tamanho)


# -----------------------------------------------------------------------------
# Fluxograma do if / else
# -----------------------------------------------------------------------------
def if_fluxo(ax, q):
    titulo(ax, "if / else: o programa escolhe um caminho")

    ciclo = 62
    rodada = min(1, int(q // ciclo))
    q0 = rodada * ciclo
    idade = [20, 15][rodada]
    verdadeiro = idade >= 18

    caixa(ax, 1.9, 6.0, "idade", str(idade), cor=CORES["int"], w=2.2, h=1.2,
          destaque=janela(q, q0 + 2, q0 + 10, 2, 2))

    avalia = janela(q, q0 + 8, q0 + 22, 2, 2)
    caminho = progresso(q, q0 + 20, q0 + 26) * (1 - progresso(q, ciclo * (rodada + 1) - 4, ciclo * (rodada + 1)))
    if rodada == 1 and q >= 2 * ciclo - 4:
        caminho = 1
    final = progresso(q, q0 + 34, q0 + 40) * (1 - progresso(q, ciclo * (rodada + 1) - 4, ciclo * (rodada + 1)))
    if rodada == 1 and q >= 2 * ciclo - 4:
        final = 1

    losango(ax, 8.0, 6.0, 4.6, 1.8, "idade >= 18 ?", fc=DESTAQUE if avalia > 0.5 else CAIXA)
    badge_bool(ax, 11.1, 6.6, verdadeiro, alpha=progresso(q, q0 + 12, q0 + 16) if q < ciclo * (rodada + 1) - 4 or rodada == 1 else 0)

    cor_sim = LARANJA if (verdadeiro and caminho > 0.5) else BORDA
    cor_nao = LARANJA if (not verdadeiro and caminho > 0.5) else BORDA
    seta(ax, 5.7, 6.0, 4.0, 4.35, cor=cor_sim, lw=3)
    seta(ax, 10.3, 6.0, 12.0, 4.35, cor=cor_nao, lw=3)
    texto(ax, 4.2, 5.6, "True", tamanho=11, cor=VERDE, negrito=True)
    texto(ax, 11.4, 5.6, "False", tamanho=11, cor=VERMELHO, negrito=True)

    for x, rotulo, ativo in [(4.0, 'print("Adulto")', verdadeiro), (12.0, 'print("Menor de idade")', not verdadeiro)]:
        aceso = caminho > 0.5 and ativo
        retangulo(ax, x - 2.6, 3.35, 5.2, 1.0, fc=DESTAQUE if aceso else CAIXA, ec=LARANJA if aceso else BORDA, lw=2)
        texto(ax, x, 3.85, rotulo, tamanho=11, mono=True, ha="center")
    texto(ax, 4.0, 2.95, "if", tamanho=11, cor=SUAVE, ha="center", mono=True)
    texto(ax, 12.0, 2.95, "else", tamanho=11, cor=SUAVE, ha="center", mono=True)

    seta(ax, 4.0, 2.75, 7.0, 1.75, cor=LARANJA if (verdadeiro and final > 0.5) else BORDA, lw=2.5)
    seta(ax, 12.0, 2.75, 9.0, 1.75, cor=LARANJA if (not verdadeiro and final > 0.5) else BORDA, lw=2.5)
    retangulo(ax, 6.2, 1.05, 3.6, 0.8, fc=DESTAQUE if final > 0.5 else CAIXA, ec=BORDA)
    texto(ax, 8.0, 1.45, "o programa continua", tamanho=11, ha="center")


# -----------------------------------------------------------------------------
# if / elif / else: testa de cima para baixo e para no primeiro True
# -----------------------------------------------------------------------------
def elif_cascata(ax, q):
    titulo(ax, "elif: testa de cima para baixo")
    caixa(ax, 13.3, 6.4, "idade", "40", cor=CORES["int"], w=2.2, h=1.1)

    linhas = ["if idade <= 12:", '    print("Criança")', "elif idade < 18:", '    print("Jovem")',
              "elif idade < 60:", '    print("Adulto")', "else:", '    print("Idoso")']
    ys = [7.0 - k * 0.72 for k in range(len(linhas))]
    testes = {0: (10, False), 2: (28, False), 4: (46, True)}
    ignoradas = progresso(q, 76, 84)

    for k, (y, linha) in enumerate(zip(ys, linhas)):
        ativo = 0
        if k in testes:
            ativo = janela(q, testes[k][0], testes[k][0] + 14, 2, 2)
        if k == 5:
            ativo = janela(q, 62, 74, 2, 2)
        alpha = 1 - 0.7 * ignoradas if k in (6, 7) else 1
        codigo(ax, 1.4, y, linha, destaque=ativo, tamanho=14, alpha=alpha)
        ponteiro(ax, 0.95, y, alpha=ativo)
        if k in testes:
            badge_bool(ax, 6.6, y, testes[k][1], alpha=progresso(q, testes[k][0] + 5, testes[k][0] + 9))
    texto(ax, 6.0, (ys[6] + ys[7]) / 2, "← nem é testado", tamanho=12, cor=SUAVE, alpha=ignoradas)

    painel(ax, 10.2, 2.3, 5.2, 2.2, "Terminal", escuro=True)
    saida_terminal(ax, 10.5, 3.4, "Adulto", alpha=progresso(q, 66, 70), tamanho=14)

    legenda(ax, "O Python para no PRIMEIRO teste verdadeiro", progresso(q, 80, 88))


ANIMACOES = {
    "if_fluxo": (if_fluxo, 140),
    "elif_cascata": (elif_cascata, 125),
}
