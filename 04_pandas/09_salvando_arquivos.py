#%%
# SALVANDO RELATÓRIOS (OUTPUT)
#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E PREPARAÇÃO DOS DADOS
# Os relatórios serão salvos na pasta "relatorios"
# ...

#%%
# from datetime import date
# from pathlib import Path
# import pandas as pd

# PASTA = Path(__file__).parent
# PASTA_DADOS = PASTA / "dados"
# PASTA_SAIDA = PASTA / "relatorios"
# PASTA_SAIDA.mkdir(exist_ok=True)

# producao = pd.read_excel(PASTA_DADOS / "producao.xlsx")
# producao["eficiencia"] = (producao["qtd_produzida_kg"] / producao["qtd_planejada_kg"]).round(3)
# producao["refugo_pct"] = (producao["qtd_refugo_kg"] / producao["qtd_produzida_kg"]).round(3)
# producao["mes"] = producao["data"].dt.month

#%%
# SALVANDO EM EXCEL
# index=False -> não grava a coluna com os números das linhas (quase sempre queremos isso)
# ...

#%%
# producao.to_excel(PASTA_SAIDA / "producao_com_indicadores.xlsx", index=False)

#%%
# SALVANDO EM CSV NO PADRÃO BRASILEIRO (abre direto no Excel em português)
# sep=";" e decimal="," -> padrão brasileiro
# encoding="utf-8-sig"  -> o Excel reconhece os acentos
# ...

#%%
# producao.to_csv(PASTA_SAIDA / "producao_com_indicadores.csv", index=False, sep=";", decimal=",", encoding="utf-8-sig")

#%%
# OUTROS FORMATOS
# to_json -> JSON (para enviar a uma API, por exemplo)
# ...

#%%
# producao.head(3).to_json(PASTA_SAIDA / "amostra.json", orient="records", date_format="iso", indent=4, force_ascii=False)

#%%
# PREPARANDO AS TABELAS DO RELATÓRIO
# ...

#%%
# por_unidade = producao.groupby("unidade")[["qtd_planejada_kg", "qtd_produzida_kg", "qtd_refugo_kg", "horas_paradas"]].sum()
# por_unidade["eficiencia"] = (por_unidade["qtd_produzida_kg"] / por_unidade["qtd_planejada_kg"]).round(3)
# por_unidade = por_unidade.sort_values("qtd_produzida_kg", ascending=False).reset_index()

# por_produto = producao.groupby("produto")[["qtd_produzida_kg", "qtd_refugo_kg"]].sum()
# por_produto["refugo_pct"] = (por_produto["qtd_refugo_kg"] / por_produto["qtd_produzida_kg"]).round(3)
# por_produto = por_produto.reset_index()

# por_mes = producao.pivot_table(index="mes", columns="unidade", values="qtd_produzida_kg",
#                                aggfunc="sum", fill_value=0).reset_index()

#%%
# RELATÓRIO COM VÁRIAS ABAS
# ExcelWriter permite escrever várias abas no MESMO arquivo
# Nome do arquivo com a data de hoje (ex: relatorio_producao_2026-10-12.xlsx)
mostrar_animacao("excel_abas")
# ...

#%%
# nome_arquivo = PASTA_SAIDA / f"relatorio_producao_{date.today():%Y-%m-%d}.xlsx"

# with pd.ExcelWriter(nome_arquivo, engine="openpyxl") as writer:
#     por_unidade.to_excel(writer, sheet_name="Por Unidade", index=False)
#     por_produto.to_excel(writer, sheet_name="Por Produto", index=False)
#     por_mes.to_excel(writer, sheet_name="Mensal por Unidade", index=False)
#     producao.to_excel(writer, sheet_name="Base Completa", index=False)

#     # Ajustando a largura das colunas de todas as abas
#     for aba in writer.sheets.values():
#         for coluna in aba.columns:
#             aba.column_dimensions[coluna[0].column_letter].width = 18

# print(f"Relatório salvo em: {nome_arquivo.name}")

#%%
# UM ARQUIVO POR UNIDADE (automação de verdade!)
# Imagine enviar para cada gerente só os dados da unidade dele
# Manualmente: filtrar, copiar, colar, salvar... 6 vezes. Todo mês
mostrar_animacao("arquivo_por_unidade")
# ...

#%%
# pasta_unidades = PASTA_SAIDA / "por_unidade"
# pasta_unidades.mkdir(exist_ok=True)

# for unidade in producao["unidade"].unique():
#     dados_unidade = producao[producao["unidade"] == unidade]
#     arquivo = pasta_unidades / f"producao_{unidade}.xlsx"
#     dados_unidade.to_excel(arquivo, index=False)
#     print(f"{arquivo.name}: {len(dados_unidade)} ordens")

#%%
# ABRINDO O ARQUIVO GERADO (só no Windows)
# ...

#%%
# import os

# os.startfile(nome_arquivo)
