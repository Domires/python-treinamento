"""Animações da aula 09 - dicionários."""

from base import *  # noqa: F401,F403

COR_DICT = CORES["dict"]


def gaveta(ax, x, y, chave, valor, cor_valor=TINTA, alpha=1.0, destaque=0.0, w_chave=2.6, w_valor=3.6,
           valor_alpha=None):
    """Um par chave: valor desenhado como uma "gaveta" (x, y = canto esquerdo central)."""
    if alpha <= 0:
        return
    retangulo(ax, x, y - 0.42, w_chave, 0.84, fc=COR_DICT, ec="none", alpha=alpha * 0.9, raio=0.12)
    texto(ax, x + w_chave / 2, y, chave, tamanho=13, mono=True, cor="white", ha="center", negrito=True, alpha=alpha)
    texto(ax, x + w_chave + 0.2, y, ":", tamanho=14, mono=True, alpha=alpha)
    retangulo(ax, x + w_chave + 0.55, y - 0.42, w_valor, 0.84, fc=DESTAQUE if destaque > 0.5 else CAIXA,
              ec=COR_DICT, lw=2, alpha=alpha, raio=0.12)
    texto(ax, x + w_chave + 0.55 + w_valor / 2, y, valor, tamanho=14, mono=True, cor=cor_valor, ha="center",
          alpha=alpha if valor_alpha is None else valor_alpha)


# -----------------------------------------------------------------------------
# Chave -> valor e acesso pela chave
# -----------------------------------------------------------------------------
def dicionario_chave_valor(ax, q):
    titulo(ax, "Dicionário: cada CHAVE guarda um VALOR")

    pares = [("marca", '"Ford"'), ("modelo", '"Mustang"'), ("ano", "1964")]
    texto(ax, 0.8, 6.9, "carro", tamanho=14, mono=True, negrito=True, alpha=progresso(q, 0, 5))
    acessos = [
        ('carro["modelo"]', 1, '"Mustang"', VERDE),
        ('carro.get("cor")', None, "None   (sem erro)", SUAVE),
        ('carro["cor"]', None, "KeyError: 'cor'", VERMELHO),
    ]
    passo = 30
    atual = max(0, min(len(acessos) - 1, int((q - 22) // passo)))
    q0 = 22 + atual * passo
    expressao, indice, resultado, cor = acessos[atual]
    procura = janela(q, q0 + 8, q0 + passo - 2, 2, 2) if q >= 22 else 0

    for k, (chave, valor) in enumerate(pares):
        gaveta(ax, 1.0, 6.0 - k * 1.1, chave, valor, alpha=progresso(q, 2 + k * 5, 8 + k * 5),
               destaque=procura if indice == k else 0)

    if q >= 22:
        codigo(ax, 9.0, 6.0, digitado(expressao, q, q0, q0 + 7), tamanho=16)
        if indice is not None:
            seta(ax, 8.9, 5.9, 7.9, 4.9 + 0.0, cor=LARANJA, alpha=procura, curva=0.2)
        balao(ax, 11.5, 4.3, f"→  {resultado}", alpha=progresso(q, q0 + 12, q0 + 17), tamanho=14,
              fc="#FEE2E2" if cor == VERMELHO else DESTAQUE, cor=cor if cor != SUAVE else TINTA)

    legenda(ax, "Procuramos pela chave (como um PROCV), não pela posição", progresso(q, 10, 16))


# -----------------------------------------------------------------------------
# Alterando, adicionando e removendo
# -----------------------------------------------------------------------------
def dicionario_alterar(ax, q):
    titulo(ax, "Alterando um dicionário")

    passos = [
        ('carro["ano"] = 2022', "chave existe → ALTERA o valor"),
        ('carro["cor"] = "vermelho"', "chave nova → ADICIONA"),
        ('del carro["modelo"]', "remove a chave"),
    ]
    passo = 36
    atual = max(-1, min(len(passos) - 1, int((q - 10) // passo)))
    q0 = 10 + max(0, atual) * passo

    if atual >= 0:
        comando, nota = passos[atual]
        codigo(ax, 0.8, 7.2, digitado(comando, q, q0, q0 + 7), tamanho=16)
        texto(ax, 0.8, 6.5, nota, tamanho=12, cor=SUAVE, alpha=progresso(q, q0 + 7, q0 + 11))

    efeito = lambda k: progresso(q, 10 + k * passo + 10, 10 + k * passo + 20)  # noqa: E731

    # ano: 1964 -> 2022
    troca_ano = efeito(0)
    # cor: entra
    entra_cor = efeito(1)
    # modelo: sai
    sai_modelo = efeito(2)

    linhas = [("marca", '"Ford"', 1.0, 0.0), ("modelo", '"Mustang"', 1 - sai_modelo, 0.0)]
    y = 5.3
    posicoes = {}
    for chave, valor, alpha, _ in linhas:
        posicoes[chave] = y
        y -= 1.1
    # "ano" e "cor" sobem quando "modelo" sai
    y_ano = mix(5.3 - 2.2, 5.3 - 1.1, sai_modelo)
    y_cor = mix(5.3 - 3.3, 5.3 - 2.2, sai_modelo)

    gaveta(ax, 1.0, posicoes["marca"], "marca", '"Ford"')
    gaveta(ax, mix(1.0, 6.0, sai_modelo), posicoes["modelo"] - sai_modelo * 0.6, "modelo", '"Mustang"',
           alpha=1 - sai_modelo)
    valor_ano = "1964" if troca_ano < 0.5 else "2022"
    gaveta(ax, 1.0, y_ano, "ano", valor_ano, destaque=janela(q, 10 + 10, 10 + 26, 2, 2),
           valor_alpha=abs(troca_ano - 0.5) * 2 if 0 < troca_ano < 1 else 1)
    gaveta(ax, 1.0, mix(y_cor - 1.0, y_cor, entra_cor), "cor", '"vermelho"', alpha=entra_cor,
           destaque=janela(q, 10 + passo + 10, 10 + passo + 26, 2, 2))

    painel(ax, 9.6, 1.4, 5.9, 3.9, "print(carro)", alpha=progresso(q, 2, 8))
    atual_dict = {"marca": '"Ford"'}
    if sai_modelo < 1:
        atual_dict["modelo"] = '"Mustang"'
    atual_dict["ano"] = valor_ano
    if entra_cor >= 1:
        atual_dict["cor"] = '"vermelho"'
    for k, (chave, valor) in enumerate(atual_dict.items()):
        texto(ax, 9.9, 4.5 - k * 0.65, f'"{chave}": {valor},', tamanho=11.5, mono=True)


# -----------------------------------------------------------------------------
# Lista de dicionários = tabela
# -----------------------------------------------------------------------------
def lista_de_dicionarios(ax, q):
    titulo(ax, "Lista de dicionários = uma tabela")

    pedidos = [{"pedido": 1, "local": "SP", "valor": 50000.0},
               {"pedido": 2, "local": "RJ", "valor": 40000.0},
               {"pedido": 3, "local": "MG", "valor": 100000.0}]
    colunas = ["pedido", "local", "valor"]
    x_colunas = [10.6, 12.5, 14.5]

    vira_tabela = progresso(q, 40, 60)
    for k, pedido in enumerate(pedidos):
        aparece = progresso(q, 4 + k * 8, 10 + k * 8)
        y_lista = 6.5 - k * 1.55
        y_tabela = 5.6 - k * 0.9
        # como dicionário (à esquerda)
        conteudo = "{" + ", ".join(f'"{c}": ' + (f'"{pedido[c]}"' if isinstance(pedido[c], str) else repr(pedido[c])) for c in colunas) + "}"
        codigo(ax, 0.6, y_lista, conteudo, tamanho=10, alpha=aparece * (1 - 0.6 * vira_tabela))
        texto(ax, 0.6, y_lista - 0.5, f"pedidos[{k}]", tamanho=10, mono=True, cor=SUAVE, alpha=aparece)
        # cada valor voa para a sua célula da tabela
        for c, coluna in enumerate(colunas):
            x0 = 0.6 + (conteudo.index(f'"{coluna}"') + len(coluna) + 4) * LARGURA_CHAR * 10 / 15
            if vira_tabela > 0:
                destaque_celula = janela(q, 80, 120, 3, 3) if (k == 0 and coluna == "valor") else 0
                if destaque_celula > 0.5 and vira_tabela >= 1:
                    retangulo(ax, x_colunas[c] - 0.95, y_tabela - 0.35, 1.9, 0.7, fc=DESTAQUE, ec=LARANJA, raio=0.08)
                valor_solto(ax, mix(x0, x_colunas[c], vira_tabela), mix(y_lista, y_tabela, vira_tabela),
                            str(pedido[coluna]), cor=CORES["float"] if coluna == "valor" else TINTA, tamanho=13)

    # cabeçalho da tabela
    for c, coluna in enumerate(colunas):
        etiqueta(ax, x_colunas[c], 6.5, coluna, COR_DICT, tamanho=12, alpha=progresso(q, 56, 62))
    for k in range(3):
        texto(ax, 9.2, 5.6 - k * 0.9, str(k), tamanho=12, mono=True, cor=SUAVE, ha="center", alpha=progresso(q, 56, 62))

    codigo(ax, 0.6, 1.6, 'pedidos[0]["valor"]', tamanho=15, alpha=progresso(q, 76, 80))
    texto(ax, 5.6, 1.6, "→  50000.0   (linha 0, coluna valor)", tamanho=13, alpha=progresso(q, 84, 88))
    legenda(ax, "É exatamente assim que o pandas e as APIs (JSON) organizam os dados", progresso(q, 92, 98))


ANIMACOES = {
    "dicionario_chave_valor": (dicionario_chave_valor, 125),
    "dicionario_alterar": (dicionario_alterar, 135),
    "lista_de_dicionarios": (lista_de_dicionarios, 135),
}
