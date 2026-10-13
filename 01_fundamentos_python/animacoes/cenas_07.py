"""Animações da aula 07 - match / case."""

from base import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# match: o valor é comparado com cada case até encontrar o certo
# -----------------------------------------------------------------------------
def match_casos(ax, q):
    titulo(ax, "match: procurando o case que combina")

    casos = [("1", "Segunda"), ("2", "Terça"), ("3", "Quarta"), ("4", "Quinta"), ("5", "Sexta"),
             ("6", "Sábado"), ("7", "Domingo"), ("_", "Não\nencontrado")]
    x_casos = [1.15 + k * 1.95 for k in range(len(casos))]
    y_casos = 4.3

    rodadas = [(6, 5), (9, 7)]   # (valor de dia, índice do case escolhido)
    duracao = 70
    rodada = min(1, int(q // duracao))
    q0 = rodada * duracao
    dia, escolhido = rodadas[rodada]
    passo = 6

    codigo(ax, 0.8, 7.2, f"dia = {dia}", tamanho=15)
    codigo(ax, 0.8, 6.55, "match dia:", tamanho=15)

    # qual case está sendo comparado agora
    t = (q - q0 - 8) / passo
    atual = max(0, min(escolhido, int(t))) if q >= q0 + 8 else -1
    achou = q >= q0 + 8 + escolhido * passo + passo

    for k, ((valor, resultado), x) in enumerate(zip(casos, x_casos)):
        if achou and k == escolhido:
            fc, ec = "#DCFCE7", VERDE
        elif k < atual or (achou and k < escolhido):
            fc, ec = "#F3F4F6", BORDA
        elif k == atual:
            fc, ec = DESTAQUE, LARANJA
        else:
            fc, ec = CAIXA, BORDA
        retangulo(ax, x - 0.85, y_casos - 0.85, 1.7, 1.7, fc=fc, ec=ec, lw=2.2)
        texto(ax, x, y_casos + 0.35, f"case {valor}", tamanho=11.5, mono=True, ha="center", negrito=True)
        texto(ax, x, y_casos - 0.3, resultado, tamanho=9 if "\n" in resultado else 11, ha="center",
              cor=SUAVE)
        if (k < atual or (achou and k < escolhido)) and q >= q0 + 8:
            texto(ax, x, y_casos + 1.15, "✗", tamanho=14, cor=VERMELHO, ha="center")

    # o valor de dia "visitando" cada case
    if q >= q0 + 4:
        x_token = x_casos[max(0, atual)] if atual >= 0 else 4.5
        bloco(ax, x_token, 6.0 if not achou else 5.6, str(dia), CORES["int"], w=1.0, h=0.8, tamanho=16)

    painel(ax, 5.5, 1.1, 5.0, 1.3, "Terminal", escuro=True)
    if achou:
        saida_terminal(ax, 5.8, 1.6, casos[escolhido][1].replace("\n", " "), tamanho=14,
                       alpha=progresso(q, q0 + 8 + (escolhido + 1) * passo, q0 + 12 + (escolhido + 1) * passo))

    if rodada == 1:
        legenda(ax, "case _ pega qualquer outro valor (é o \"senão\" do match)",
              alpha=progresso(q, duracao + 60, duracao + 66))


ANIMACOES = {
    "match_casos": (match_casos, 150),
}
