"""Animações da aula 06 - colunas calculadas."""

from pandas_comum import *  # noqa: F401,F403

REFUGO = [555, 726, 400, 392, 760, 330]


# -----------------------------------------------------------------------------
# Indicadores: eficiência e % de refugo
# -----------------------------------------------------------------------------
def indicadores_colunas(ax, q):
    titulo(ax, "Indicadores: eficiência e % de refugo")

    x0, y0, h = 0.9, 5.9, 0.5
    cols = ["unidade", "planejado", "produzido", "refugo", "eficiencia", "refugo_pct"]
    larg = [1.85, 1.75, 1.75, 1.3, 1.9, 1.9]
    xs = x_colunas(x0, larg)

    ef_todas = progresso(q, 34, 38) >= 1
    ref_todas = progresso(q, 70, 74) >= 1
    linhas = []
    for (op, uni, turno, prod, plan, produzido), refugo in zip(AMOSTRA, REFUGO):
        ef = f"{produzido / plan:.3f}" if ef_todas else ""
        rp = f"{refugo / produzido:.3f}" if ref_todas else ""
        linhas.append([uni, fmt(plan), fmt(produzido), fmt(refugo), ef, rp])

    def estilo(r, c):
        if c == 4 and ef_todas:
            return {"fc": VERDE_CLARO}
        if c == 5 and ref_todas:
            return {"fc": VERDE_CLARO}
        if r == 0 and ((c in (1, 2) and 12 <= q < 34) or (c in (2, 3) and 50 <= q < 70)):
            return {"fc": DESTAQUE}
        return None

    grade(ax, x0, y0, cols, linhas, larg, estilo=estilo, h=h, tamanho=10.5,
          alpha_coluna=lambda c: 1.0 if c < 4 else progresso(q, 4 + (c - 4) * 44, 8 + (c - 4) * 44))

    codigo(ax, 0.6, 7.25, 'producao["eficiencia"] = producao["qtd_produzida_kg"] / producao["qtd_planejada_kg"]',
           tamanho=10, destaque=janela(q, 4, 42, 2, 2))
    codigo(ax, 0.6, 6.75, 'producao["refugo_pct"] = producao["qtd_refugo_kg"] / producao["qtd_produzida_kg"]',
           tamanho=10, alpha=progresso(q, 44, 48), destaque=janela(q, 46, 80, 2, 2))
    balao(ax, 8.0, 2.0, "linha 0:  18.500 ÷ 20.000 = 0,925  (92,5% do plano)", alpha=janela(q, 14, 34, 3, 3), tamanho=12)
    balao(ax, 8.0, 2.0, "linha 0:  555 ÷ 18.500 = 0,030  (3% virou refugo)", alpha=janela(q, 52, 70, 3, 3), tamanho=12)
    legenda(ax, "A mesma conta é feita para TODAS as linhas de uma vez", progresso(q, 82, 88))


# -----------------------------------------------------------------------------
# Coluna com condição usando .loc
# -----------------------------------------------------------------------------
def loc_condicao(ax, q):
    titulo(ax, "Coluna com condição (o SE do Excel) usando .loc")

    eficiencias = [0.925, 0.807, 1.017, 0.817, 0.950, 0.936]
    passos = [
        ('producao["faixa"] = "Baixa"', None, "Baixa"),
        ('producao.loc[producao["eficiencia"] >= 0.85, "faixa"] = "Média"', 0.85, "Média"),
        ('producao.loc[producao["eficiencia"] >= 0.95, "faixa"] = "Alta"', 0.95, "Alta"),
    ]
    cores_faixa = {"Baixa": VERMELHO_CLARO, "Média": DESTAQUE, "Alta": VERDE_CLARO}
    passo = 30
    atual = max(-1, min(2, int((q - 6) // passo)))

    for k, (cmd, _, _) in enumerate(passos):
        codigo(ax, 0.6, 7.25 - k * 0.5, cmd, tamanho=10.5, alpha=1.0 if k <= atual else 0.3,
               destaque=1.0 if k == atual else 0)

    faixas = [None] * 6
    marcadas = set()
    for k in range(atual + 1):
        _, limite, nome = passos[k]
        aplica = q >= 6 + k * passo + 14
        for r, ef in enumerate(eficiencias):
            if limite is None or ef >= limite:
                if k == atual:
                    marcadas.add(r)
                if aplica or k < atual:
                    faixas[r] = nome

    x0, y0, h = 3.0, 5.4, 0.52
    linhas = [[AMOSTRA[r][0], f"{eficiencias[r]:.3f}", faixas[r] or ""] for r in range(6)]

    def estilo(r, c):
        if c == 1 and r in marcadas and atual >= 1:
            return {"fc": DESTAQUE, "ec": LARANJA, "lw": 2}
        if c == 2 and faixas[r]:
            return {"fc": cores_faixa[faixas[r]], "negrito": True}
        return None

    grade(ax, x0, y0, ["id_ordem", "eficiencia", "faixa"], linhas, [1.7, 1.9, 1.7], estilo=estilo, h=h, tamanho=11)
    texto(ax, 9.0, 3.6, "cada .loc sobrescreve só\nas linhas da condição", tamanho=12, cor=SUAVE, alpha=progresso(q, 40, 46))
    legenda(ax, "Ordem importa: do valor padrão para a condição mais exigente", progresso(q, 98, 104))


# -----------------------------------------------------------------------------
# Datas com .dt
# -----------------------------------------------------------------------------
def datas_dt(ax, q):
    titulo(ax, "Datas com .dt: extraindo partes da data")

    bloco(ax, 8.0, 6.5, "2025-03-14", CORES["int"], w=3.6, h=0.9, tamanho=20)
    texto(ax, 8.0, 7.25, 'producao["data"]', tamanho=11, mono=True, cor=SUAVE, ha="center")

    partes = [(".dt.year", "2025"), (".dt.month", "3"), (".dt.quarter", "1  (1º trimestre)"),
              (".dt.dayofweek", "4  (0 = segunda)"), ('.dt.strftime("%Y-%m")', '"2025-03"')]
    for k, (metodo, resultado) in enumerate(partes):
        q0 = 8 + k * 14
        y = 5.0 - k * 0.82
        voa = progresso(q, q0, q0 + 8)
        if voa > 0:
            if voa < 1:
                valor_solto(ax, mix(8.0, 7.6, voa), mix(6.5, y, voa), resultado.split()[0], cor=CORES["int"], tamanho=13)
            codigo(ax, 2.0, y, metodo, tamanho=13, alpha=voa)
            texto(ax, 6.7, y, "→", tamanho=14, cor=SUAVE, alpha=voa)
            if voa >= 1:
                texto(ax, 7.4, y, resultado, tamanho=13, mono=True, negrito=True, cor=CORES["int"])

    q_map = 8 + 5 * 14 + 4
    seta(ax, 11.0, 5.0 - 3 * 0.82, 12.2, 5.0 - 3 * 0.82, cor=LARANJA, alpha=progresso(q, q_map, q_map + 4))
    texto(ax, 12.3, 5.0 - 3 * 0.82 + 0.35, ".map(nomes_dias)", tamanho=10, mono=True, cor=LARANJA, alpha=progresso(q, q_map, q_map + 4))
    texto(ax, 12.3, 5.0 - 3 * 0.82 - 0.15, '"Sexta"', tamanho=13, mono=True, negrito=True, cor=CORES["str"],
          alpha=progresso(q, q_map + 4, q_map + 8))
    legenda(ax, "Ótimo para agrupar por mês, trimestre ou dia da semana", progresso(q, q_map + 10, q_map + 16))


ANIMACOES = {
    "indicadores_colunas": (indicadores_colunas, 110),
    "loc_condicao": (loc_condicao, 120),
    "datas_dt": (datas_dt, 115),
}
