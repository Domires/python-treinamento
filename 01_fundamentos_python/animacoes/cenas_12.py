"""Animações da aula 12 - funções."""

from base import *  # noqa: F401,F403

COR_FUNC = CORES["func"]


# -----------------------------------------------------------------------------
# Função como uma "máquina": entra argumento, sai o retorno
# -----------------------------------------------------------------------------
def funcao_maquina(ax, q):
    titulo(ax, "Função: escreve uma vez, usa quantas vezes quiser")

    codigo(ax, 0.8, 7.25, "def fahrenheit_para_celsius(fahrenheit):", tamanho=12.5)
    codigo(ax, 0.8, 6.7, "    return (fahrenheit - 32) * 5 / 9", tamanho=12.5)

    # máquina
    retangulo(ax, 5.4, 2.7, 5.2, 2.6, fc="#EEF2FF", ec=COR_FUNC, lw=3)
    texto(ax, 8.0, 4.95, "fahrenheit_para_celsius", tamanho=11.5, mono=True, ha="center", negrito=True, cor=COR_FUNC)

    chamadas = [("77", "25.0"), ("95", "35.0")]
    passo = 52
    rodada = min(1, int(q // passo))
    q0 = 6 + rodada * passo
    argumento, resultado = chamadas[rodada]

    codigo(ax, 0.8, 1.3, f"retorno = fahrenheit_para_celsius({argumento})", tamanho=13,
           alpha=progresso(q, q0, q0 + 5))

    entra = progresso(q, q0 + 6, q0 + 16)
    if entra < 1:
        valor_solto(ax, mix(2.6, 5.4, entra), mix(3.9, 3.9, entra), argumento, cor=CORES["int"], alpha=progresso(q, q0, q0 + 5))
    else:
        texto(ax, 8.0, 4.1, f"parâmetro: fahrenheit = {argumento}", tamanho=11, mono=True, ha="center",
              alpha=1 - progresso(q, q0 + 30, q0 + 34))
        texto(ax, 8.0, 3.4, f"({argumento} - 32) * 5 / 9", tamanho=12.5, mono=True, ha="center",
              alpha=progresso(q, q0 + 18, q0 + 22) * (1 - progresso(q, q0 + 30, q0 + 34)))
    sai = progresso(q, q0 + 32, q0 + 42)
    if 0 < sai < 1:
        valor_solto(ax, mix(10.6, 13.3, sai), mix(3.9, 3.9, sai), resultado, cor=CORES["float"])
    texto(ax, 4.5, 4.4, "entra", tamanho=10.5, cor=SUAVE, ha="center")
    texto(ax, 11.6, 4.4, "return", tamanho=10.5, cor=SUAVE, ha="center")
    seta(ax, 4.0, 3.9, 5.3, 3.9, cor=BORDA)
    seta(ax, 10.7, 3.9, 12.0, 3.9, cor=BORDA)
    caixa(ax, 13.6, 3.9, "retorno", resultado if sai >= 1 else None, cor=CORES["float"], w=2.6, h=1.1,
          tamanho_valor=16)


# -----------------------------------------------------------------------------
# print x return
# -----------------------------------------------------------------------------
def print_vs_return(ax, q):
    titulo(ax, "print() só MOSTRA · return DEVOLVE o valor")

    # lado esquerdo: print
    texto(ax, 4.0, 7.3, "com print", tamanho=13, negrito=True, ha="center", cor=SUAVE)
    codigo(ax, 0.6, 6.6, "def converter(f):", tamanho=11.5)
    codigo(ax, 0.6, 6.1, "    print((f - 32) * 5 / 9)", tamanho=11.5)
    codigo(ax, 0.6, 5.3, "retorno = converter(77)", tamanho=11.5, alpha=progresso(q, 6, 10))
    painel(ax, 0.6, 3.1, 6.8, 1.5, "Terminal", escuro=True)
    voo = progresso(q, 14, 26)
    if 0 < voo < 1:
        valor_solto(ax, mix(4.0, 2.0, voo), mix(6.1, 3.65, voo), "25.0", cor=CORES["float"], tamanho=15)
    saida_terminal(ax, 0.9, 3.65, "25.0", alpha=progresso(q, 25, 28), tamanho=14)
    caixa(ax, 4.0, 1.5, "retorno", "None" if q >= 32 else None, cor=CORES["none"], w=2.8, h=1.0, tamanho_valor=15)
    texto(ax, 4.0, 0.55, "a variável fica VAZIA (None)", tamanho=11, cor=VERMELHO, ha="center", alpha=progresso(q, 34, 40))

    # divisória
    ax.plot([8.0, 8.0], [0.6, 7.5], color=BORDA, lw=1.5)

    # lado direito: return
    b = 50
    texto(ax, 12.0, 7.3, "com return", tamanho=13, negrito=True, ha="center", cor=SUAVE, alpha=progresso(q, b - 4, b))
    codigo(ax, 8.6, 6.6, "def converter(f):", tamanho=11.5, alpha=progresso(q, b - 4, b))
    codigo(ax, 8.6, 6.1, "    return (f - 32) * 5 / 9", tamanho=11.5, alpha=progresso(q, b - 4, b))
    codigo(ax, 8.6, 5.3, "retorno = converter(77)", tamanho=11.5, alpha=progresso(q, b + 4, b + 8))
    voo = progresso(q, b + 12, b + 24)
    if 0 < voo < 1:
        valor_solto(ax, mix(12.5, 12.0, voo), mix(6.1, 2.9, voo), "25.0", cor=CORES["float"], tamanho=15)
    caixa(ax, 12.0, 2.9, "retorno", "25.0" if voo >= 1 else None, cor=CORES["float"], w=2.8, h=1.0,
          tamanho_valor=15, alpha=progresso(q, b, b + 4))
    codigo(ax, 9.4, 1.4, "retorno + 10  →  35.0", tamanho=13, alpha=progresso(q, b + 30, b + 35))
    texto(ax, 12.0, 0.55, "o valor pode ser usado depois", tamanho=11, cor=VERDE, ha="center",
          alpha=progresso(q, b + 34, b + 40))


# -----------------------------------------------------------------------------
# Escopo: variável local x global
# -----------------------------------------------------------------------------
def escopo(ax, q):
    titulo(ax, "Escopo: variáveis locais e globais")

    # área global
    retangulo(ax, 0.5, 0.9, 15.0, 6.6, fc="#F8FAFC", ec=BORDA, lw=2)
    texto(ax, 0.8, 7.15, "fora das funções (GLOBAL)", tamanho=11, cor=SUAVE)
    codigo(ax, 0.9, 6.5, 'nome = "Alex"', tamanho=13)

    valor_global = '"Alex"'
    if q >= 98:
        valor_global = '"Ana"'
    caixa(ax, 3.0, 4.6, "nome", valor_global, cor=CORES["str"], w=2.8, h=1.1, tamanho_valor=15,
          destaque=janela(q, 96, 108, 2, 2))

    # função 1: variável local
    abre_1 = progresso(q, 10, 16) * (1 - progresso(q, 44, 50))
    retangulo(ax, 6.0, 3.3, 4.4, 3.1, fc="#EEF2FF", ec=CORES["func"], lw=2.5, alpha=max(0.25, abre_1))
    texto(ax, 6.2, 6.1, "minha_funcao()", tamanho=10.5, cor=CORES["func"], negrito=True, alpha=max(0.25, abre_1))
    codigo(ax, 6.3, 5.5, 'nome = "João"', tamanho=11.5, alpha=max(0.25, abre_1))
    caixa(ax, 8.2, 4.1, "nome", '"João"', cor=CORES["str"], w=2.6, h=0.9, tamanho_valor=14,
          alpha=progresso(q, 18, 24) * (1 - progresso(q, 44, 50)))
    texto(ax, 8.2, 2.9, "só existe aqui dentro", tamanho=10, cor=SUAVE, ha="center",
          alpha=progresso(q, 24, 30) * (1 - progresso(q, 44, 50)))
    texto(ax, 8.2, 2.9, "função terminou: a local some", tamanho=10, cor=VERMELHO, ha="center",
          alpha=janela(q, 50, 70, 3, 3))

    # função 2: global
    abre_2 = progresso(q, 76, 82)
    retangulo(ax, 11.0, 3.3, 4.2, 3.1, fc="#EEF2FF", ec=CORES["func"], lw=2.5, alpha=max(0.25, abre_2))
    texto(ax, 11.2, 6.1, "outra_funcao()", tamanho=10.5, cor=CORES["func"], negrito=True, alpha=max(0.25, abre_2))
    codigo(ax, 11.3, 5.5, "global nome", tamanho=11.5, alpha=max(0.25, abre_2))
    codigo(ax, 11.3, 4.9, 'nome = "Ana"', tamanho=11.5, alpha=max(0.25, abre_2))
    seta(ax, 11.2, 4.6, 4.5, 4.6, cor=LARANJA, alpha=progresso(q, 86, 92), curva=0.25, lw=2.5)
    texto(ax, 7.6, 3.0 + 0.0, "global: altera a variável de FORA", tamanho=10.5, cor=LARANJA, ha="center",
          alpha=progresso(q, 92, 98))

    painel(ax, 0.9, 1.15, 4.2, 1.4, "print(nome)", escuro=True)
    saida_terminal(ax, 1.2, 1.6, valor_global.strip('"'), tamanho=13, alpha=progresso(q, 54, 58))


# -----------------------------------------------------------------------------
# Recursão: fatorial
# -----------------------------------------------------------------------------
def recursao(ax, q):
    titulo(ax, "Recursão: a função chama a si mesma")
    codigo(ax, 0.8, 7.25, "def fatorial(n):", tamanho=12)
    codigo(ax, 0.8, 6.75, "    if n <= 1: return 1", tamanho=12)
    codigo(ax, 0.8, 6.25, "    return n * fatorial(n - 1)", tamanho=12)

    n_max = 4
    descida = 12      # quadros por chamada
    inicio_volta = 6 + n_max * descida + 8
    subida = 14
    resultados = {1: 1, 2: 2, 3: 6, 4: 24}

    for k, n in enumerate(range(n_max, 0, -1)):
        y = 5.2 - k * 1.05
        x = 6.0 + k * 0.6
        aparece = progresso(q, 6 + k * descida, 6 + k * descida + 6)
        indice_volta = n - 1          # n=1 volta primeiro
        q_volta = inicio_volta + indice_volta * subida
        resolvido = q >= q_volta + 6
        cor = VERDE if resolvido else CORES["func"]
        retangulo(ax, x, y - 0.42, 7.0, 0.84, fc="#DCFCE7" if resolvido else "#EEF2FF", ec=cor, lw=2, alpha=aparece)
        texto(ax, x + 0.2, y, f"fatorial({n})", tamanho=13, mono=True, negrito=True, cor=cor, alpha=aparece)
        if n == 1:
            explicacao = "n <= 1  →  1"
        else:
            explicacao = f"{n} * fatorial({n - 1})" if not resolvido else f"{n} * {resultados[n - 1]} = {resultados[n]}"
        texto(ax, x + 2.7, y, explicacao, tamanho=12.5, mono=True, alpha=aparece)

    texto(ax, 4.6, 3.6, "chamando", tamanho=10.5, cor=CORES["func"], ha="right",
          alpha=progresso(q, 10, 16))
    seta(ax, 5.3, 5.1, 5.3, 2.2, cor=CORES["func"], alpha=progresso(q, 10, 16))
    texto(ax, 15.3, 5.55, "volta", tamanho=10.5, cor=VERDE, ha="center",
          alpha=progresso(q, inicio_volta, inicio_volta + 6))
    seta(ax, 15.3, 2.2, 15.3, 5.1, cor=VERDE, alpha=progresso(q, inicio_volta, inicio_volta + 6))

    fim = inicio_volta + n_max * subida
    balao(ax, 8.0, 1.0, "fatorial(4) = 4 × 3 × 2 × 1 = 24", alpha=progresso(q, fim, fim + 6), tamanho=14)


ANIMACOES = {
    "funcao_maquina": (funcao_maquina, 120),
    "print_vs_return": (print_vs_return, 110),
    "escopo": (escopo, 130),
    "recursao": (recursao, 145),
}
