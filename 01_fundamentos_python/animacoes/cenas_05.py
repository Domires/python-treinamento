"""Animações da aula 05 - entrada de dados (input)."""

from base import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# input(): pergunta, espera o usuário digitar e guarda na variável
# -----------------------------------------------------------------------------
def input_fluxo(ax, q):
    titulo(ax, "input(): o programa pergunta e espera a resposta")

    painel(ax, 0.5, 4.3, 8.0, 3.0, "aula.py")
    linhas = ['nome = input("Qual é o seu nome? ")', 'print(f"Olá, {nome}!")']
    destaque_codigo(ax, 0.9, [5.9, 5.0], linhas, q, [(0, 6, 64), (1, 66, 999)], tamanho=11.5)

    painel(ax, 9.0, 4.3, 6.5, 3.0, "Terminal", escuro=True)
    pergunta = "Qual é o seu nome? "
    resposta = "Ana"
    if q >= 12:
        saida_terminal(ax, 9.3, 5.9, pergunta + digitado(resposta, q, 30, 40))
        # cursor piscando enquanto espera
        if q < 44 and (q // 4) % 2 == 0:
            x_cursor = 9.3 + (len(pergunta) + len(digitado(resposta, q, 30, 40))) * LARGURA_CHAR * 12 / 15
            retangulo(ax, x_cursor, 5.7, 0.14, 0.4, fc=TERMINAL_TEXTO, ec="none", raio=0)
    texto(ax, 12.2, 3.9, "o programa fica PARADO esperando o Enter", tamanho=10.5, cor=SUAVE, ha="center",
          alpha=janela(q, 14, 40, 4, 4))
    balao(ax, 14.6, 5.1, "Enter ↵", alpha=janela(q, 40, 52, 2, 4), tamanho=11, mono=False)

    caixa(ax, 4.5, 2.0, "nome", '"Ana"' if q >= 62 else None, cor=CORES["str"], w=3.0, h=1.2,
          alpha=progresso(q, 44, 50))
    voo = progresso(q, 48, 62)
    if 0 < voo < 1:
        x0 = 9.3 + (len(pergunta) + 1.5) * LARGURA_CHAR * 12 / 15
        valor_solto(ax, mix(x0, 4.5, voo), mix(5.9, 2.0, voo), '"Ana"', cor=CORES["str"], tamanho=16)

    saida_terminal(ax, 9.3, 5.2, "Olá, Ana!", alpha=progresso(q, 74, 80))
    legenda(ax, "O que foi digitado é guardado na variável", progresso(q, 64, 70))


# -----------------------------------------------------------------------------
# input() sempre devolve TEXTO
# -----------------------------------------------------------------------------
def input_sempre_texto(ax, q):
    titulo(ax, "input() sempre devolve TEXTO")

    painel(ax, 0.5, 5.7, 7.2, 1.5, "Terminal", escuro=True)
    saida_terminal(ax, 0.8, 6.2, "Digite seu peso (kg): " + digitado("70", q, 6, 12))

    # o que o Python recebe
    texto(ax, 8.3, 6.4, "o Python recebe:", tamanho=12, cor=SUAVE, alpha=progresso(q, 16, 20))
    bloco(ax, 13.0, 6.4, '"70"', CORES["str"], w=1.9, alpha=progresso(q, 16, 22))
    etiqueta(ax, 14.6, 6.4, "str", CORES["str"], alpha=progresso(q, 18, 24))

    # tentativa de conta com texto
    codigo(ax, 0.8, 4.3, 'peso + 1', alpha=progresso(q, 32, 36), tamanho=16)
    texto(ax, 3.6, 4.3, "→", tamanho=16, cor=SUAVE, alpha=progresso(q, 36, 39))
    balao(ax, 8.2, 4.3, 'TypeError: texto + número não funciona', alpha=progresso(q, 38, 44), tamanho=12,
          fc="#FEE2E2", cor=VERMELHO, mono=False)

    # solução: converter
    codigo(ax, 0.8, 2.6, 'float(peso) + 1', alpha=progresso(q, 64, 68), tamanho=16)
    texto(ax, 5.3, 2.6, "→", tamanho=16, cor=SUAVE, alpha=progresso(q, 68, 71))
    bloco(ax, 7.0, 2.6, "70.0", CORES["float"], w=1.9, alpha=progresso(q, 70, 76))
    texto(ax, 8.3, 2.6, "+ 1  =", tamanho=16, mono=True, alpha=progresso(q, 76, 80))
    bloco(ax, 11.2, 2.6, "71.0", CORES["float"], w=1.9, alpha=progresso(q, 80, 86))
    etiqueta(ax, 12.9, 2.6, "float", CORES["float"], alpha=progresso(q, 80, 86))

    legenda(ax, "Para fazer contas, converta com int() ou float()", progresso(q, 88, 94))


ANIMACOES = {
    "input_fluxo": (input_fluxo, 115),
    "input_sempre_texto": (input_sempre_texto, 125),
}
