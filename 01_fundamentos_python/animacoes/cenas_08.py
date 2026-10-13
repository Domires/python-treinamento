"""Animações da aula 08 - listas."""

from base import *  # noqa: F401,F403

COR_LISTA = CORES["list"]


# -----------------------------------------------------------------------------
# Índices positivos e negativos
# -----------------------------------------------------------------------------
def lista_indices(ax, q):
    titulo(ax, "Listas: cada item tem uma posição (índice)")

    unidades = ["Jacareí I", "Jacareí II", "Suzano I", "Suzano II", "Cruz Alta"]
    largura, x0, y = 2.75, 1.65, 4.6

    acessos = [
        ("unidades[0]", [0], '"Jacareí I"', "o primeiro é o 0"),
        ("unidades[-1]", [4], '"Cruz Alta"', "negativo conta do final"),
        ("unidades[0:2]", [0, 1], '["Jacareí I", "Jacareí II"]', "fatia: o fim (2) não entra"),
    ]
    passo = 34
    atual = max(0, min(len(acessos) - 1, int((q - 14) // passo)))
    q0 = 14 + atual * passo
    expressao, selecao, resultado, nota = acessos[atual]
    marca = progresso(q, q0 + 8, q0 + 13) if q >= 14 else 0

    texto(ax, 0.6, y, "[", tamanho=40, cor=COR_LISTA)
    texto(ax, 15.05, y, "]", tamanho=40, cor=COR_LISTA)
    for i, unidade in enumerate(unidades):
        x = x0 + i * largura + 0.05
        aparece = progresso(q, i * 2, i * 2 + 6)
        bloco(ax, x + 0.4, y, unidade, COR_LISTA, w=largura - 0.25, h=1.1, tamanho=12.5, alpha=aparece,
              destaque=1 if (marca > 0.5 and i in selecao) else 0)
        texto(ax, x + 0.4, y - 0.95, str(i), tamanho=13, mono=True, ha="center", negrito=True, alpha=aparece,
              cor=LARANJA if (marca > 0.5 and i in selecao and atual != 1) else TINTA)
        texto(ax, x + 0.4, y + 0.95, str(i - len(unidades)), tamanho=11, mono=True, ha="center",
              cor=LARANJA if (marca > 0.5 and atual == 1 and i in selecao) else SUAVE, alpha=aparece)

    if q >= 14:
        codigo(ax, 0.8, 7.1, digitado(expressao, q, q0, q0 + 7), tamanho=17)
        texto(ax, 5.2, 7.1, nota, tamanho=12, cor=SUAVE, alpha=marca)
        balao(ax, 8.0, 2.2, f"→  {resultado}", alpha=progresso(q, q0 + 13, q0 + 18), tamanho=14)

    legenda(ax, "A contagem começa em ZERO", progresso(q, 8, 12) * (1 - progresso(q, 30, 34)))


# -----------------------------------------------------------------------------
# append, insert, remove e pop
# -----------------------------------------------------------------------------
def desenhar_transicao(ax, antes, depois, p, y, x0=1.8, passo=2.6, removido_para=None):
    """Desenha a lista passando do estado 'antes' para 'depois' (p de 0 a 1)."""
    for item in set(antes) | set(depois):
        if item in antes and item in depois:
            x = mix(x0 + antes.index(item) * passo, x0 + depois.index(item) * passo, p)
            bloco(ax, x, y, item, COR_LISTA, w=2.3, h=1.0, tamanho=13)
        elif item in depois:   # entrando
            x = x0 + depois.index(item) * passo
            bloco(ax, x, mix(y + 1.6, y, p), item, COR_LISTA, w=2.3, h=1.0, tamanho=13, alpha=p, destaque=1)
        else:                  # saindo
            x = x0 + antes.index(item) * passo
            destino = removido_para if removido_para else (x, y - 1.8)
            bloco(ax, mix(x, destino[0], p), mix(y, destino[1], p), item, VERMELHO, w=2.3, h=1.0, tamanho=13,
                  alpha=1 - 0.6 * p)


def lista_metodos(ax, q):
    titulo(ax, "Alterando listas")

    estados = [
        ("unidades = [...]", ["Mauá", "Suzano", "Jacareí"], ""),
        ('unidades.append("Cruz Alta")', ["Mauá", "Suzano", "Jacareí", "Cruz Alta"], "adiciona no FINAL"),
        ('unidades.insert(1, "Paulínia")', ["Mauá", "Paulínia", "Suzano", "Jacareí", "Cruz Alta"], "adiciona na posição 1"),
        ('unidades.remove("Suzano")', ["Mauá", "Paulínia", "Jacareí", "Cruz Alta"], "remove pelo VALOR"),
        ("removido = unidades.pop()", ["Mauá", "Paulínia", "Jacareí"], "remove o ÚLTIMO e devolve"),
    ]
    passo = 30
    atual = max(0, min(len(estados) - 1, int((q - 4) // passo)))
    q0 = 4 + atual * passo
    comando, depois, nota = estados[atual]
    antes = estados[atual - 1][1] if atual > 0 else depois
    p = progresso(q, q0 + 8, q0 + 20) if atual > 0 else 1

    codigo(ax, 0.8, 7.0, digitado(comando, q, q0, q0 + 7) if atual else comando, tamanho=16)
    texto(ax, 0.8, 6.3, nota, tamanho=12, cor=SUAVE, alpha=progresso(q, q0 + 6, q0 + 10))

    destino_pop = (12.5, 1.6) if atual == 4 else None
    desenhar_transicao(ax, antes, depois, p, 4.2, removido_para=destino_pop)
    for i in range(len(depois) if p >= 1 else len(antes)):
        texto(ax, 1.8 + i * 2.6, 3.35, str(i), tamanho=11, mono=True, cor=SUAVE, ha="center")

    if atual == 4 and p >= 1:
        caixa(ax, 12.5, 1.6, "removido", '"Cruz Alta"', cor=CORES["str"], w=3.4, h=1.0, tamanho_valor=14)
    elif atual == 3 and p >= 1:
        legenda(ax, "Os itens seguintes \"andam\" para a esquerda", progresso(q, q0 + 20, q0 + 24))


# -----------------------------------------------------------------------------
# Cópia x referência
# -----------------------------------------------------------------------------
def lista_copia(ax, q):
    titulo(ax, "Copiar lista: referência x cópia")

    def lista(x, y, valores, alpha=1.0, destaque_remover=0.0):
        retangulo(ax, x - 0.2, y - 0.6, len(valores) * 1.1 + 0.4 if valores else 1.0, 1.2, fc=CAIXA,
                  ec=COR_LISTA, lw=2.2, alpha=alpha)
        for i, v in enumerate(valores):
            bloco(ax, x + 0.35 + i * 1.1, y, str(v), COR_LISTA if not (v == 2 and destaque_remover > 0.5) else VERMELHO,
                  w=0.9, h=0.8, tamanho=15, alpha=alpha)

    # ----- parte de cima: referência -----
    texto(ax, 0.6, 7.25, "minha_lista = lista_original", tamanho=14, mono=True)
    remove_1 = progresso(q, 30, 38)
    valores_1 = [1, 2, 3] if remove_1 < 1 else [1, 3]
    lista(7.6, 6.1, valores_1, destaque_remover=janela(q, 24, 38, 2, 1))
    etiqueta(ax, 2.3, 6.5, "lista_original", SUAVE, tamanho=11)
    etiqueta(ax, 2.3, 5.7, "minha_lista", COR_LISTA, tamanho=11, alpha=progresso(q, 6, 12))
    seta(ax, 3.8, 6.5, 7.3, 6.25, cor=SUAVE)
    seta(ax, 3.6, 5.7, 7.3, 5.95, cor=COR_LISTA, alpha=progresso(q, 6, 12))
    codigo(ax, 11.9, 6.1, "minha_lista.remove(2)", tamanho=10, alpha=progresso(q, 20, 24))
    texto(ax, 7.6, 4.95, "as DUAS mudam: é a mesma lista!", tamanho=12, cor=VERMELHO, alpha=progresso(q, 40, 46))

    # ----- parte de baixo: cópia -----
    base_q = 60
    texto(ax, 0.6, 3.75, "minha_lista = lista_original.copy()", tamanho=14, mono=True, alpha=progresso(q, base_q, base_q + 5))
    etiqueta(ax, 2.3, 2.7, "lista_original", SUAVE, tamanho=11, alpha=progresso(q, base_q, base_q + 5))
    lista(6.0, 2.7, [1, 2, 3], alpha=progresso(q, base_q, base_q + 5))
    seta(ax, 3.8, 2.7, 5.7, 2.7, cor=SUAVE, alpha=progresso(q, base_q, base_q + 5))

    remove_2 = progresso(q, base_q + 30, base_q + 38)
    copia = progresso(q, base_q + 8, base_q + 18)
    if copia > 0:
        valores_2 = [1, 2, 3] if remove_2 < 1 else [1, 3]
        lista(mix(6.0, 10.6, copia), mix(2.7, 1.5, copia), valores_2, destaque_remover=janela(q, base_q + 24, base_q + 38, 2, 1))
        etiqueta(ax, 9.1, 1.5, "minha_lista", COR_LISTA, tamanho=11, alpha=copia)
    texto(ax, 10.5, 2.7, "minha_lista.remove(2)", tamanho=10, mono=True, alpha=progresso(q, base_q + 20, base_q + 24))
    legenda(ax, "com .copy() a original NÃO muda", progresso(q, base_q + 40, base_q + 46))


ANIMACOES = {
    "lista_indices": (lista_indices, 130),
    "lista_metodos": (lista_metodos, 160),
    "lista_copia": (lista_copia, 130),
}
