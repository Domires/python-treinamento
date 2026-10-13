"""Animações da aula 08 - juntando tabelas (merge e concat)."""

from pandas_comum import *  # noqa: F401,F403

ESQUERDA = [["OP-0001", "Unidade_A"], ["OP-0002", "Unidade_B"], ["OP-0003", "Unidade_F"], ["OP-0004", "Unidade_A"]]
CADASTRO = [["Unidade_A", "Marcos Lima"], ["Unidade_B", "Patrícia Rocha"], ["Unidade_C", "Ricardo Nunes"]]


# -----------------------------------------------------------------------------
# merge = PROCV
# -----------------------------------------------------------------------------
def merge_procv(ax, q):
    titulo(ax, "merge: o PROCV do pandas")
    codigo(ax, 0.6, 7.25, 'producao.merge(unidades, on="unidade", how="left")', tamanho=13)

    h = 0.55
    lx, ly = 0.6, 5.8
    llarg = [1.6, 1.85, 2.4]
    rx, ry = 10.2, 5.8
    rlarg = [1.85, 2.4]
    texto(ax, lx, ly + 0.55, "producao", tamanho=11, negrito=True, cor=SUAVE)
    texto(ax, rx, ry + 0.55, "unidades (cadastro)", tamanho=11, negrito=True, cor=SUAVE)

    passo = 16
    atual = int((q - 10) // passo) if q >= 10 else -1
    gerentes = []
    for r, (_, u) in enumerate(ESQUERDA):
        achado = next((g for uu, g in CADASTRO if uu == u), None)
        preenchido = q >= 10 + r * passo + 10
        gerentes.append((achado if achado else "NaN") if preenchido else "")
    linhas = [e + [g] for e, g in zip(ESQUERDA, gerentes)]

    def estilo_esq(r, c):
        if c == 2 and gerentes[r] == "NaN":
            return {"fc": VERMELHO_CLARO, "cor": VERMELHO, "negrito": True}
        if c == 2 and gerentes[r]:
            return {"fc": VERDE_CLARO}
        if r == atual and c == 1:
            return {"fc": DESTAQUE, "ec": LARANJA, "lw": 2}
        return None

    grade(ax, lx, ly, ["id_ordem", "unidade", "gerente"], linhas, llarg, estilo=estilo_esq, h=h, tamanho=11,
          alpha_coluna=lambda c: 1.0 if c < 2 else progresso(q, 4, 8))

    alvo = None
    if 0 <= atual < len(ESQUERDA):
        u = ESQUERDA[atual][1]
        alvo = next((i for i, (uu, _) in enumerate(CADASTRO) if uu == u), None)

    def estilo_dir(r, c):
        if r == alvo:
            return {"fc": DESTAQUE, "ec": LARANJA, "lw": 2}
        return None

    grade(ax, rx, ry, ["unidade", "gerente"], CADASTRO, rlarg, estilo=estilo_dir, h=h, tamanho=11)

    if 0 <= atual < len(ESQUERDA):
        q0 = 10 + atual * passo
        y_esq = ly - (atual + 1) * h
        if alvo is not None:
            y_dir = ry - (alvo + 1) * h
            seta(ax, lx + llarg[0] + llarg[1] + 0.1, y_esq, rx - 0.1, y_dir, cor=LARANJA, alpha=janela(q, q0, q0 + 14, 2, 2), curva=-0.15)
            voo = progresso(q, q0 + 4, q0 + 10)
            if 0 < voo < 1:
                valor_solto(ax, mix(rx + rlarg[0] + 1.0, lx + llarg[0] + llarg[1] + 1.1, voo), mix(y_dir, y_esq, voo),
                            CADASTRO[alvo][1], cor=VERDE, tamanho=11)
        else:
            texto(ax, 6.5, y_esq, "não encontrou → NaN (o #N/D)", tamanho=11.5, cor=VERMELHO, negrito=True,
                  alpha=janela(q, q0 + 2, q0 + 16, 2, 2))
    legenda(ax, 'on = coluna em comum · how="left" mantém TODAS as linhas da producao', progresso(q, 78, 84))


# -----------------------------------------------------------------------------
# Tipos de junção
# -----------------------------------------------------------------------------
def tipos_join(ax, q):
    titulo(ax, "Tipos de junção: left, inner e outer")

    h = 0.46
    grade(ax, 0.6, 6.7, ["unidade"], [["Unidade_A"], ["Unidade_B"], ["Unidade_F"]], [1.9], h=h, tamanho=10.5)
    texto(ax, 0.6, 7.25, "producao", tamanho=10.5, negrito=True, cor=SUAVE)
    grade(ax, 3.0, 6.7, ["unidade", "gerente"], [[u, g.split()[0]] for u, g in CADASTRO], [1.9, 1.5], h=h, tamanho=10.5)
    texto(ax, 3.0, 7.25, "unidades", tamanho=10.5, negrito=True, cor=SUAVE)

    resultados = [
        ('how="left"', "tudo da ESQUERDA", [["Unidade_A", "Marcos"], ["Unidade_B", "Patrícia"], ["Unidade_F", "NaN"]]),
        ('how="inner"', "só o que está nas DUAS", [["Unidade_A", "Marcos"], ["Unidade_B", "Patrícia"]]),
        ('how="outer"', "tudo das DUAS", [["Unidade_A", "Marcos"], ["Unidade_B", "Patrícia"], ["Unidade_F", "NaN"],
                                          ["Unidade_C", "Ricardo"]]),
    ]
    for k, (how, nota, linhas) in enumerate(resultados):
        q0 = 10 + k * 26
        x = 0.6 + k * 5.15
        a = progresso(q, q0, q0 + 8)
        codigo(ax, x, 4.3, how, tamanho=13, alpha=a, cor=LARANJA)
        texto(ax, x, 3.85, nota, tamanho=10.5, cor=SUAVE, alpha=a)
        grade(ax, x, 3.3, ["unidade", "gerente"], linhas, [1.9, 1.5], h=h, tamanho=10.5, alpha=a,
              estilo=lambda r, c, ls=linhas: {"fc": VERMELHO_CLARO, "cor": VERMELHO} if ls[r][1] == "NaN" else None)
    legenda(ax, "O mais usado é o left: não perde nenhuma linha da sua base", progresso(q, 90, 96))


# -----------------------------------------------------------------------------
# concat: empilhando planilhas
# -----------------------------------------------------------------------------
def concat_empilhar(ax, q):
    titulo(ax, "concat: empilhando as planilhas de cada mês")
    codigo(ax, 0.6, 7.25, "consolidado = pd.concat(lista_tabelas, ignore_index=True)", tamanho=12)

    meses = [("producao_2025_01.xlsx", [["OP-0001", "Unidade_E"], ["OP-0002", "Unidade_B"]]),
             ("producao_2025_02.xlsx", [["OP-0078", "Unidade_A"], ["OP-0079", "Unidade_D"]]),
             ("producao_2025_03.xlsx", [["OP-0150", "Unidade_C"], ["OP-0151", "Unidade_A"]])]
    cores = [CORES["int"], CORES["str"], CORES["float"]]
    h = 0.48
    larg = [1.6, 1.85]
    for k, (arquivo, linhas) in enumerate(meses):
        x = 0.6 + k * 2.75
        q0 = 4 + k * 4
        icone_arquivo(ax, x + 0.5, 5.9, "", "xlsx", alpha=progresso(q, q0, q0 + 4))
        texto(ax, x + 0.5, 4.95, arquivo.replace("producao_", "producao_\n"), tamanho=9, mono=True, ha="center",
              alpha=progresso(q, q0, q0 + 4))
        desce = progresso(q, 24 + k * 10, 36 + k * 10)
        for r, linha in enumerate(linhas):
            y_origem = 4.2 - r * h
            y_destino = 4.5 - (k * 2 + r) * h
            xx = mix(x, 9.3, desce)
            yy = mix(y_origem, y_destino, desce)
            celula(ax, xx, yy, larg[0], h, linha[0], ec=cores[k], lw=1.8, tamanho=10.5)
            celula(ax, xx + larg[0], yy, larg[1], h, linha[1], ec=cores[k], lw=1.8, tamanho=10.5)
            if desce >= 1:
                celula(ax, xx + larg[0] + larg[1], yy, 2.3, h, arquivo.replace("producao_", "").replace(".xlsx", ""),
                       ec=cores[k], lw=1.8, tamanho=10, cor=cores[k])
                texto(ax, 9.0, yy, str(k * 2 + r), tamanho=10, mono=True, cor=SUAVE, ha="center",
                      alpha=progresso(q, 70, 76))
    for nome, xc, w in zip(["id_ordem", "unidade", "arquivo_origem"], x_colunas(9.3, [1.6, 1.85, 2.3]), [1.6, 1.85, 2.3]):
        celula(ax, xc, 4.5 + h, w, h, nome, fc=COR_CAB, ec="none", negrito=True, tamanho=10, alpha=progresso(q, 24, 30))
    texto(ax, 9.3, 1.3, "ignore_index=True → índice novo: 0, 1, 2...", tamanho=11, cor=SUAVE, alpha=progresso(q, 70, 76))
    legenda(ax, "12 planilhas viram uma base única: sem copiar e colar", progresso(q, 78, 84))


ANIMACOES = {
    "merge_procv": (merge_procv, 100),
    "tipos_join": (tipos_join, 110),
    "concat_empilhar": (concat_empilhar, 100),
}
