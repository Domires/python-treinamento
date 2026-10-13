#%%
# COLUNAS CALCULADAS

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E LEITURA DOS DADOS
# ...

#%%
# from pathlib import Path
# import pandas as pd

# PASTA_DADOS = Path(__file__).parent / "dados"
# pd.set_option("display.max_columns", 20)
# pd.set_option("display.width", 200)

# producao = pd.read_excel(PASTA_DADOS / "producao.xlsx")

#%%
# CONTAS ENTRE COLUNAS: OS PRINCIPAIS INDICADORES
# eficiência   = produzido / planejado      (quanto do plano foi cumprido)
# refugo (%)   = refugo / produzido          (quanto do que foi produzido foi perdido)
# produção boa = produzido - refugo          (o que realmente pode ser vendido)
# A conta é feita linha a linha, para a tabela inteira
mostrar_animacao("indicadores_colunas")
# ...

#%%
# producao["eficiencia"] = producao["qtd_produzida_kg"] / producao["qtd_planejada_kg"]
# producao["refugo_pct"] = producao["qtd_refugo_kg"] / producao["qtd_produzida_kg"]
# producao["qtd_boa_kg"] = producao["qtd_produzida_kg"] - producao["qtd_refugo_kg"]

# print(producao[["unidade", "qtd_planejada_kg", "qtd_produzida_kg", "eficiencia", "refugo_pct", "qtd_boa_kg"]].head())

#%%
# ARREDONDANDO E MUDANDO A ESCALA
# De kg para toneladas: divide por 1000
# ...

#%%
# producao["eficiencia"] = producao["eficiencia"].round(3)
# producao["refugo_pct"] = producao["refugo_pct"].round(3)
# producao["qtd_produzida_t"] = (producao["qtd_produzida_kg"] / 1000).round(1)

# print(producao[["qtd_produzida_kg", "qtd_produzida_t", "eficiencia", "refugo_pct"]].head())

#%%
# COLUNA DE VERDADEIRO / FALSO
# Uma comparação gera True ou False para cada linha
# ...

#%%
# producao["atingiu_plano"] = producao["qtd_produzida_kg"] >= producao["qtd_planejada_kg"]
# print(producao["atingiu_plano"].value_counts())

#%%
# COLUNA COM CONDIÇÃO SIMPLES (SE ... ENTÃO ... SENÃO)
# Criamos a coluna com um valor padrão e usamos .loc para "marcar" as linhas que atendem à condição
mostrar_animacao("loc_condicao")
# ...

#%%
# producao["faixa_eficiencia"] = "Baixa"
# producao.loc[producao["eficiencia"] >= 0.85, "faixa_eficiencia"] = "Média"
# producao.loc[producao["eficiencia"] >= 0.95, "faixa_eficiencia"] = "Alta"

# print(producao["faixa_eficiencia"].value_counts())

#%%
# COLUNA COM CONDIÇÃO USANDO UMA FUNÇÃO (apply)
# Lembra das funções dos fundamentos? Podemos aplicá-las a cada valor da coluna
# ...

#%%
# def classificar_parada(horas):
#     if horas == 0:
#         return "Sem parada"
#     elif horas <= 2:
#         return "Parada curta"
#     else:
#         return "Parada longa"

# producao["tipo_parada"] = producao["horas_paradas"].apply(classificar_parada)
# print(producao["tipo_parada"].value_counts())

#%%
# TRABALHANDO COM DATAS (.dt)
# year, month, day, quarter (trimestre), dayofweek (0 = segunda ... 6 = domingo)
# strftime -> data como texto no formato desejado
mostrar_animacao("datas_dt")
# ...

#%%
# producao["ano"] = producao["data"].dt.year
# producao["mes"] = producao["data"].dt.month
# producao["trimestre"] = producao["data"].dt.quarter
# producao["dia_semana"] = producao["data"].dt.dayofweek
# producao["ano_mes"] = producao["data"].dt.strftime("%Y-%m")   # ótimo para agrupar por mês

# print(producao[["data", "ano", "mes", "trimestre", "dia_semana", "ano_mes"]].head())

#%%
# MAPEANDO VALORES COM UM DICIONÁRIO (.map)
# Troca cada valor da coluna pelo valor correspondente no dicionário
# ...

#%%
# nomes_dias = {0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo"}
# producao["dia_semana"] = producao["dia_semana"].map(nomes_dias)

# horarios = {"A": "06h às 14h", "B": "14h às 22h", "C": "22h às 06h"}
# producao["horario_turno"] = producao["turno"].map(horarios)

# print(producao[["data", "dia_semana", "turno", "horario_turno"]].head())

#%%
# COLUNAS DE TEXTO COMBINADAS
# ...

#%%
# producao["descricao"] = producao["unidade"] + " - " + producao["produto"]
# print(producao["descricao"].head())

#%%
# REMOVENDO COLUNAS QUE NÃO PRECISAMOS MAIS
# ...

#%%
# producao = producao.drop(columns=["ano", "descricao"])
# print(list(producao.columns))
