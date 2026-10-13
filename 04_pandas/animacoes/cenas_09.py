"""Animações da aula 09 - salvando relatórios."""

from pandas_comum import *  # noqa: F401,F403


# -----------------------------------------------------------------------------
# Excel com várias abas
# -----------------------------------------------------------------------------
def excel_abas(ax, q):
    titulo(ax, "ExcelWriter: várias tabelas, um arquivo, várias abas")
    codigo(ax, 0.6, 7.25, 'with pd.ExcelWriter("relatorio.xlsx") as writer:', tamanho=11.5)

    tabelas = [
        ("por_unidade", "Por Unidade", ["unidade", "produzido"], [["Unidade_A", "4.355.177"], ["Unidade_B", "3.076.849"]]),
        ("por_produto", "Por Produto", ["produto", "refugo_pct"], [["Produto_H", "0,051"], ["Produto_E", "0,050"]]),
        ("por_mes", "Mensal", ["mes", "Unidade_A"], [["1", "345.210"], ["2", "312.480"]]),
    ]
    jx, jy, jw, jh = 8.4, 1.3, 7.2, 5.0
    janela_programa(ax, jx, jy, jw, jh, "relatorio.xlsx - Excel")
    passo = 22
    abas_criadas = 0
    for k, (var, aba, cols, linhas) in enumerate(tabelas):
        q0 = 8 + k * passo
        codigo(ax, 0.9, 6.7 - k * 0.45, f'    {var}.to_excel(writer, sheet_name="{aba}")', tamanho=10,
               alpha=progresso(q, q0 - 4, q0), destaque=janela(q, q0, q0 + passo - 2, 2, 2))
        voa = progresso(q, q0 + 4, q0 + 14)
        y_tabela = 4.6 - k * 1.25
        if voa < 1:
            grade(ax, mix(0.9, jx + 0.3, voa), mix(y_tabela, jy + jh - 0.9, voa), cols, linhas, [1.75, 1.55], h=0.4, tamanho=10)
        if voa >= 1:
            abas_criadas = k + 1
    # conteúdo da aba ativa e as abas embaixo
    if abas_criadas:
        _, _, cols, linhas = tabelas[abas_criadas - 1]
        grade(ax, jx + 0.3, jy + jh - 0.9, cols, linhas, [1.75, 1.55], h=0.4, tamanho=10)
    xa = jx + 0.1
    for k in range(abas_criadas):
        nome = tabelas[k][1]
        w = len(nome) * 0.15 + 0.4
        ativa = k == abas_criadas - 1
        retangulo(ax, xa, jy + 0.1, w, 0.42, fc="white" if ativa else "#E5E7EB", ec="#16A34A" if ativa else "#9CA3AF",
                  lw=2 if ativa else 1, raio=0.04)
        texto(ax, xa + w / 2, jy + 0.31, nome, tamanho=9, ha="center", negrito=ativa, cor="#16A34A" if ativa else TINTA)
        xa += w + 0.05
    legenda(ax, "Cada to_excel(writer, sheet_name=...) vira uma ABA do mesmo arquivo", progresso(q, 76, 82))


# -----------------------------------------------------------------------------
# Um arquivo por unidade
# -----------------------------------------------------------------------------
def arquivo_por_unidade(ax, q):
    titulo(ax, "Um arquivo por unidade com um for")
    codigo(ax, 0.6, 7.25, 'for unidade in producao["unidade"].unique():', tamanho=11.5)
    codigo(ax, 0.6, 6.8, '    producao[producao["unidade"] == unidade].to_excel(f"producao_{unidade}.xlsx")', tamanho=9.5)

    unidades = ["Unidade_A", "Unidade_B", "Unidade_C"]
    linhas = [[l[0], l[1], fmt(l[5])] for l in AMOSTRA]
    passo = 24
    atual = int((q - 10) // passo) if q >= 10 else -1
    x0, y0, h = 0.6, 5.8, 0.5

    def estilo(r, c):
        u = AMOSTRA[r][1]
        if 0 <= atual < 3 and u == unidades[atual]:
            return {"fc": DESTAQUE, "ec": CORES_UNIDADE[u], "lw": 2}
        return {"cor": CORES_UNIDADE[u]} if c == 1 else None

    grade(ax, x0, y0, ["id_ordem", "unidade", "produzido"], linhas, [1.6, 1.85, 1.75], estilo=estilo, h=h, tamanho=11)
    for k, u in enumerate(unidades):
        q0 = 10 + k * passo
        x_icone, y_icone = 8.6, 5.4 - k * 1.55
        icone_arquivo(ax, x_icone, y_icone, "", "xlsx", alpha=progresso(q, q0 + 10, q0 + 16))
        texto(ax, x_icone + 0.7, y_icone + 0.15, f"producao_{u}.xlsx", tamanho=11, mono=True, alpha=progresso(q, q0 + 10, q0 + 16))
        if k == atual:
            for r, l in enumerate(AMOSTRA):
                if l[1] == u:
                    voo = progresso(q, q0 + 4, q0 + 12)
                    if 0 < voo < 1:
                        valor_solto(ax, mix(x0 + 2.5, x_icone, voo), mix(y0 - (r + 1) * h, y_icone, voo), l[0],
                                    cor=CORES_UNIDADE[u], tamanho=10)
        texto(ax, x_icone + 0.7, y_icone - 0.3, "→ enviar ao gerente", tamanho=10, cor=SUAVE, alpha=progresso(q, q0 + 16, q0 + 20))
    legenda(ax, "6 unidades = 6 arquivos, todo mês, em segundos", progresso(q, 84, 90))


ANIMACOES = {
    "excel_abas": (excel_abas, 100),
    "arquivo_por_unidade": (arquivo_por_unidade, 105),
}
