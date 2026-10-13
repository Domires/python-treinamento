"""Animações da aula 01 - variáveis e tipos."""

from base import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# 1. O Python lê de cima para baixo
# -----------------------------------------------------------------------------
def cima_para_baixo(ax, q):
    titulo(ax, "O Python lê de cima para baixo")

    linhas = ['print("Passo 1: Abrir o Excel")',
              'print("Passo 2: Copiar os dados")',
              'print("Passo 3: Colar no relatório")']
    saidas = ["Passo 1: Abrir o Excel", "Passo 2: Copiar os dados", "Passo 3: Colar no relatório"]

    # painel do código
    ax.add_patch(FancyBboxPatch((0.5, 2.0), 8.6, 5.2, boxstyle="round,pad=0,rounding_size=0.2",
                                fc=CAIXA, ec=BORDA, lw=1.5))
    ax.text(0.8, 6.85, "aula.py", fontsize=11, color=SUAVE, family=FONTE, va="center")

    # painel do terminal
    ax.add_patch(FancyBboxPatch((9.5, 2.0), 6.0, 5.2, boxstyle="round,pad=0,rounding_size=0.2",
                                fc=TERMINAL, ec="none"))
    ax.text(9.8, 6.85, "Terminal", fontsize=11, color="#9CA3AF", family=FONTE, va="center")

    inicio, passo = 12, 26
    for k, linha in enumerate(linhas):
        y = 5.9 - k * 1.2
        ativo = progresso(q, inicio + k * passo, inicio + k * passo + 5) - progresso(q, inicio + (k + 1) * passo, inicio + (k + 1) * passo + 5)
        if k == len(linhas) - 1:
            ativo = progresso(q, inicio + k * passo, inicio + k * passo + 5)
        codigo(ax, 1.25, y, linha, destaque=ativo, tamanho=12)
        if ativo > 0.05:
            ax.text(0.85, y, "▶", fontsize=13, color="#D97706", va="center", ha="center", alpha=ativo)

        saida_alpha = progresso(q, inicio + k * passo + 10, inicio + k * passo + 16)
        if saida_alpha > 0:
            ax.text(9.8, 5.9 - k * 1.2, saidas[k], fontsize=12, family=MONO, color=TERMINAL_TEXTO,
                    va="center", alpha=saida_alpha)

    legenda(ax, "Cada linha é executada na ordem em que aparece, uma de cada vez",
            progresso(q, inicio + 3 * passo, inicio + 3 * passo + 8))


# -----------------------------------------------------------------------------
# 2. Criando variáveis: caixinha com etiqueta
# -----------------------------------------------------------------------------
def variavel_caixa(ax, q):
    titulo(ax, "Variável = uma caixinha com etiqueta")

    passos = [
        # (código, nome, valor, cor, x da caixa, largura, y do código, quadro inicial)
        ("quantidade = 123", "quantidade", "123", CORES["int"], 4.2, 3.2, 7.0, 5),
        ('unidade = "Jacareí I"', "unidade", '"Jacareí I"', CORES["str"], 11.6, 4.4, 6.2, 70),
    ]

    for texto, nome, valor, cor, x_caixa, largura, y_codigo, q0 in passos:
        digitado = int(len(texto) * progresso(q, q0, q0 + 20))
        if digitado > 0:
            codigo(ax, 0.8, y_codigo, texto[:digitado])

        caixa_alpha = progresso(q, q0 + 22, q0 + 30)
        voo = progresso(q, q0 + 34, q0 + 52)
        caixa(ax, x_caixa, 3.4, nome, valor if voo >= 1 else None, cor=cor, alpha=caixa_alpha, w=largura)

        if 0 < voo < 1:
            x0 = x_do_trecho(0.8, texto, valor)
            valor_solto(ax, mix(x0, x_caixa, voo), mix(y_codigo, 3.4, voo), valor, cor=cor)

    legenda(ax, "O sinal  =  significa: guarde este valor nesta variável", progresso(q, 40, 50))


# -----------------------------------------------------------------------------
# 3. Variáveis podem mudar de valor
# -----------------------------------------------------------------------------
def variavel_muda_valor(ax, q):
    titulo(ax, "Variáveis podem mudar de valor")

    linhas = ["estoque = 1000", "estoque = 2000", "estoque = estoque - 300"]
    etapas = [10, 50, 95]          # quadro em que cada linha começa
    fim_etapas = [48, 92, 999]
    x_caixa, y_caixa = 12.2, 3.6

    for k, linha in enumerate(linhas):
        ativo = progresso(q, etapas[k], etapas[k] + 5) * (1 - progresso(q, fim_etapas[k], fim_etapas[k] + 5))
        codigo(ax, 0.8, 6.4 - k * 1.1, linha, destaque=ativo, alpha=0.35 + 0.65 * progresso(q, etapas[k] - 6, etapas[k]))

    # valor atual dentro da caixa
    valor_atual = None
    if q >= 30:
        valor_atual = "1000"
    if q >= 75:
        valor_atual = "2000"
    if q >= 140:
        valor_atual = "1700"

    # valores saindo (o antigo cai e some)
    saida_1000 = progresso(q, 58, 70)
    saida_2000 = progresso(q, 122, 134)
    esconder = (58 <= q < 75) or (122 <= q < 140)
    caixa(ax, x_caixa, y_caixa, "estoque", None if esconder else valor_atual, cor=CORES["int"])

    if 0 < saida_1000 < 1:
        valor_solto(ax, x_caixa + 2.6 * saida_1000, y_caixa - 1.6 * saida_1000, "1000", cor=SUAVE, alpha=1 - saida_1000)
    if 0 < saida_2000 < 1:
        valor_solto(ax, x_caixa + 2.6 * saida_2000, y_caixa - 1.6 * saida_2000, "2000", cor=SUAVE, alpha=1 - saida_2000)

    # valores entrando
    entra_1000 = progresso(q, 15, 30)
    if 0 < entra_1000 < 1:
        x0 = x_do_trecho(0.8, linhas[0], "1000")
        valor_solto(ax, mix(x0, x_caixa, entra_1000), mix(6.4, y_caixa, entra_1000), "1000", cor=CORES["int"])
    entra_2000 = progresso(q, 62, 75)
    if 0 < entra_2000 < 1:
        x0 = x_do_trecho(0.8, linhas[1], "2000")
        valor_solto(ax, mix(x0, x_caixa, entra_2000), mix(5.3, y_caixa, entra_2000), "2000", cor=CORES["int"])

    # conta da terceira linha
    conta = progresso(q, 100, 110)
    if conta > 0 and q < 140:
        ax.text(x_caixa, 6.6, "2000 - 300 = 1700", ha="center", va="center", fontsize=15, family=MONO,
                color=TINTA, alpha=conta,
                bbox=dict(boxstyle="round,pad=0.4", fc=DESTAQUE, ec="none", alpha=conta))
    entra_1700 = progresso(q, 126, 140)
    if 0 < entra_1700 < 1:
        valor_solto(ax, x_caixa, mix(6.6, y_caixa, entra_1700), "1700", cor=CORES["int"])

    legenda(ax, "O valor antigo é substituído pelo novo", progresso(q, 60, 70))


# -----------------------------------------------------------------------------
# 4. Tipos de dados
# -----------------------------------------------------------------------------
def tipos_de_dados(ax, q):
    titulo(ax, "Tipos de dados")

    itens = [
        ("nome", '"Ana"', "str  ·  texto", CORES["str"]),
        ("idade", "34", "int  ·  inteiro", CORES["int"]),
        ("salario", "5750.5", "float  ·  decimal", CORES["float"]),
        ("ativo", "True", "bool  ·  lógico", CORES["bool"]),
    ]
    for k, (nome, valor, tipo, cor) in enumerate(itens):
        q0 = 8 + k * 22
        x = 2.2 + k * 3.85
        aparece = progresso(q, q0, q0 + 8)
        if aparece > 0:
            ax.text(x, 6.7, f"{nome} = {valor}", ha="center", va="center", fontsize=12,
                    family=MONO, color=TINTA, alpha=aparece)
        caixa(ax, x, 4.2, nome, valor, cor=cor, alpha=aparece, w=3.3,
              tipo=tipo, tipo_alpha=progresso(q, q0 + 9, q0 + 15))

    legenda(ax, "type(variavel) mostra o tipo   ·   números decimais usam PONTO: 5750.5",
            progresso(q, 100, 110))


# -----------------------------------------------------------------------------
# 5. "10" é diferente de 10
# -----------------------------------------------------------------------------
def texto_vs_numero(ax, q):
    titulo(ax, 'Cuidado: "10" é diferente de 10')

    linhas = [
        # (y, rótulo, valor, resultado, explicação, cor, quadro inicial, largura do bloco, resultado "colado")
        (5.7, "número", "10", "20", "soma", CORES["int"], 8),
        (2.9, "texto", '"10"', '"1010"', "junta (concatena)", CORES["str"], 62),
    ]
    for y, rotulo, valor, resultado, explicacao, cor, q0 in linhas:
        aparece = progresso(q, q0, q0 + 8)
        if aparece > 0:
            ax.text(0.6, y, rotulo, fontsize=14, color=cor, weight="bold", va="center", family=FONTE, alpha=aparece)

        junta = progresso(q, q0 + 16, q0 + 34)
        x_a, x_b, x_res = 3.6, 6.6, 10.0
        largura = 1.6 if rotulo == "número" else 1.9

        if junta < 1:
            if rotulo == "número":
                destino_a = destino_b = x_res
            else:
                destino_a, destino_b = x_res - largura / 2, x_res + largura / 2
            bloco(ax, mix(x_a, destino_a, junta), y, valor, cor, alpha=aparece, w=largura)
            bloco(ax, mix(x_b, destino_b, junta), y, valor, cor, alpha=aparece, w=largura)
            sinais = aparece * (1 - junta)
            if sinais > 0:
                ax.text((x_a + x_b) / 2, y, "+", fontsize=22, ha="center", va="center", color=TINTA, alpha=sinais)
        else:
            bloco(ax, x_res, y, resultado, cor, w=1.6 if rotulo == "número" else 2 * largura)

        nota = progresso(q, q0 + 36, q0 + 44)
        if nota > 0:
            ax.text(12.4, y, explicacao, fontsize=13, color=SUAVE, va="center", family=FONTE, alpha=nota)

    legenda(ax, "Com aspas é texto; sem aspas é número", progresso(q, 110, 118))


# -----------------------------------------------------------------------------
# 6. Casting (conversão de tipos)
# -----------------------------------------------------------------------------
def casting(ax, q):
    titulo(ax, "Casting: convertendo tipos")
    codigo(ax, 0.8, 7.2, 'valor = "10"', tamanho=14)

    conversoes = [
        ("str(valor)", '"10"', "str", 6.0),
        ("int(valor)", "10", "int", 4.5),
        ("float(valor)", "10.0", "float", 3.0),
    ]
    x_entrada, x_maquina, x_saida = 2.4, 7.6, 12.6
    y_linha = 4.5

    bloco(ax, x_entrada, y_linha, '"10"', CORES["str"], w=1.9)
    ax.text(x_entrada, y_linha - 1.0, "texto", ha="center", fontsize=11, color=CORES["str"], family=FONTE)

    ciclo = 40
    atual = min(q // ciclo, len(conversoes) - 1)
    for k, (funcao, resultado, tipo, y_saida) in enumerate(conversoes):
        q0 = 8 + k * ciclo
        cor = CORES[tipo]
        entra = progresso(q, q0, q0 + 12)
        sai = progresso(q, q0 + 18, q0 + 30)

        if k == atual:
            pisca = progresso(q, q0 + 12, q0 + 15) * (1 - progresso(q, q0 + 16, q0 + 20))
            ax.add_patch(FancyBboxPatch((x_maquina - 1.7, y_linha - 0.9), 3.4, 1.8,
                                        boxstyle="round,pad=0,rounding_size=0.25",
                                        fc=DESTAQUE if pisca > 0.1 else CAIXA, ec=TINTA, lw=2.5))
            ax.text(x_maquina, y_linha, funcao, ha="center", va="center", fontsize=14, family=MONO, color=TINTA)
            # o valor entra até a borda esquerda da "máquina" e sai pela borda direita
            if 0 < entra < 1:
                valor_solto(ax, mix(x_entrada + 1.2, x_maquina - 2.2, entra), y_linha, '"10"',
                            cor=CORES["str"], alpha=1 - entra)
            if 0 < sai < 1:
                valor_solto(ax, mix(x_maquina + 2.3, x_saida, sai), mix(y_linha, y_saida, sai), resultado,
                            cor=cor, alpha=min(1.0, sai * 4))

        if sai >= 1:
            bloco(ax, x_saida, y_saida, resultado, cor, w=1.9)
            ax.text(x_saida + 1.3, y_saida, tipo, va="center", fontsize=12, color="white", weight="bold",
                    family=FONTE, bbox=dict(boxstyle="round,pad=0.3", fc=cor, ec="none"))

    legenda(ax, "str() → texto     int() → inteiro     float() → decimal", progresso(q, 120, 128))


# -----------------------------------------------------------------------------
# 7. Desempacotamento
# -----------------------------------------------------------------------------
def desempacotamento(ax, q):
    titulo(ax, "Desempacotamento")
    codigo(ax, 0.8, 7.2, "minha_lista = [1, 2, 3]", tamanho=14)
    codigo(ax, 0.8, 6.5, "x, y, z = minha_lista", tamanho=14,
           destaque=progresso(q, 14, 20), alpha=0.35 + 0.65 * progresso(q, 10, 16))

    # a lista: 3 células lado a lado
    x_lista = [10.2, 11.6, 13.0]
    y_lista = 6.6
    ax.text(11.6, 7.75, "minha_lista", ha="center", fontsize=12, family=MONO, color=SUAVE)
    ax.text(9.3, y_lista, "[", fontsize=34, ha="center", va="center", color=TINTA)
    ax.text(13.9, y_lista, "]", fontsize=34, ha="center", va="center", color=TINTA)

    x_caixas = [4.0, 8.0, 12.0]
    nomes = ["x", "y", "z"]
    for k in range(3):
        q0 = 24 + k * 20
        voo = progresso(q, q0, q0 + 14)
        cor = CORES["int"]
        if voo < 1:
            bloco(ax, x_lista[k], y_lista, str(k + 1), cor, w=1.2, h=1.0, alpha=1 - 0.6 * (voo > 0))
        else:
            bloco(ax, x_lista[k], y_lista, str(k + 1), cor, w=1.2, h=1.0, alpha=0.35)
        ax.text(x_lista[k], y_lista - 0.8, f"[{k}]", ha="center", fontsize=10, color=SUAVE, family=MONO)

        caixa(ax, x_caixas[k], 2.9, nomes[k], str(k + 1) if voo >= 1 else None, cor=cor, w=2.4, h=1.4)
        if 0 < voo < 1:
            valor_solto(ax, mix(x_lista[k], x_caixas[k], voo), mix(y_lista, 2.9, voo), str(k + 1), cor=cor)

    legenda(ax, "Cada item da lista vai para uma variável, na mesma ordem", progresso(q, 85, 93))


ANIMACOES = {
    "cima_para_baixo": (cima_para_baixo, 125),
    "variavel_caixa": (variavel_caixa, 150),
    "variavel_muda_valor": (variavel_muda_valor, 170),
    "tipos_de_dados": (tipos_de_dados, 140),
    "texto_vs_numero": (texto_vs_numero, 140),
    "casting": (casting, 150),
    "desempacotamento": (desempacotamento, 120),
}
