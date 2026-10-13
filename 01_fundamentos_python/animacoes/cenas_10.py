"""Animações da aula 10 - for."""

from base import *  # noqa: F401,F403

COR_LISTA = CORES["list"]


# -----------------------------------------------------------------------------
# for percorrendo uma lista
# -----------------------------------------------------------------------------
def for_lista(ax, q):
    titulo(ax, "for: repete para CADA item da lista")

    vendedores = ["Ana", "Bruno", "Carlos"]
    x_itens = [9.6, 11.6, 13.6]
    y_lista = 6.9
    texto(ax, 8.5, y_lista, "vendedores =", tamanho=11, mono=True, cor=SUAVE, ha="right")
    for x, nome in zip(x_itens, vendedores):
        bloco(ax, x, y_lista, f'"{nome}"', COR_LISTA, w=1.85, h=0.85, tamanho=12.5)

    painel(ax, 0.5, 3.6, 7.6, 2.6, "aula.py")
    linhas = ["for vendedor in vendedores:", '    print(f"Enviando para {vendedor}")', 'print("Fim!")']
    passo = 28
    tempos = []
    for k in range(3):
        q0 = 6 + k * passo
        tempos += [(0, q0, q0 + 10), (1, q0 + 12, q0 + passo - 2)]
    tempos.append((2, 6 + 3 * passo + 2, 999))
    destaque_codigo(ax, 0.95, [5.5, 4.75, 4.0], linhas, q, tempos, tamanho=10.5)

    atual = int((q - 6) // passo)
    if 0 <= atual < 3:
        q0 = 6 + atual * passo
        # ponteiro em cima do item atual
        texto(ax, x_itens[atual], y_lista + 0.75, "▼", tamanho=14, cor=LARANJA, ha="center")
        voo = progresso(q, q0 + 2, q0 + 10)
        if voo < 1:
            valor_solto(ax, mix(x_itens[atual], 4.3, voo), mix(y_lista, 1.9, voo), f'"{vendedores[atual]}"',
                        cor=CORES["str"], tamanho=15)
    valor_atual = None
    if q >= 16:
        valor_atual = f'"{vendedores[min(2, max(0, int((q - 16) // passo)))]}"'
    caixa(ax, 4.3, 1.9, "vendedor", valor_atual, cor=CORES["str"], w=3.0, h=1.0, tamanho_valor=15)
    texto(ax, 4.3, 0.95, f"volta {min(3, max(1, atual + 1))} de 3", tamanho=11, cor=SUAVE, ha="center",
          alpha=1 if 0 <= atual < 3 else 0)

    painel(ax, 8.6, 1.0, 6.9, 4.2, "Terminal", escuro=True)
    for k, nome in enumerate(vendedores):
        saida_terminal(ax, 8.9, 4.4 - k * 0.6, f"Enviando para {nome}",
                       alpha=progresso(q, 6 + k * passo + 14, 6 + k * passo + 18))
    saida_terminal(ax, 8.9, 4.4 - 3 * 0.6, "Fim!", alpha=progresso(q, 6 + 3 * passo + 4, 6 + 3 * passo + 8))


# -----------------------------------------------------------------------------
# Acumulando um total
# -----------------------------------------------------------------------------
def for_acumulador(ax, q):
    titulo(ax, "Acumulando um total com for")

    vendas = [10, 24, 122, 183, 18]
    x_itens = [3.6 + k * 2.2 for k in range(len(vendas))]
    codigo(ax, 0.8, 7.2, "total = 0", tamanho=14)
    codigo(ax, 0.8, 6.6, "for valor in vendas:", tamanho=14)
    codigo(ax, 0.8, 6.0, "    total += valor", tamanho=14)

    passo = 22
    total = 0
    totais = []
    for v in vendas:
        totais.append((total, total + v))
        total += v

    for k, (x, v) in enumerate(zip(x_itens, vendas)):
        q0 = 10 + k * passo
        usado = progresso(q, q0 + 4, q0 + 12)
        bloco(ax, x, 4.4, str(v), CORES["int"], w=1.7, h=0.95, tamanho=16, alpha=1 - 0.65 * (usado >= 1),
              destaque=janela(q, q0, q0 + 6, 2, 2))
        if 0 < usado < 1:
            valor_solto(ax, mix(x, 8.0, usado), mix(4.4, 1.9, usado), str(v), cor=CORES["int"], tamanho=16)

    atual = max(-1, min(len(vendas) - 1, int((q - 10) // passo)))
    if atual >= 0:
        antes, depois = totais[atual]
        q0 = 10 + atual * passo
        mostrar = depois if q >= q0 + 12 else antes
        balao(ax, 12.6, 1.9, f"{antes} + {vendas[atual]} = {depois}", alpha=progresso(q, q0 + 12, q0 + 16), tamanho=14)
    else:
        mostrar = 0
    caixa(ax, 8.0, 1.9, "total", str(mostrar), cor=CORES["int"], w=3.0, h=1.1)

    legenda(ax, "total = 357  (o mesmo que sum(vendas))", progresso(q, 10 + 5 * passo + 2, 10 + 5 * passo + 8))


# -----------------------------------------------------------------------------
# range()
# -----------------------------------------------------------------------------
def range_numeros(ax, q):
    titulo(ax, "range(): gera uma sequência de números")

    exemplos = [
        ("range(5)", list(range(5)), "começa em 0 e o 5 NÃO entra"),
        ("range(1, 6)", list(range(1, 6)), "de 1 até 6 (sem o 6)"),
        ("range(0, 10, 2)", list(range(0, 10, 2)), "de 2 em 2"),
    ]
    for k, (chamada, numeros, nota) in enumerate(exemplos):
        y = 6.5 - k * 2.0
        q0 = 4 + k * 32
        codigo(ax, 0.8, y, chamada, tamanho=16, alpha=progresso(q, q0, q0 + 5))
        for i, n in enumerate(numeros):
            bloco(ax, 6.0 + i * 1.3, y, str(n), CORES["int"], w=1.05, h=0.85, tamanho=15,
                  alpha=progresso(q, q0 + 6 + i * 3, q0 + 10 + i * 3))
        if k == 2:
            for i in range(len(numeros) - 1):
                seta(ax, 6.0 + i * 1.3, y + 0.5, 6.0 + (i + 1) * 1.3, y + 0.5, curva=-0.5, cor=LARANJA,
                     alpha=progresso(q, q0 + 22, q0 + 28), lw=1.5)
        texto(ax, 6.0, y - 0.75, nota, tamanho=11, cor=SUAVE, alpha=progresso(q, q0 + 20, q0 + 26))

    legenda(ax, "for mes in range(1, 13):  → repete 12 vezes (meses 1 a 12)", progresso(q, 104, 110))


# -----------------------------------------------------------------------------
# continue e break
# -----------------------------------------------------------------------------
def break_continue(ax, q):
    titulo(ax, "continue pula · break para")

    vendas = [10, 24, 122, 183, 18]

    def linha(y, q0, regra, comando, nota):
        codigo(ax, 0.8, y + 0.85, f"if venda {regra}: {comando}", tamanho=13, alpha=progresso(q, q0 - 6, q0))
        parou = False
        for i, v in enumerate(vendas):
            x = 2.0 + i * 2.2
            t = q0 + i * 9
            visitado = q >= t
            if comando == "continue":
                pula = v < 20
                estado = "pulado" if (visitado and pula) else ("ok" if visitado else "espera")
            else:
                if parou:
                    estado = "nunca"
                elif visitado and v >= 100:
                    estado = "parou"
                    parou = True
                else:
                    estado = "ok" if visitado else "espera"
            cor = {"ok": VERDE, "pulado": SUAVE, "parou": VERMELHO, "nunca": BORDA, "espera": CORES["int"]}[estado]
            if estado == "nunca" and q < t:
                cor = CORES["int"]
            bloco(ax, x, y, str(v), cor, w=1.7, h=0.9, tamanho=15, alpha=0.4 if estado in ("pulado", "nunca") and q >= t else 1)
            simbolo = {"ok": "✓", "pulado": "pulou", "parou": "break!"}.get(estado)
            if simbolo and q >= t + 3:
                texto(ax, x, y - 0.8, simbolo, tamanho=11, cor=cor, ha="center", negrito=True)
        texto(ax, 13.2, y, nota, tamanho=11.5, cor=SUAVE, alpha=progresso(q, q0 + 48, q0 + 54))

    linha(5.4, 10, "< 20", "continue", "vai para a\npróxima volta")
    linha(2.2, 72, ">= 100", "break", "sai do for\nna hora")


ANIMACOES = {
    "for_lista": (for_lista, 135),
    "for_acumulador": (for_acumulador, 140),
    "range_numeros": (range_numeros, 130),
    "break_continue": (break_continue, 145),
}
