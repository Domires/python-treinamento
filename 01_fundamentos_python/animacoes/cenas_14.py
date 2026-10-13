"""Animações da aula 14 - arquivos e pastas."""

from base import *  # noqa: F401,F403

COR_PASTA = "#CA8A04"
COR_ARQUIVO = "#475569"


def icone_pasta(ax, x, y, nome, alpha=1.0, destaque=False, tamanho=12):
    """Pasta (x, y = canto esquerdo central)."""
    if alpha <= 0:
        return
    retangulo(ax, x, y - 0.28, 0.7, 0.56, fc="#FDE68A", ec=COR_PASTA, lw=1.8, alpha=alpha, raio=0.06)
    retangulo(ax, x, y + 0.2, 0.32, 0.16, fc="#FDE68A", ec=COR_PASTA, lw=1.5, alpha=alpha, raio=0.04)
    if destaque:
        retangulo(ax, x + 0.85, y - 0.27, len(nome) * 0.17 + 0.3, 0.54, fc=DESTAQUE, ec="none", alpha=alpha, raio=0.08)
    texto(ax, x + 1.0, y, nome, tamanho=tamanho, mono=True, alpha=alpha)


def icone_arquivo(ax, x, y, nome, alpha=1.0, destaque=False, cor=COR_ARQUIVO, tamanho=12):
    if alpha <= 0:
        return
    retangulo(ax, x + 0.1, y - 0.33, 0.5, 0.66, fc="white", ec=cor, lw=1.8, alpha=alpha, raio=0.04)
    for i in range(3):
        ax.plot([x + 0.2, x + 0.5], [y + 0.15 - i * 0.15] * 2, color=cor, lw=1, alpha=alpha)
    if destaque:
        retangulo(ax, x + 0.85, y - 0.27, len(nome) * 0.17 + 0.3, 0.54, fc=DESTAQUE, ec="none", alpha=alpha, raio=0.08)
    texto(ax, x + 1.0, y, nome, tamanho=tamanho, mono=True, alpha=alpha)


# -----------------------------------------------------------------------------
# Montando caminhos com Path e /
# -----------------------------------------------------------------------------
def caminhos(ax, q):
    titulo(ax, "Caminhos com pathlib: juntando com /")

    passos = [
        ("PASTA_ATUAL = Path(__file__).parent", r"C:\...\01_fundamentos_python"),
        ('PASTA_TESTE = PASTA_ATUAL / "pasta_de_teste"', r"C:\...\01_fundamentos_python\pasta_de_teste"),
        ('arquivo = PASTA_TESTE / "anotacoes.txt"', r"C:\...\pasta_de_teste\anotacoes.txt"),
    ]
    for k, (comando, resultado) in enumerate(passos):
        q0 = 6 + k * 30
        y = 7.1 - k * 1.25
        codigo(ax, 0.8, y, digitado(comando, q, q0, q0 + 8), tamanho=12.5)
        texto(ax, 1.2, y - 0.5, "→ " + resultado, tamanho=10.5, mono=True, cor=SUAVE, alpha=progresso(q, q0 + 10, q0 + 14))

    # árvore de pastas
    retangulo(ax, 8.8, 0.9, 6.7, 2.9, fc=CAIXA, ec=BORDA)
    icone_pasta(ax, 9.1, 3.25, "01_fundamentos_python", alpha=progresso(q, 10, 16), destaque=janela(q, 10, 36, 3, 3) > 0.5,
                tamanho=11)
    ax.plot([9.45, 9.45, 9.9], [2.95, 2.25, 2.25], color=BORDA, lw=1.5, alpha=progresso(q, 46, 52))
    icone_pasta(ax, 9.9, 2.25, "pasta_de_teste", alpha=progresso(q, 46, 52), destaque=janela(q, 46, 66, 3, 3) > 0.5,
                tamanho=11)
    ax.plot([10.25, 10.25, 10.7], [1.95, 1.3, 1.3], color=BORDA, lw=1.5, alpha=progresso(q, 76, 82))
    icone_arquivo(ax, 10.7, 1.3, "anotacoes.txt", alpha=progresso(q, 76, 82), destaque=q >= 76, tamanho=11)

    legenda(ax, "A / funciona em qualquer sistema (Windows, Linux, Mac)", progresso(q, 96, 102))


# -----------------------------------------------------------------------------
# Modos de abertura: w, a, r
# -----------------------------------------------------------------------------
def modos_arquivo(ax, q):
    titulo(ax, 'open(): modos "w", "a" e "r"')

    # documento
    x_doc, y_doc = 9.2, 1.0
    retangulo(ax, x_doc, y_doc, 6.0, 5.6, fc="white", ec=COR_ARQUIVO, lw=2)
    texto(ax, x_doc + 0.3, y_doc + 5.25, "anotacoes.txt", tamanho=11, mono=True, cor=SUAVE)

    conteudo_antigo = ["texto antigo...", "mais texto antigo"]
    linhas_w = ["Reunião às 14h", "Enviar relatório"]
    linha_a = "Conferir estoque"

    passos = [
        ('with open(arquivo, "w") as f:', 'f.write("Reunião às 14h\\n...")', "w: APAGA tudo e escreve do zero"),
        ('with open(arquivo, "a") as f:', 'f.write("Conferir estoque\\n")', "a: adiciona no FINAL"),
        ('with open(arquivo, "r") as f:', "conteudo = f.read()", "r: só lê"),
    ]
    passo = 38
    atual = max(0, min(2, int((q - 6) // passo)))
    q0 = 6 + atual * passo
    cmd1, cmd2, nota = passos[atual]
    codigo(ax, 0.8, 6.9, digitado(cmd1, q, q0, q0 + 7), tamanho=12.5)
    codigo(ax, 0.8, 6.3, "    " + digitado(cmd2, q, q0 + 7, q0 + 13), tamanho=12.5)
    texto(ax, 0.8, 5.5, nota, tamanho=13, negrito=True, cor=LARANJA, alpha=progresso(q, q0 + 13, q0 + 17))

    y0 = y_doc + 4.6
    if atual == 0:
        apaga = progresso(q, q0 + 14, q0 + 22)
        for i, linha in enumerate(conteudo_antigo):
            texto(ax, x_doc + 0.4, y0 - i * 0.55, linha, tamanho=12, mono=True, cor=VERMELHO, alpha=1 - apaga)
        for i, linha in enumerate(linhas_w):
            texto(ax, x_doc + 0.4, y0 - i * 0.55, digitado(linha, q, q0 + 22 + i * 6, q0 + 28 + i * 6), tamanho=12, mono=True)
    else:
        for i, linha in enumerate(linhas_w):
            texto(ax, x_doc + 0.4, y0 - i * 0.55, linha, tamanho=12, mono=True)
        if atual == 1:
            texto(ax, x_doc + 0.4, y0 - 2 * 0.55, digitado(linha_a, q, q0 + 16, q0 + 24), tamanho=12, mono=True, cor=VERDE)
        else:
            texto(ax, x_doc + 0.4, y0 - 2 * 0.55, linha_a, tamanho=12, mono=True)

    if atual == 2:
        le = progresso(q, q0 + 16, q0 + 28)
        retangulo(ax, x_doc + 0.2, y0 - 1.45, 5.0, 1.75, fc="none", ec=LARANJA, lw=2, alpha=janela(q, q0 + 14, q0 + 30, 3, 3))
        if 0 < le < 1:
            valor_solto(ax, mix(x_doc + 2.5, 3.0, le), mix(y0 - 0.6, 2.4, le), "...", cor=CORES["str"])
        caixa(ax, 3.4, 2.4, "conteudo", '"Reunião às 14h\\n..."' if le >= 1 else None, cor=CORES["str"], w=5.2, h=1.0,
              tamanho_valor=12, alpha=progresso(q, q0 + 10, q0 + 15))

    legenda(ax, 'Use sempre encoding="utf-8" para os acentos funcionarem', progresso(q, 118, 124))


# -----------------------------------------------------------------------------
# Copiar, mover e renomear
# -----------------------------------------------------------------------------
def copiar_mover(ax, q):
    titulo(ax, "Copiar, renomear e mover arquivos")

    # duas pastas
    for x, nome in [(0.8, "pasta_de_teste"), (9.0, "02_fevereiro")]:
        retangulo(ax, x, 1.2, 6.2, 4.4, fc="#FFFBEB", ec=COR_PASTA, lw=2)
        icone_pasta(ax, x + 0.3, 5.15, nome, tamanho=11.5)

    passos = [
        ('shutil.copy(origem, destino)', "copiar: o original CONTINUA lá"),
        ('origem.rename(novo_nome)', "renomear: mesmo lugar, nome novo"),
        ('shutil.move(arquivo, outra_pasta)', "mover: sai de um lugar e vai para outro"),
    ]
    passo = 34
    atual = max(-1, min(2, int((q - 8) // passo)))
    if atual >= 0:
        q0 = 8 + atual * passo
        cmd, nota = passos[atual]
        codigo(ax, 0.8, 7.2, digitado(cmd, q, q0, q0 + 8), tamanho=14)
        texto(ax, 0.8, 6.5, nota, tamanho=12, cor=SUAVE, alpha=progresso(q, q0 + 8, q0 + 12))

    copia = progresso(q, 8 + 10, 8 + 22)
    renomeia = progresso(q, 8 + passo + 10, 8 + passo + 16)
    move = progresso(q, 8 + 2 * passo + 10, 8 + 2 * passo + 22)

    # arquivo 1: copiado (o original fica)
    nome_1 = "relatorio_1.txt" if renomeia < 0.5 else "relatorio_vendas.txt"
    icone_arquivo(ax, 1.2, 4.2, nome_1, destaque=0.5 < renomeia and q < 8 + 2 * passo)
    if copia > 0:
        icone_arquivo(ax, mix(1.2, 9.4, copia), mix(4.2, 4.2, copia), "relatorio_1.txt" if copia < 1 else "relatorio_1_copia.txt",
                      cor=VERDE, destaque=copia >= 1 and q < 8 + passo)

    # arquivo 2: movido
    icone_arquivo(ax, mix(1.2, 9.4, move), mix(3.2, 3.2, move), "relatorio_2.txt",
                  cor=CORES["int"] if move > 0 else COR_ARQUIVO, destaque=move >= 1)
    icone_arquivo(ax, 1.2, 2.2, "relatorio_3.txt")

    legenda(ax, "CUIDADO: apagar pelo Python (unlink, rmtree) NÃO manda para a lixeira", progresso(q, 116, 122))


ANIMACOES = {
    "caminhos": (caminhos, 125),
    "modos_arquivo": (modos_arquivo, 140),
    "copiar_mover": (copiar_mover, 135),
}
