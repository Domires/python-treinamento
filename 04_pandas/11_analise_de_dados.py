#%%
# ANÁLISE COMPLETA (FECHAMENTO ANUAL DA PRODUÇÃO)
# Situação:
#   A área industrial recebe 12 planilhas (uma por mês) com as ordens de produção de todas as unidades. Alguém precisa:
#     1. juntar todas as planilhas em uma base única
#     2. calcular os indicadores (produção, eficiência, refugo, paradas e custo)
#     3. comparar o realizado com a meta de cada unidade
#     4. montar um Excel de relatório com várias abas e um gráfico
#     5. escrever um resumo executivo para a diretoria
#   Hoje isso leva uma manhã inteira. Vamos fazer em menos de 1 minuto, usando tudo o que vimos no treinamento

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E CONFIGURAÇÕES
# ...

#%%
# import time
# from datetime import date
# from pathlib import Path

# import pandas as pd
# import matplotlib.pyplot as plt

# PASTA = Path(__file__).parent
# PASTA_DADOS = PASTA / "dados"
# PASTA_SAIDA = PASTA / "relatorios" / "fechamento"
# PASTA_SAIDA.mkdir(parents=True, exist_ok=True)

# pd.set_option("display.max_columns", 20)
# pd.set_option("display.width", 200)

# inicio = time.time()

#%%
# FUNÇÕES AUXILIARES: FORMATAR NO PADRÃO BRASILEIRO
# ...

#%%
# def formatar_numero(valor, casas=0):
#     """1234.5 -> '1.234' (ou '1.234,50' com casas=2)"""
#     return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# def formatar_moeda(valor):
#     return f"R$ {formatar_numero(valor, 2)}"

# def formatar_pct(valor):
#     """0.822 -> '82,2%'"""
#     return f"{formatar_numero(valor * 100, 1)}%"

#%%
# ETAPA 1 - CONSOLIDAR AS PLANILHAS MENSAIS (concat)
mostrar_animacao("fluxo_fechamento")
# ...

#%%
# tabelas = []
# for arquivo in sorted((PASTA_DADOS / "producao_mensal").glob("*.xlsx")):
#     tabelas.append(pd.read_excel(arquivo))

# producao = pd.concat(tabelas, ignore_index=True)
# print(f"{len(tabelas)} arquivos, {len(producao)} ordens de produção")

#%%
# ETAPA 2 - CONFERIR E TRATAR OS DADOS
# Antes de analisar, sempre verifique vazios e duplicados
# ...

#%%
# print("Vazios por coluna:")
# print(producao.isna().sum())
# print("Duplicados:", producao.duplicated().sum())

# producao["motivo_parada"] = producao["motivo_parada"].fillna("Sem parada")

#%%
# ETAPA 3 - JUNTAR COM OS CADASTROS (merge)
# produtos.csv -> custo por kg | unidades.xlsx -> gerente e meta mensal
# ...

#%%
# produtos = pd.read_csv(PASTA_DADOS / "produtos.csv", sep=";", decimal=",")
# unidades = pd.read_excel(PASTA_DADOS / "unidades.xlsx")

# producao = producao.merge(produtos, on="produto", how="left")
# producao = producao.merge(unidades[["unidade", "gerente", "meta_mensal_kg"]], on="unidade", how="left")
# producao["gerente"] = producao["gerente"].fillna("Sem cadastro")

#%%
# ETAPA 4 - COLUNAS CALCULADAS
# ...

#%%
# producao["mes"] = producao["data"].dt.month
# producao["custo_producao"] = producao["qtd_produzida_kg"] * producao["custo_kg"]
# producao["custo_refugo"] = producao["qtd_refugo_kg"] * producao["custo_kg"]

#%%
# ETAPA 5 - INDICADORES GERAIS
# ...

#%%
# total_planejado = producao["qtd_planejada_kg"].sum()
# total_produzido = producao["qtd_produzida_kg"].sum()
# total_refugo = producao["qtd_refugo_kg"].sum()

# indicadores = {
#     "Produção total (t)": formatar_numero(total_produzido / 1000, 1),
#     "Eficiência geral": formatar_pct(total_produzido / total_planejado),
#     "Refugo": formatar_pct(total_refugo / total_produzido),
#     "Horas paradas": formatar_numero(producao["horas_paradas"].sum(), 1),
#     "Custo de produção": formatar_moeda(producao["custo_producao"].sum()),
#     "Perda com refugo": formatar_moeda(producao["custo_refugo"].sum()),
#     "Nº de ordens": len(producao),
# }
# resumo = pd.DataFrame({"Indicador": indicadores.keys(), "Valor": indicadores.values()})
# print(resumo)

#%%
# ETAPA 6 - META x REALIZADO POR UNIDADE (groupby + merge)
# A meta do cadastro é mensal; a meta anual é a meta mensal x 12
# ...

#%%
# por_unidade = producao.groupby("unidade").agg(
#     ordens=("id_ordem", "count"),
#     planejado_kg=("qtd_planejada_kg", "sum"),
#     produzido_kg=("qtd_produzida_kg", "sum"),
#     refugo_kg=("qtd_refugo_kg", "sum"),
#     horas_paradas=("horas_paradas", "sum"),
#     custo_producao=("custo_producao", "sum"),
# ).reset_index()

# por_unidade = por_unidade.merge(unidades[["unidade", "gerente", "meta_mensal_kg"]], on="unidade", how="left")
# por_unidade["gerente"] = por_unidade["gerente"].fillna("Sem cadastro")
# por_unidade["eficiencia_%"] = (por_unidade["produzido_kg"] / por_unidade["planejado_kg"] * 100).round(1)
# por_unidade["refugo_%"] = (por_unidade["refugo_kg"] / por_unidade["produzido_kg"] * 100).round(1)
# por_unidade["meta_anual_kg"] = por_unidade["meta_mensal_kg"] * 12
# por_unidade["atingimento_%"] = (por_unidade["produzido_kg"] / por_unidade["meta_anual_kg"] * 100).round(1)
# por_unidade = por_unidade.sort_values("produzido_kg", ascending=False)

# print(por_unidade)

#%%
# UNIDADES ABAIXO DE 90% DA META
# ...

#%%
# abaixo_meta = por_unidade[por_unidade["atingimento_%"] < 90]
# print(abaixo_meta[["unidade", "gerente", "atingimento_%"]])

#%%
# ETAPA 7 - OUTRAS VISÕES: PRODUTOS, TURNOS, PARADAS E MÊS A MÊS
# ...

#%%
# por_produto = producao.groupby(["produto", "categoria"])[["qtd_produzida_kg", "qtd_refugo_kg", "custo_refugo"]].sum().reset_index()
# por_produto["refugo_%"] = (por_produto["qtd_refugo_kg"] / por_produto["qtd_produzida_kg"] * 100).round(1)
# por_produto = por_produto.sort_values("refugo_%", ascending=False)

# por_turno = producao.groupby("turno")[["qtd_planejada_kg", "qtd_produzida_kg", "qtd_refugo_kg"]].sum()
# por_turno["eficiencia_%"] = (por_turno["qtd_produzida_kg"] / por_turno["qtd_planejada_kg"] * 100).round(1)
# por_turno["refugo_%"] = (por_turno["qtd_refugo_kg"] / por_turno["qtd_produzida_kg"] * 100).round(1)
# por_turno = por_turno.reset_index()

# paradas = (
#     producao[producao["horas_paradas"] > 0]
#     .groupby("motivo_parada")
#     .agg(ocorrencias=("id_ordem", "count"), horas=("horas_paradas", "sum"))
#     .sort_values("horas", ascending=False)
#     .reset_index()
# )

# mensal = producao.pivot_table(index="mes", columns="unidade", values="qtd_produzida_kg", aggfunc="sum", fill_value=0)

# print(por_produto)
# print(por_turno)
# print(paradas)

#%%
# ETAPA 8 - RELATÓRIO EM EXCEL COM VÁRIAS ABAS
# ...

#%%
# arquivo_relatorio = PASTA_SAIDA / "fechamento_producao_2025.xlsx"

# with pd.ExcelWriter(arquivo_relatorio, engine="openpyxl") as writer:
#     resumo.to_excel(writer, sheet_name="Resumo", index=False)
#     por_unidade.to_excel(writer, sheet_name="Por Unidade", index=False)
#     por_produto.to_excel(writer, sheet_name="Por Produto", index=False)
#     por_turno.to_excel(writer, sheet_name="Por Turno", index=False)
#     paradas.to_excel(writer, sheet_name="Paradas", index=False)
#     mensal.reset_index().to_excel(writer, sheet_name="Mensal", index=False)
#     producao.to_excel(writer, sheet_name="Base", index=False)

#     for aba in writer.sheets.values():
#         for coluna in aba.columns:
#             aba.column_dimensions[coluna[0].column_letter].width = 18

# print("Relatório salvo:", arquivo_relatorio.name)

#%%
# ETAPA 9 - GRÁFICO: PRODUÇÃO MENSAL POR UNIDADE (em toneladas)
# ...

#%%
# (mensal / 1000).plot(kind="line", marker="o", figsize=(10, 5))
# plt.title("Produção Mensal por Unidade - 2025")
# plt.xlabel("Mês")
# plt.ylabel("Produção (t)")
# plt.xticks(range(1, 13))
# plt.grid(True, alpha=0.3)
# plt.legend(title="Unidade")
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_mensal_unidades.png")
# plt.show()

#%%
# ETAPA 10 - RESUMO EXECUTIVO EM TEXTO
# Montamos uma lista de linhas e juntamos com "\n" (quebra de linha)
# ...

#%%
# linhas = [
#     f"RESUMO EXECUTIVO - FECHAMENTO DA PRODUÇÃO 2025 (gerado em {date.today():%d/%m/%Y})",
#     "",
# ]
# for indicador, valor in indicadores.items():
#     linhas.append(f"{indicador:<20} {valor}")

# linhas.append("")
# linhas.append("ATINGIMENTO DA META POR UNIDADE:")
# for _, linha in por_unidade.iterrows():
#     if pd.isna(linha["atingimento_%"]):
#         linhas.append(f"  - {linha['unidade']}: sem meta cadastrada")
#     else:
#         linhas.append(f"  - {linha['unidade']}: {formatar_numero(linha['atingimento_%'], 1)}% da meta")

# linhas.append("")
# linhas.append("PONTOS DE ATENÇÃO:")
# for _, linha in abaixo_meta.iterrows():
#     linhas.append(f"  - {linha['unidade']} abaixo de 90% da meta (gerente: {linha['gerente']})")
# pior_produto = por_produto.iloc[0]
# linhas.append(f"  - Maior refugo: {pior_produto['produto']} ({formatar_numero(pior_produto['refugo_%'], 1)}%)")
# pior_turno = por_turno.sort_values("eficiencia_%").iloc[0]
# linhas.append(f"  - Turno com menor eficiência: {pior_turno['turno']} ({formatar_numero(pior_turno['eficiencia_%'], 1)}%)")
# linhas.append(f"  - Principal motivo de parada: {paradas.iloc[0]['motivo_parada']} ({formatar_numero(paradas.iloc[0]['horas'], 1)} h)")

# texto_resumo = "\n".join(linhas)
# print(texto_resumo)

#%%
# ETAPA 11 - SALVANDO O RESUMO EM UM ARQUIVO .txt
# ...

#%%
# (PASTA_SAIDA / "resumo_executivo.txt").write_text(texto_resumo, encoding="utf-8")

# duracao = time.time() - inicio
# print(f"Fechamento concluído em {duracao:.1f} segundos! Arquivos em: {PASTA_SAIDA}")
