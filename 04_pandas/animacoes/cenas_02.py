"""Animações da aula 02 - Series e DataFrames."""

from pandas_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# loc (rótulo) x iloc (posição)
# -----------------------------------------------------------------------------
def loc_iloc(ax, q):
    titulo(ax, "loc usa o RÓTULO · iloc usa a POSIÇÃO")

    linhas = [["20.000", "18.500"], ["18.000", "18.300"], ["15.000", "12.100"]]
    rotulos = ["turno_A", "turno_B", "turno_C"]
    x0, y0, h = 3.2, 4.8, 0.55
    larguras = [2.9, 2.9]

    passos = [
        ('df.loc["turno_A"]', {0}, None, "linha com o RÓTULO turno_A"),
        ("df.iloc[2]", {2}, None, "linha na POSIÇÃO 2 (a 3ª)"),
        ('df.loc["turno_C", "produzido_kg"]', set(), (2, 1), "uma célula: linha, coluna"),
        ("df.iloc[0:2]", {0, 1}, None, "posições 0 e 1 (o fim não entra)"),
    ]
    passo = 26
    atual = max(0, min(3, int((q - 6) // passo)))
    q0 = 6 + atual * passo
    comando, linhas_sel, celula_sel, nota = passos[atual]
    marca = progresso(q, q0 + 9, q0 + 13)

    def estilo(r, c):
        if marca > 0.5 and (r in linhas_sel or celula_sel == (r, c)):
            return {"fc": DESTAQUE, "ec": LARANJA, "lw": 2}
        return None

    grade(ax, x0, y0, ["planejado_kg", "produzido_kg"], linhas, larguras, indice=rotulos, estilo=estilo, h=h, tamanho=11.5,
          largura_indice=1.5)
    # posições (iloc)
    for r in range(3):
        usa_posicao = "iloc" in comando and marca > 0.5 and r in linhas_sel
        texto(ax, x0 - 2.0, y0 - (r + 1) * h, str(r), tamanho=12, mono=True, ha="center", negrito=usa_posicao,
              cor=LARANJA if usa_posicao else SUAVE)
    texto(ax, x0 - 2.0, y0 + 0.55, "posição", tamanho=9.5, cor=SUAVE, ha="center")
    texto(ax, x0 - 0.75, y0 + 0.55, "rótulo", tamanho=9.5, cor=SUAVE, ha="center")
    if "loc[" in comando and marca > 0.5:
        for r in linhas_sel | ({celula_sel[0]} if celula_sel else set()):
            retangulo(ax, x0 - 1.5, y0 - (r + 1) * h - h / 2 + 0.03, 1.48, h - 0.06, fc="none", ec=LARANJA, lw=2, raio=0.04)

    codigo(ax, 0.8, 7.0, digitado(comando, q, q0, q0 + 8), tamanho=17)
    texto(ax, 0.8, 6.3, nota, tamanho=12, cor=SUAVE, alpha=marca)
    texto(ax, 10.6, 4.0, "loc  → pelo NOME\niloc → pelo NÚMERO\n        (começa em 0)", tamanho=12.5, alpha=progresso(q, 2, 8))


ANIMACOES = {
    "loc_iloc": (loc_iloc, 120),
}
