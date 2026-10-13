"""Animações da aula 06 - lendo o CSV."""

from base import *  # noqa: F401,F403

LINHAS_CSV = [
    ["fabrica", "codigo_material", "nome_material", "quantidade", "observacao"],
    ["Fábrica São Paulo", "MAT-0001", "Açúcar Cristal", "500", "Local seco"],
    ["Fábrica Campinas", "MAT-0002", "Óleo de Soja", "1200", ""],
    ["Fábrica Curitiba", "MAT-0003", "Farinha de Trigo", "8", "Exportação"],
]
X_COLUNAS = [0.7, 3.8, 6.3, 9.15, 11.4]
LARGURAS = [3.0, 2.4, 2.8, 2.1, 2.3]


def tabela(ax, y_topo, alpha=1.0, vazio="", destaque_linha=None, destaque_vazio=0.0):
    """Tabela do pandas com as linhas do CSV."""
    for c, nome in enumerate(LINHAS_CSV[0]):
        retangulo(ax, X_COLUNAS[c], y_topo - 0.32, LARGURAS[c] - 0.08, 0.64, fc="#E0F2FE", ec="none", alpha=alpha, raio=0.04)
        texto(ax, X_COLUNAS[c] + 0.12, y_topo, nome, tamanho=9.5, mono=True, negrito=True, alpha=alpha)
    for r, linha in enumerate(LINHAS_CSV[1:]):
        y = y_topo - 0.75 - r * 0.62
        if destaque_linha == r:
            retangulo(ax, 0.1, y - 0.3, 13.6, 0.6, fc=DESTAQUE, ec=LARANJA, lw=1.5, alpha=alpha, raio=0.05)
        texto(ax, 0.3, y, str(r), tamanho=9.5, mono=True, cor=SUAVE, alpha=alpha)
        for c, valor in enumerate(linha):
            mostrar = valor if valor != "" else vazio
            cor = VERMELHO if (valor == "" and vazio == "NaN") else TINTA
            if valor == "" and destaque_vazio > 0:
                retangulo(ax, X_COLUNAS[c], y - 0.25, LARGURAS[c] - 0.1, 0.5, fc="#DCFCE7", ec=VERDE,
                          alpha=alpha * destaque_vazio, raio=0.04)
            texto(ax, X_COLUNAS[c] + 0.12, y, mostrar, tamanho=10, alpha=alpha, cor=cor)


# -----------------------------------------------------------------------------
# Do texto do CSV para a tabela
# -----------------------------------------------------------------------------
def csv_para_tabela(ax, q):
    titulo(ax, "CSV: um texto com colunas separadas por ;")

    texto(ax, 0.6, 7.25, "produtos.csv  (aberto no Bloco de Notas)", tamanho=10.5, cor=SUAVE)
    some = progresso(q, 40, 50)
    for r, linha in enumerate(LINHAS_CSV):
        conteudo = ";".join(linha)
        y = 6.7 - r * 0.45
        # pinta os ";" de vermelho desenhando-os por cima
        codigo(ax, 0.6, y, conteudo, tamanho=11, alpha=1 - 0.75 * some)
        pos = 0
        for parte in linha[:-1]:
            pos += len(parte)
            valor_solto(ax, x_char(0.6, pos, 11) + 0.09, y, ";", cor=VERMELHO, tamanho=11,
                        alpha=janela(q, 12, 40, 3, 4))
            pos += 1

    codigo(ax, 0.6, 4.55, 'tabela = pd.read_csv("produtos.csv", sep=";", dtype=str)', tamanho=11,
           alpha=progresso(q, 30, 36))
    tabela(ax, 3.6, alpha=progresso(q, 46, 54), vazio="NaN" if q < 84 else "",
           destaque_vazio=progresso(q, 84, 88))

    codigo(ax, 0.6, 0.6, 'tabela = tabela.fillna("")', tamanho=11, alpha=progresso(q, 72, 76),
           destaque=janela(q, 76, 100, 2, 3))
    texto(ax, 7.4, 0.6, "células vazias (NaN) viram texto vazio", tamanho=10.5, cor=SUAVE, alpha=progresso(q, 80, 86))


# -----------------------------------------------------------------------------
# iterrows: percorrendo linha por linha
# -----------------------------------------------------------------------------
def iterrows_linhas(ax, q):
    titulo(ax, "iterrows(): percorrendo a tabela linha por linha")

    codigo(ax, 0.6, 7.2, "for indice, linha in tabela.iterrows():", tamanho=12)
    codigo(ax, 0.6, 6.7, '    print(linha["codigo_material"], "-", linha["nome_material"])', tamanho=11)

    passo = 26
    atual = max(-1, min(2, int((q - 8) // passo)))
    tabela(ax, 5.8, vazio="", destaque_linha=atual if atual >= 0 else None)

    if atual >= 0:
        linha = LINHAS_CSV[1 + atual]
        q0 = 8 + atual * passo
        caixa(ax, 1.3, 2.0, "indice", str(atual), cor=CORES["int"], w=1.6, h=0.9, tamanho_valor=15)
        retangulo(ax, 2.6, 0.9, 7.9, 2.0, fc=CAIXA, ec=CORES["list"], lw=2.2)
        texto(ax, 2.75, 3.15, "linha", tamanho=12, mono=True, negrito=True)
        texto(ax, 2.8, 2.5, f'linha["codigo_material"]  →  "{linha[1]}"', tamanho=9.5, mono=True)
        texto(ax, 2.8, 1.95, f'linha["nome_material"]    →  "{linha[2]}"', tamanho=9.5, mono=True)
        texto(ax, 2.8, 1.4, f'linha["quantidade"]       →  "{linha[3]}"', tamanho=9.5, mono=True)
        voa = progresso(q, q0, q0 + 8)
        if voa < 1:
            valor_solto(ax, 7.6, mix(5.05 - atual * 0.62, 2.5, voa), linha[1], cor=CORES["list"], tamanho=12, alpha=1 - voa * 0.3)

    painel(ax, 10.8, 0.9, 4.7, 2.3, "Terminal", escuro=True)
    for k in range(3):
        linha = LINHAS_CSV[1 + k]
        saida_terminal(ax, 11.0, 2.45 - k * 0.5, f"{linha[1]} - {linha[2]}", tamanho=9.5,
                       alpha=progresso(q, 8 + k * passo + 12, 8 + k * passo + 15))


ANIMACOES = {
    "csv_para_tabela": (csv_para_tabela, 115),
    "iterrows_linhas": (iterrows_linhas, 110),
}
