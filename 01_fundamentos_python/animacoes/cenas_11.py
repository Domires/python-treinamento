"""Animações da aula 11 - while."""

from base import *  # noqa: F401,F403


def badge_bool(ax, x, y, valor, alpha=1.0, tamanho=12):
    etiqueta(ax, x, y, "True" if valor else "False", VERDE if valor else VERMELHO, alpha=alpha, tamanho=tamanho)


# -----------------------------------------------------------------------------
# while: repete enquanto a condição for True
# -----------------------------------------------------------------------------
def while_loop(ax, q):
    titulo(ax, "while: repete ENQUANTO a condição for True")

    painel(ax, 0.5, 3.5, 7.4, 3.9, "aula.py")
    ys = [6.45, 5.7, 4.95, 4.2]
    linhas = ["i = 1", "while i < 6:", "    print(i)", "    i += 1"]

    passo = 18
    q_inicio = 8
    voltas = 5
    tempos = [(0, 2, 7)]
    for v in range(voltas):
        q0 = q_inicio + v * passo
        tempos += [(1, q0, q0 + 6), (2, q0 + 6, q0 + 11), (3, q0 + 11, q0 + 17)]
    q_saida = q_inicio + voltas * passo
    tempos.append((1, q_saida, q_saida + 14))
    destaque_codigo(ax, 1.2, ys, linhas, q, tempos, tamanho=15)

    # seta de "volta"
    seta(ax, 5.4, 4.2, 5.4, 5.7, curva=-0.8, cor=LARANJA, alpha=0.8 if q_inicio <= q < q_saida else 0.25, lw=2.2)
    texto(ax, 6.3, 5.0, "volta", tamanho=10.5, cor=LARANJA, alpha=0.8 if q_inicio <= q < q_saida else 0.25)

    volta = int((q - q_inicio) // passo)
    if q < q_inicio:
        i = 1
    elif q >= q_saida:
        i = 6
    else:
        i = volta + 1 + (1 if q >= q_inicio + volta * passo + 13 else 0)
    caixa(ax, 4.0, 1.8, "i", str(i) if q >= 4 else None, cor=CORES["int"], w=2.2, h=1.1)

    # condição avaliada
    if q_inicio <= q < q_saida:
        q0 = q_inicio + volta * passo
        badge_bool(ax, 6.2, 5.7, True, alpha=janela(q, q0 + 1, q0 + 7, 1, 1))
        balao(ax, 10.4, 1.8, f"{volta + 1} < 6 ?", alpha=janela(q, q0, q0 + 7, 1, 1), tamanho=13)
    if q >= q_saida:
        badge_bool(ax, 6.2, 5.7, False, alpha=progresso(q, q_saida + 2, q_saida + 5))
        balao(ax, 10.4, 1.8, "6 < 6 ?  False → sai do while", alpha=progresso(q, q_saida + 2, q_saida + 6), tamanho=13)

    painel(ax, 8.6, 3.5, 6.9, 3.9, "Terminal", escuro=True)
    for v in range(voltas):
        saida_terminal(ax, 8.9, 6.6 - v * 0.55, str(v + 1), alpha=progresso(q, q_inicio + v * passo + 8, q_inicio + v * passo + 11),
                       tamanho=13)

    legenda(ax, "Se a condição nunca ficar False, o loop não termina (Ctrl + C para parar)",
            progresso(q, q_saida + 16, q_saida + 22))


# -----------------------------------------------------------------------------
# while True + break: menu até digitar "sair"
# -----------------------------------------------------------------------------
def while_true_break(ax, q):
    titulo(ax, "while True + break: repete até pedir para sair")

    painel(ax, 0.5, 2.6, 7.6, 4.8, "aula.py")
    linhas = ["while True:", "    entrada = input(...)", '    if entrada == "sair":', "        break",
              "    total += float(entrada)"]
    ys = [6.5, 5.8, 5.1, 4.4, 3.7]

    entradas = ["10", "20.5", "sair"]
    passo = 30
    tempos = []
    for k, entrada in enumerate(entradas):
        q0 = 6 + k * passo
        tempos += [(0, q0, q0 + 4), (1, q0 + 4, q0 + 13), (2, q0 + 13, q0 + 19)]
        if entrada == "sair":
            tempos.append((3, q0 + 19, q0 + 40))
        else:
            tempos.append((4, q0 + 19, q0 + 28))
    destaque_codigo(ax, 1.0, ys, linhas, q, tempos, tamanho=13)

    painel(ax, 8.6, 2.6, 6.9, 4.8, "Terminal", escuro=True)
    total = 0.0
    for k, entrada in enumerate(entradas):
        q0 = 6 + k * passo
        if q >= q0 + 4:
            saida_terminal(ax, 8.9, 6.7 - k * 0.7, "Digite um valor: " + digitado(entrada, q, q0 + 6, q0 + 11), tamanho=12)
        if entrada != "sair" and q >= q0 + 24:
            total += float(entrada)

    fim = 6 + 2 * passo + 22
    seta(ax, 0.75, 4.25, 0.75, 1.9, cor=LARANJA, alpha=progresso(q, fim - 2, fim + 2), lw=2.5)
    texto(ax, 4.3, 1.3, "← break: sai do loop", tamanho=11, cor=LARANJA, alpha=progresso(q, fim - 2, fim + 2))
    saida_terminal(ax, 8.9, 6.7 - 3 * 0.7, f"Total: R$ {total:.2f}", alpha=progresso(q, fim + 4, fim + 8), tamanho=12)

    caixa(ax, 2.6, 1.3, "total", f"{total:.1f}", cor=CORES["float"], w=2.6, h=1.0, tamanho_valor=15)


ANIMACOES = {
    "while_loop": (while_loop, 145),
    "while_true_break": (while_true_break, 125),
}
