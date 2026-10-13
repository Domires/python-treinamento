"""Animações da aula 02 - operações matemáticas."""

from base import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# Operadores: uma "tabela" que vai sendo preenchida
# -----------------------------------------------------------------------------
def operadores(ax, q):
    titulo(ax, "Operadores matemáticos")

    linhas = [
        ("+", "soma", "10 + 3", "13"),
        ("-", "subtração", "10 - 3", "7"),
        ("*", "multiplicação", "10 * 3", "30"),
        ("/", "divisão", "10 / 3", "3.333..."),
        ("**", "potência", "10 ** 3", "1000"),
        ("//", "divisão inteira", "10 // 3", "3"),
        ("%", "resto da divisão", "10 % 3", "1"),
    ]
    for k, (simbolo, nome, exemplo, resultado) in enumerate(linhas):
        y = 7.1 - k * 0.85
        q0 = 6 + k * 14
        aparece = progresso(q, q0, q0 + 5)
        ativo = janela(q, q0, q0 + 14, 3, 3) if k < len(linhas) - 1 else progresso(q, q0, q0 + 3)
        if ativo > 0:
            retangulo(ax, 0.7, y - 0.36, 13.6, 0.72, fc=DESTAQUE, ec="none", alpha=ativo, raio=0.1)
        texto(ax, 1.4, y, simbolo, tamanho=17, mono=True, negrito=True, cor=CORES["int"], alpha=aparece, ha="center")
        texto(ax, 2.6, y, nome, tamanho=13, alpha=aparece)
        codigo(ax, 7.3, y, exemplo, alpha=aparece, tamanho=15)
        texto(ax, 9.9, y, "→", tamanho=15, cor=SUAVE, alpha=progresso(q, q0 + 6, q0 + 9))
        codigo(ax, 10.8, y, resultado, alpha=progresso(q, q0 + 6, q0 + 10), tamanho=15, cor=CORES["int"])

    legenda(ax, "// = quantas vezes cabe inteiro     % = o que sobra", progresso(q, 104, 112))


# -----------------------------------------------------------------------------
# Divisão inteira e resto: unidades indo para as caixas
# -----------------------------------------------------------------------------
def divisao_e_resto(ax, q):
    titulo(ax, "Divisão inteira (//) e resto (%)")
    texto(ax, 0.8, 7.3, "38 unidades, caixas com 12 unidades cada", tamanho=13, cor=SUAVE)

    total, por_caixa = 38, 12
    # posições iniciais: grade 10 x 4 à esquerda
    origem = [(1.0 + (i % 10) * 0.45, 5.9 - (i // 10) * 0.55) for i in range(total)]
    # caixas à direita
    x_caixas = [7.4, 10.3, 13.2]
    for c, xc in enumerate(x_caixas):
        cheia = progresso(q, 12 + (c * por_caixa + por_caixa - 1) * 1.3 + 8, 12 + (c * por_caixa + por_caixa - 1) * 1.3 + 12)
        retangulo(ax, xc - 1.2, 3.6, 2.4, 2.4, fc=CAIXA, ec=CORES["int"] if cheia > 0.5 else BORDA, lw=2.5)
        texto(ax, xc, 3.25, f"caixa {c + 1}", tamanho=11, cor=SUAVE, ha="center")

    xs, ys, cores = [], [], []
    for i in range(total):
        if i < len(x_caixas) * por_caixa:
            c, slot = i // por_caixa, i % por_caixa
            destino = (x_caixas[c] - 0.75 + (slot % 4) * 0.5, 5.45 - (slot // 4) * 0.6)
            p = progresso(q, 12 + i * 1.3, 12 + i * 1.3 + 8)
            xs.append(mix(origem[i][0], destino[0], p))
            ys.append(mix(origem[i][1], destino[1], p))
            cores.append(CORES["int"])
        else:
            xs.append(origem[i][0])
            ys.append(origem[i][1])
            cores.append(LARANJA if q > 70 else CORES["int"])
    ax.scatter(xs, ys, s=110, c=cores, zorder=3)

    fim = 12 + 35 * 1.3 + 12
    balao(ax, 4.6, 1.9, "38 // 12 = 3   (caixas cheias)", alpha=progresso(q, fim, fim + 8), tamanho=14)
    balao(ax, 11.6, 1.9, "38 % 12 = 2   (sobram)", alpha=progresso(q, fim + 10, fim + 18), tamanho=14,
          fc="#FFEDD5")


# -----------------------------------------------------------------------------
# Ordem das operações
# -----------------------------------------------------------------------------
def ordem_operacoes(ax, q):
    titulo(ax, "Ordem das operações")

    texto(ax, 0.8, 6.9, "sem parênteses", tamanho=12, cor=SUAVE)
    reducao(ax, 0.8, 6.0, [
        ("1 + 1 * 5", "1 * 5", "primeiro * e /"),
        ("1 + 5", "1 + 5", "depois + e -"),
        ("1 + 1 * 5  =  6", None, ""),
    ], q, 8, x_nota=7.0)

    texto(ax, 0.8, 4.2, "com parênteses", tamanho=12, cor=SUAVE, alpha=progresso(q, 72, 78))
    reducao(ax, 0.8, 3.3, [
        ("(1 + 1) * 5", "(1 + 1)", "parênteses primeiro"),
        ("2 * 5", "2 * 5", "depois *"),
        ("(1 + 1) * 5  =  10", None, ""),
    ], q, 76, x_nota=7.0)

    legenda(ax, "Ordem: ( )  →  **  →  * e /  →  + e -", progresso(q, 140, 148))


# -----------------------------------------------------------------------------
# Operadores de atribuição
# -----------------------------------------------------------------------------
def operadores_atribuicao(ax, q):
    titulo(ax, "Operadores de atribuição")

    linhas = ["total = 100", "total += 50", "total -= 20", "total *= 2"]
    contas = [None, "100 + 50 = 150", "150 - 20 = 130", "130 * 2 = 260"]
    valores = ["100", "150", "130", "260"]
    passo = 30
    for k, linha in enumerate(linhas):
        q0 = 8 + k * passo
        ativo = janela(q, q0, q0 + passo, 3, 3) if k < len(linhas) - 1 else progresso(q, q0, q0 + 3)
        codigo(ax, 1.2, 6.6 - k * 1.0, linha, destaque=ativo, alpha=0.3 + 0.7 * progresso(q, q0 - 4, q0))
        ponteiro(ax, 0.85, 6.6 - k * 1.0, alpha=ativo)

    atual = max(0, min(len(linhas) - 1, int((q - 8) // passo)))
    q0 = 8 + atual * passo
    if contas[atual]:
        balao(ax, 11.6, 6.6, contas[atual], alpha=progresso(q, q0 + 4, q0 + 10), tamanho=15)
    troca = progresso(q, q0 + 12, q0 + 18)
    valor = valores[atual] if (troca > 0.5 or atual == 0) else valores[atual - 1]
    caixa(ax, 11.6, 3.6, "total", valor if q >= 14 else None, cor=CORES["int"], w=3.4,
          destaque=janela(q, q0 + 12, q0 + 20, 2, 2) if atual else 0)

    legenda(ax, "total += 50  é o mesmo que  total = total + 50", progresso(q, 44, 52))


ANIMACOES = {
    "operadores": (operadores, 130),
    "divisao_e_resto": (divisao_e_resto, 125),
    "ordem_operacoes": (ordem_operacoes, 165),
    "operadores_atribuicao": (operadores_atribuicao, 145),
}
