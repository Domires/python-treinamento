"""Animações da aula 03 - lendo e explorando dados."""

from pandas_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# Lendo Excel e CSV e dando uma olhada nos dados
# -----------------------------------------------------------------------------
def ler_arquivos(ax, q):
    titulo(ax, "Lendo arquivos: do Excel/CSV para um DataFrame")
    b = 80
    if q < b:
        # 1) Excel
        icone_arquivo(ax, 1.3, 5.9, "producao.xlsx", "xlsx")
        codigo(ax, 0.6, 7.25, 'producao = pd.read_excel("producao.xlsx")', tamanho=12, alpha=progresso(q, 2, 6))
        seta(ax, 1.95, 5.9, 2.65, 5.9, cor=SUAVE, alpha=progresso(q, 6, 10))

        x0, y0, h = 3.3, 6.4, 0.44
        linhas = [[fmt(v) for v in linha] for linha in AMOSTRA] + [["...", "...", "...", "...", "...", "..."]]
        linhas_visiveis = int(7 * progresso(q, 10, 24))
        head = janela(q, 30, 52, 2, 2) > 0.5

        def estilo(r, c):
            if head and r < 5:
                return {"fc": DESTAQUE}
            return None

        if linhas_visiveis > 0:
            grade(ax, x0, y0, COLUNAS_AMOSTRA, linhas[:linhas_visiveis], LARGURAS_AMOSTRA, indice=list(range(6)) + ["..."],
                  estilo=estilo, h=h, tamanho=10, largura_indice=0.55)
        texto(ax, x0, 2.75, "+ 893 linhas", tamanho=10, cor=SUAVE, alpha=progresso(q, 24, 28))

        codigo(ax, 0.6, 1.95, "producao.head()", tamanho=13, alpha=progresso(q, 28, 32), destaque=janela(q, 30, 52, 2, 2))
        texto(ax, 4.4, 1.95, "→ as 5 primeiras linhas", tamanho=11.5, cor=SUAVE, alpha=progresso(q, 32, 36))
        codigo(ax, 0.6, 1.2, "producao.shape", tamanho=13, alpha=progresso(q, 54, 58), destaque=janela(q, 56, 76, 2, 2))
        texto(ax, 4.4, 1.2, "→ (900, 10)  = 900 linhas e 10 colunas", tamanho=11.5, cor=SUAVE, alpha=progresso(q, 58, 62))
    else:
        # 2) CSV
        icone_arquivo(ax, 1.2, 5.6, "produtos.csv", "csv")
        texto(ax, 2.4, 6.2, "o arquivo por dentro:", tamanho=10.5, cor=SUAVE)
        texto(ax, 2.4, 5.7, "produto;categoria;custo_kg", tamanho=12, mono=True)
        texto(ax, 2.4, 5.25, "Produto_A;Granulado;2,35", tamanho=12, mono=True)
        texto(ax, 2.4, 4.8, "Produto_B;Granulado;2,80", tamanho=12, mono=True)
        codigo(ax, 0.6, 7.25, 'produtos = pd.read_csv("produtos.csv", sep=";", decimal=",")', tamanho=12,
               alpha=progresso(q, b, b + 5))
        seta(ax, 7.6, 5.3, 8.8, 5.3, cor=SUAVE, alpha=progresso(q, b + 6, b + 10))
        grade(ax, 9.3, 6.0, ["produto", "categoria", "custo_kg"], [["Produto_A", "Granulado", "2.35"],
              ["Produto_B", "Granulado", "2.80"]], [1.9, 1.95, 1.65], h=0.5, tamanho=11, indice=[0, 1],
              alpha=progresso(q, b + 8, b + 14))
        texto(ax, 0.6, 2.9, 'sep=";"       → o ; separa as colunas', tamanho=12.5, mono=False, alpha=progresso(q, b + 14, b + 18))
        texto(ax, 0.6, 2.2, 'decimal=","   → 2,35 vira o NÚMERO 2.35 (dá para fazer contas)', tamanho=12.5,
              alpha=progresso(q, b + 18, b + 22))


ANIMACOES = {
    "ler_arquivos": (ler_arquivos, 130),
}
