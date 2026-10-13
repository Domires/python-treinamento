"""Animações da aula 03 - textos (strings)."""

from base import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# f-string: os valores das variáveis entram nas chaves
# -----------------------------------------------------------------------------
def f_string(ax, q):
    titulo(ax, "f-string: encaixando variáveis no texto")

    modelo = 'f"O {nome} trabalha como {cargo} em {local}"'
    x_modelo, y_modelo = 0.8, 6.9
    variaveis = [("nome", '"João"', 3.0), ("cargo", '"Analista"', 8.0), ("local", '"São Paulo"', 13.0)]

    for k, (nome, valor, x) in enumerate(variaveis):
        caixa(ax, x, 3.9, nome, valor, cor=CORES["str"], w=3.6, alpha=progresso(q, 4 + k * 4, 10 + k * 4),
              tamanho_valor=16)

    for k, (nome, valor, x) in enumerate(variaveis):
        q0 = 25 + k * 22
        marcar_trecho(ax, x_modelo, y_modelo, modelo, "{" + nome + "}", alpha=janela(q, q0 + 12, q0 + 22, 3, 3))
    codigo(ax, x_modelo, y_modelo, modelo, alpha=progresso(q, 0, 6))

    for k, (nome, valor, x) in enumerate(variaveis):
        q0 = 25 + k * 22
        voo = progresso(q, q0, q0 + 14)
        if 0 < voo < 1:
            destino = x_do_trecho(x_modelo, modelo, "{" + nome + "}")
            valor_solto(ax, mix(x, destino, voo), mix(3.9, y_modelo, voo), valor.strip('"'),
                        cor=CORES["str"], tamanho=16)

    painel(ax, 0.6, 1.2, 14.8, 1.1, escuro=True, alpha=progresso(q, 92, 98))
    saida_terminal(ax, 1.0, 1.75, digitado("O João trabalha como Analista em São Paulo", q, 96, 116),
                   tamanho=14)


# -----------------------------------------------------------------------------
# Índices e fatiamento
# -----------------------------------------------------------------------------
def fatiamento(ax, q):
    titulo(ax, "Índices e fatiamento: texto[início:fim]")

    email = "alex.rangel@icl-group.com"
    largura = 0.58
    x0 = 8 - len(email) * largura / 2
    y = 5.0

    fatias = [
        ("email[0:11]", range(0, 11), 11, "'alex.rangel'", "o fim (11) não entra"),
        ("email[12:]", range(12, 25), None, "'icl-group.com'", "sem fim: vai até o final"),
        ("email[-13:]", range(12, 25), None, "'icl-group.com'", "negativo: conta do final"),
    ]
    passo = 36
    atual = max(0, min(len(fatias) - 1, int((q - 16) // passo)))
    q0 = 16 + atual * passo
    expressao, selecao, excluido, resultado, nota = fatias[atual]
    marca = progresso(q, q0 + 10, q0 + 16) if q >= 16 else 0

    for i, letra in enumerate(email):
        x = x0 + i * largura + largura / 2
        aparece = progresso(q, i * 0.4, i * 0.4 + 5)
        selecionado = marca > 0.5 and i in selecao
        retangulo(ax, x - largura / 2 + 0.03, y - 0.42, largura - 0.06, 0.84,
                  fc=DESTAQUE if selecionado else CAIXA,
                  ec=VERMELHO if (excluido == i and marca > 0.5) else (LARANJA if selecionado else BORDA),
                  lw=2.2 if selecionado or excluido == i else 1.2, alpha=aparece, raio=0.08)
        texto(ax, x, y, letra, tamanho=14, mono=True, ha="center", alpha=aparece)
        negativo = atual == 2 and marca > 0.5
        texto(ax, x, y - 0.75, str(i - len(email)) if negativo else str(i), tamanho=8.5,
              cor=LARANJA if negativo else SUAVE, ha="center", alpha=aparece)

    if q >= 16:
        codigo(ax, 0.8, 7.0, digitado(expressao, q, q0, q0 + 8), tamanho=17)
        texto(ax, 4.5, 7.0, nota, tamanho=12, cor=SUAVE, alpha=marca)
        balao(ax, 8, 2.6, f"→  {resultado}", alpha=progresso(q, q0 + 16, q0 + 22), tamanho=16)

    legenda(ax, "A contagem começa em 0", progresso(q, 10, 16) * (1 - progresso(q, 30, 34)))


# -----------------------------------------------------------------------------
# Métodos de texto
# -----------------------------------------------------------------------------
def metodos_texto(ax, q):
    titulo(ax, "Métodos de texto")

    original = "  sulfurgran premium  "
    visivel = lambda s: s.replace(" ", "·")  # noqa: E731
    codigo(ax, 0.8, 7.1, 'produto = "  sulfurgran premium  "', tamanho=14)

    metodos = [
        ("produto.upper()", original.upper()),
        ("produto.title()", original.title()),
        ("produto.strip()", original.strip()),
        ('produto.replace("premium", "standard")', original.replace("premium", "standard")),
        ("produto.strip().upper()", original.strip().upper()),
    ]
    for k, (chamada, resultado) in enumerate(metodos):
        q0 = 10 + k * 22
        y = 5.9 - k * 0.95
        codigo(ax, 0.8, y, digitado(chamada, q, q0, q0 + 8), tamanho=12)
        texto(ax, 9.4, y, "→", tamanho=15, cor=SUAVE, alpha=progresso(q, q0 + 9, q0 + 12))
        codigo(ax, 10.1, y, f'"{visivel(resultado)}"', tamanho=12, cor=CORES["str"],
               alpha=progresso(q, q0 + 10, q0 + 15), destaque=janela(q, q0 + 10, q0 + 22, 3, 3))

    legenda(ax, "· = espaço     métodos podem ser encadeados: .strip().upper()", progresso(q, 30, 38))


# -----------------------------------------------------------------------------
# split e join
# -----------------------------------------------------------------------------
def split_join(ax, q):
    titulo(ax, "split() quebra o texto  ·  join() junta")

    linha = "2026-01-15;Cliente A;1500.00"
    partes = linha.split(";")
    tamanho = 16
    lc = LARGURA_CHAR * tamanho / 15
    x_linha, y_linha = 4.2, 6.6

    codigo(ax, 0.8, 7.5, 'linha.split(";")', alpha=progresso(q, 14, 18), tamanho=13, cor=SUAVE)

    # posições das partes no texto original
    inicios, pos = [], 0
    for parte in partes:
        inicios.append(pos)
        pos += len(parte) + 1

    separa = progresso(q, 20, 36)
    junta = progresso(q, 70, 86)
    x_lista = [3.2, 8.0, 12.8]
    x_final_inicio = 8 - len(" | ".join(partes)) * lc / 2

    if separa < 1:
        # o texto inteiro, com os ";" sumindo
        for parte, inicio in zip(partes, inicios):
            x_centro = x_linha + (inicio + len(parte) / 2) * lc
            valor_solto(ax, mix(x_centro, x_lista[partes.index(parte)], separa), mix(y_linha, 4.6, separa),
                        parte, cor=CORES["str"], tamanho=tamanho)
        for inicio, parte in zip(inicios[1:], partes[1:]):
            valor_solto(ax, x_linha + (inicio - 0.5) * lc, y_linha, ";", cor=VERMELHO, alpha=1 - separa,
                        tamanho=tamanho)
    elif junta < 1:
        for k, parte in enumerate(partes):
            fim_x = x_final_inicio + (sum(len(p) + 3 for p in partes[:k]) + len(parte) / 2) * lc
            if junta == 0:
                bloco(ax, x_lista[k], 4.6, "", CORES["list"], w=4.2, h=1.0)
                texto(ax, x_lista[k], 3.8, f"[{k}]", tamanho=10, cor=SUAVE, mono=True, ha="center")
            valor_solto(ax, mix(x_lista[k], fim_x, junta), mix(4.6, 2.4, junta), f"'{parte}'" if junta == 0 else parte,
                        cor=CORES["str"], tamanho=tamanho if junta else 14)
        if junta == 0:
            texto(ax, 0.6, 4.6, "[", tamanho=36, cor=CORES["list"])
            texto(ax, 15.1, 4.6, "]", tamanho=36, cor=CORES["list"])
    else:
        codigo(ax, x_final_inicio, 2.4, " | ".join(partes), tamanho=tamanho, cor=CORES["str"])

    codigo(ax, 0.8, 3.2, '" | ".join(partes)', alpha=progresso(q, 62, 66), tamanho=13, cor=SUAVE)
    legenda(ax, "split devolve uma LISTA de textos", janela(q, 38, 66, 6, 4))
    legenda(ax, "join cola os itens usando o separador escolhido", progresso(q, 90, 96))


ANIMACOES = {
    "f_string": (f_string, 135),
    "fatiamento": (fatiamento, 140),
    "metodos_texto": (metodos_texto, 140),
    "split_join": (split_join, 120),
}
