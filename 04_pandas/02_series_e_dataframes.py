#%%
# SERIES E DATAFRAMES

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÃO
# ...

#%%
# import pandas as pd

#%%
# CRIANDO UMA SERIES A PARTIR DE UMA LISTA
# O pandas cria o índice automaticamente (0, 1, 2...)
# ...

#%%
# producao = [18500, 21300, 19800]

# serie = pd.Series(producao)
# print(serie)

#%%
# ACESSANDO UM VALOR PELO ÍNDICE
# ...

#%%
# print(serie[0])

#%%
# NOMEANDO OS RÓTULOS
# Podemos nomear os rótulos passando uma lista para o parâmetro index
# ...

#%%
# serie = pd.Series(producao, index=["turno_A", "turno_B", "turno_C"])
# print(serie)
# print(serie["turno_B"])

#%%
# SERIES A PARTIR DE UM DICIONÁRIO
# As chaves viram o índice
# ...

#%%
# producao_dia = {"segunda": 42000, "terça": 38000, "quarta": 39000}

# serie_producao = pd.Series(producao_dia)
# print(serie_producao)

#%%
# OPERAÇÕES COM SERIES
# A conta é aplicada em todos os valores de uma vez
# ...

#%%
# print(serie_producao / 1000)   # de kg para toneladas
# print(serie_producao.sum(), serie_producao.mean(), serie_producao.max())
# print(serie_producao[serie_producao > 38500])   # filtro

#%%
# DATAFRAME A PARTIR DE UM DICIONÁRIO DE LISTAS
# Cada chave é uma coluna
# ...

#%%
# dados = {
#     "planejado_kg": [20000, 18000, 15000],
#     "produzido_kg": [18500, 18300, 12100],
# }

# df = pd.DataFrame(dados)
# print(df)

#%%
# DATAFRAME A PARTIR DE UMA LISTA DE DICIONÁRIOS
# Cada dicionário é uma linha (é o formato que recebemos das APIs!)
# ...

#%%
# ordens = [
#     {"ordem": "OP-0001", "unidade": "Unidade_A", "produzido_kg": 18500},
#     {"ordem": "OP-0002", "unidade": "Unidade_B", "produzido_kg": 21300},
#     {"ordem": "OP-0003", "unidade": "Unidade_C", "produzido_kg": 9800},
# ]

# df_ordens = pd.DataFrame(ordens)
# print(df_ordens)

#%%
# ÍNDICE PERSONALIZADO
# Podemos nomear as linhas com o parâmetro index
# ...

#%%
# df = pd.DataFrame(dados, index=["turno_A", "turno_B", "turno_C"])
# print(df)

#%%
# loc -> ACESSA PELO RÓTULO (nome) DA LINHA
# Uma linha devolve uma Series; uma lista de linhas devolve um DataFrame
mostrar_animacao("loc_iloc")
# ...

#%%
# print(df.loc["turno_A"])
# print(df.loc[["turno_A", "turno_C"]])

#%%
# iloc -> ACESSA PELA POSIÇÃO (número) DA LINHA, começando em 0
# ...

#%%
# print(df.iloc[0])
# print(df.iloc[0:2])

#%%
# ACESSANDO UMA CÉLULA
# df.loc[linha, coluna]  ou  df.iloc[posição_linha, posição_coluna]
# ...

#%%
# print(df.loc["turno_C", "produzido_kg"])
# print(df.iloc[2, 1])

#%%
# DEFININDO UMA COLUNA COMO ÍNDICE
# set_index -> transforma uma coluna em índice | reset_index -> volta o índice para coluna
# ...

#%%
# df_ordens = df_ordens.set_index("ordem")
# print(df_ordens)
# print(df_ordens.loc["OP-0002"])

# df_ordens = df_ordens.reset_index()
# print(df_ordens)

#%%
# CONVERTENDO DE VOLTA PARA PYTHON PURO
# ...

#%%
# print(df_ordens["unidade"].tolist())          # coluna -> lista
# print(df_ordens.to_dict(orient="records"))    # tabela -> lista de dicionários
