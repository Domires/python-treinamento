"""Animações da aula 15 - erros, try/except e debug."""

from base import *  # noqa: F401,F403

ERRO = "#F87171"


# -----------------------------------------------------------------------------
# Lendo o traceback de baixo para cima
# -----------------------------------------------------------------------------
def traceback_leitura(ax, q):
    titulo(ax, "Mensagem de erro: leia de BAIXO para CIMA")

    linhas = [
        ("Traceback (most recent call last):", TERMINAL_TEXTO),
        ('  File "C:\\...\\aula.py", line 7, in <module>', TERMINAL_TEXTO),
        ("    print(10 / quantidade)", TERMINAL_TEXTO),
        ("          ~~~^~~~~~~~~~~~", ERRO),
        ("ZeroDivisionError: division by zero", ERRO),
    ]
    painel(ax, 0.5, 2.6, 15.0, 4.6, "Terminal", escuro=True)
    ys = [6.3, 5.6, 4.95, 4.4, 3.4]
    for (conteudo, cor), y in zip(linhas, ys):
        texto(ax, 0.9, y, conteudo, tamanho=13, mono=True, cor=cor, alpha=progresso(q, 2, 8))

    # 1º: última linha
    retangulo(ax, 0.7, 3.05, 8.6, 0.7, fc="none", ec=LARANJA, lw=2.5, alpha=janela(q, 16, 999, 4, 1))
    etiqueta(ax, 11.7, 3.4, "1º  o TIPO e o MOTIVO", LARANJA, alpha=progresso(q, 18, 24), tamanho=11)
    # 2º: arquivo e linha
    retangulo(ax, 0.7, 4.65, 10.0, 1.25, fc="none", ec=CORES["int"], lw=2.5, alpha=progresso(q, 44, 50))
    etiqueta(ax, 13.1, 5.3, "2º  ONDE (arquivo e linha)", CORES["int"], alpha=progresso(q, 46, 52), tamanho=11)
    seta(ax, 14.3, 3.75, 14.3, 4.95, cor=SUAVE, alpha=progresso(q, 34, 40))

    texto(ax, 0.8, 1.7, "ZeroDivisionError = divisão por zero  →  a variável quantidade vale 0 na linha 7",
          tamanho=12.5, alpha=progresso(q, 66, 72))
    legenda(ax, "Copie a última linha no Google: quase sempre alguém já resolveu", progresso(q, 84, 90))


# -----------------------------------------------------------------------------
# try / except / else / finally
# -----------------------------------------------------------------------------
def try_except(ax, q):
    titulo(ax, "try / except: tratando o erro sem parar o programa")

    linhas = ["try:", "    numero = int(valor)", "except ValueError:", '    print("Valor inválido")',
              "else:", '    print("Conversão ok")', "finally:", '    print("Fim da tentativa")']
    ys = [6.9 - k * 0.66 for k in range(len(linhas))]

    rodadas = [('valor = "abc"', [(0, 4, 9), (1, 9, 20), (2, 22, 28), (3, 28, 36), (6, 38, 43), (7, 43, 52)],
                ["Valor inválido", "Fim da tentativa"], (1, 16)),
               ('valor = "25"', [(0, 4, 9), (1, 9, 18), (4, 20, 25), (5, 25, 33), (6, 35, 40), (7, 40, 50)],
                ["Conversão ok", "Fim da tentativa"], None)]
    duracao = 64
    rodada = min(1, int(q // duracao))
    q0 = rodada * duracao
    atribuicao, tempos, saidas, erro_em = rodadas[rodada]

    codigo(ax, 0.8, 7.55, atribuicao, tamanho=14, cor=CORES["str"])
    destaque_codigo(ax, 1.3, ys, linhas, q - q0, tempos, tamanho=13)

    if erro_em:
        linha_erro, quadro = erro_em
        balao(ax, 9.2, ys[linha_erro], "ValueError!", alpha=janela(q - q0, quadro, 22, 2, 3), tamanho=13,
              fc="#FEE2E2", cor=VERMELHO, mono=False)
        seta(ax, 7.5, ys[linha_erro] - 0.1, 6.0, ys[2] + 0.1, cor=VERMELHO, curva=-0.4, alpha=janela(q - q0, 19, 26, 2, 3))
        texto(ax, 8.4, (ys[2] + ys[3]) / 2, "pula direto para o except", tamanho=11, cor=VERMELHO,
              alpha=janela(q - q0, 19, 34, 2, 3))

    painel(ax, 9.6, 1.0, 5.9, 2.4, "Terminal", escuro=True)
    for k, saida in enumerate(saidas):
        saida_terminal(ax, 9.9, 2.5 - k * 0.6, saida, tamanho=12,
                       alpha=progresso(q - q0, tempos[3 + k * 2][1] + 2, tempos[3 + k * 2][1] + 5))

    texto(ax, 9.6, 4.6, "except: só se der erro\nelse: só se NÃO der erro\nfinally: SEMPRE", tamanho=11,
          cor=SUAVE, alpha=progresso(q, duracao + 52, duracao + 58))


# -----------------------------------------------------------------------------
# Debugger: breakpoint e execução passo a passo
# -----------------------------------------------------------------------------
def debug_breakpoint(ax, q):
    titulo(ax, "Debug: pausando o programa para ver as variáveis")

    linhas = ["def media_acima_da_meta(vendas, meta):", "    soma = 0", "    quantidade = 0", "    for venda in vendas:",
              "        if venda > meta:", "            soma += venda", "        quantidade += 1",
              "    return soma / quantidade"]
    ys = [6.75 - k * 0.6 for k in range(len(linhas))]
    painel(ax, 0.5, 1.75, 9.0, 5.75, "aula.py")

    # breakpoint na linha "quantidade += 1"
    ax.scatter([0.85], [ys[6]], s=110, color=VERMELHO, zorder=4, alpha=progresso(q, 4, 8))
    texto(ax, 0.8, 1.25, "clique à esquerda do nº da linha = breakpoint (bolinha vermelha)", tamanho=10.5, cor=SUAVE,
          alpha=progresso(q, 4, 10))

    # execução: o programa pausa na linha 6 a cada volta (F5 continua)
    vendas = [500, 1000, 300, 1400]
    passo = 22
    volta = max(-1, min(3, int((q - 16) // passo)))
    soma = 0
    quantidade = 0
    for v in vendas[:max(0, volta)]:
        if v > 800:
            soma += v
        quantidade += 1
    if volta >= 0 and vendas[volta] > 800:
        soma += vendas[volta]

    for k, (y, linha) in enumerate(zip(ys, linhas)):
        pausado = volta >= 0 and k == 6
        codigo(ax, 1.3, y, linha, tamanho=11.5, destaque=1 if pausado else 0)
        if pausado:
            ponteiro(ax, 1.1, y, tamanho=12)

    # painel de variáveis
    painel(ax, 10.0, 1.75, 5.5, 5.75, "VARIABLES")
    if volta >= 0:
        variaveis = [("vendas", "[500, 1000...]"), ("meta", "800"), ("venda", str(vendas[volta])),
                     ("soma", str(soma)), ("quantidade", str(quantidade))]
        for k, (nome, valor) in enumerate(variaveis):
            y = 6.6 - k * 0.65
            mudou = nome in ("venda", "soma", "quantidade")
            texto(ax, 10.3, y, f"{nome}:", tamanho=11.5, mono=True, cor=SUAVE)
            texto(ax, 12.7, y, valor, tamanho=11.5, mono=True, cor=LARANJA if mudou else TINTA, negrito=mudou)
        texto(ax, 10.3, 3.2, f"pausa {volta + 1}  (F5 continua)", tamanho=10.5, cor=SUAVE)

    texto(ax, 10.3, 2.4, "quantidade conta TODAS\nas vendas, não só as\nacima da meta!", tamanho=11, cor=VERMELHO,
          negrito=True, alpha=progresso(q, 16 + 3 * passo + 8, 16 + 3 * passo + 14))


ANIMACOES = {
    "traceback_leitura": (traceback_leitura, 110),
    "try_except": (try_except, 140),
    "debug_breakpoint": (debug_breakpoint, 125),
}
