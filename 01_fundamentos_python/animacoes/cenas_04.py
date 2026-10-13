"""Animações da aula 04 - booleanos."""

from base import *  # noqa: F401,F403


def badge_bool(ax, x, y, valor, alpha=1.0, tamanho=13):
    etiqueta(ax, x, y, "True" if valor else "False", VERDE if valor else VERMELHO, alpha=alpha, tamanho=tamanho)


# -----------------------------------------------------------------------------
# Comparações viram True ou False
# -----------------------------------------------------------------------------
def comparacoes(ax, q):
    titulo(ax, "Comparações sempre resultam em True ou False")

    itens = [
        ("10 > 9", True), ("10 == 9", False), ("10 < 9", False),
        ("10 != 9", True), ('"SP" == "SP"', True), ('"SP" == "sp"', False),
    ]
    for k, (expressao, resultado) in enumerate(itens):
        coluna, linha = k // 3, k % 3
        x = 1.2 + coluna * 7.6
        y = 6.4 - linha * 1.5
        q0 = 6 + k * 15
        codigo(ax, x, y, expressao, alpha=progresso(q, q0, q0 + 5), tamanho=17)
        texto(ax, x + 3.9, y, "→", tamanho=16, cor=SUAVE, alpha=progresso(q, q0 + 6, q0 + 9))
        badge_bool(ax, x + 5.3, y, resultado, alpha=progresso(q, q0 + 7, q0 + 11), tamanho=14)

    legenda(ax, "Atenção:  ==  compara    ·    =  guarda um valor na variável", progresso(q, 100, 108))


# -----------------------------------------------------------------------------
# and / or / not: tabela-verdade sendo preenchida
# -----------------------------------------------------------------------------
def and_or_not(ax, q):
    titulo(ax, "Operadores lógicos: and, or, not")

    colunas = [("A", 1.6), ("B", 3.9), ("A and B", 6.7), ("A or B", 9.8)]
    for nome, x in colunas:
        texto(ax, x, 7.1, nome, tamanho=14, mono=True, negrito=True, ha="center", alpha=progresso(q, 0, 6))
    ax.plot([0.6, 11.2], [6.65, 6.65], color=BORDA, lw=1.5)

    linhas = [(True, True), (True, False), (False, True), (False, False)]
    for k, (a, b) in enumerate(linhas):
        y = 6.0 - k * 0.95
        q0 = 8 + k * 18
        badge_bool(ax, 1.6, y, a, alpha=progresso(q, q0, q0 + 4))
        badge_bool(ax, 3.9, y, b, alpha=progresso(q, q0, q0 + 4))
        badge_bool(ax, 6.7, y, a and b, alpha=progresso(q, q0 + 6, q0 + 10))
        badge_bool(ax, 9.8, y, a or b, alpha=progresso(q, q0 + 11, q0 + 15))

    texto(ax, 11.8, 6.0, "and: as DUAS\nprecisam ser True", tamanho=10.5, cor=SUAVE, alpha=progresso(q, 30, 36))
    texto(ax, 11.8, 4.4, "or: basta\nUMA ser True", tamanho=10.5, cor=SUAVE, alpha=progresso(q, 40, 46))

    q0 = 90
    codigo(ax, 1.5, 1.6, "not True", alpha=progresso(q, q0, q0 + 5), tamanho=16)
    badge_bool(ax, 5.0, 1.6, False, alpha=progresso(q, q0 + 6, q0 + 10))
    codigo(ax, 8.5, 1.6, "not False", alpha=progresso(q, q0 + 10, q0 + 15), tamanho=16)
    badge_bool(ax, 12.2, 1.6, True, alpha=progresso(q, q0 + 16, q0 + 20))
    texto(ax, 8.0, 0.55, "not inverte o resultado", tamanho=12, cor=SUAVE, ha="center", alpha=progresso(q, q0 + 20, q0 + 26))


# -----------------------------------------------------------------------------
# bool(): quais valores são True e quais são False
# -----------------------------------------------------------------------------
def verdadeiro_falso(ax, q):
    titulo(ax, "bool(): valores verdadeiros e falsos")

    valores = [('"Olá"', True), ("0", False), ("1", True), ('""', False),
               ("[1, 2, 3]", True), ("[]", False), ("None", False), ("{}", False)]

    # duas "caixas" abertas em cima
    for x, nome, cor in [(4.0, "True", VERDE), (12.0, "False", VERMELHO)]:
        ax.plot([x - 2.6, x - 2.6, x + 2.6, x + 2.6], [5.4, 1.6, 1.6, 5.4], color=cor, lw=3)
        etiqueta(ax, x, 1.15, nome, cor, tamanho=13)

    contagem = {True: 0, False: 0}
    for k, (valor, resultado) in enumerate(valores):
        q0 = 8 + k * 14
        x_destino = 4.0 if resultado else 12.0
        indice = contagem[resultado]
        contagem[resultado] += 1
        y_destino = 2.1 + indice * 0.72
        # aparece em cima, mostra bool(valor) e cai na caixa certa
        aparece = progresso(q, q0, q0 + 4)
        cai = progresso(q, q0 + 6, q0 + 13)
        if aparece > 0:
            x = mix(8.0, x_destino, cai)
            y = mix(6.6, y_destino, cai)
            if cai < 1:
                codigo(ax, 5.6, 7.3, f"bool({valor})", tamanho=15, alpha=aparece * (1 - cai))
            bloco(ax, x, y, valor, CORES["bool"], w=2.4, h=0.62, tamanho=13, alpha=aparece)

    legenda(ax, "False: 0, None, texto vazio e coleções vazias. Quase todo o resto é True",
            progresso(q, 125, 132))


ANIMACOES = {
    "comparacoes": (comparacoes, 125),
    "and_or_not": (and_or_not, 135),
    "verdadeiro_falso": (verdadeiro_falso, 150),
}
