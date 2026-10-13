#%%
# INTRODUÇÃO AO PANDAS
# O pandas é a biblioteca mais usada na comunidade python para trabalhar com tabelas
#   - processa milhões de linhas
#   - lê e escreve Excel, CSV, bancos de dados, JSON de APIs e etc...

#%%
from animacoes import mostrar_animacao

#%%
# INSTALAÇÃO E IMPORTAÇÃO
# No terminal: pip install pandas openpyxl matplotlib
# "pd" é o apelido padrão usado por todo mundo
# ...

#%%
# import pandas as pd

#%%
# VERIFICAR VERSÃO
# ...

#%%
# print(pd.__version__)

#%%
# CRIANDO UMA TABELA A PARTIR DE UM DICIONÁRIO
# Cada chave vira o nome de uma coluna; cada lista, os valores da coluna
mostrar_animacao("dict_para_dataframe")
# ...

#%%
# dataset = {
#     "produto": ["Produto_A", "Produto_B", "Produto_C", "Produto_D", "Produto_E"],
#     "categoria": ["Granulado", "Granulado", "Líquido", "Líquido", "Líquido"],
#     "custo_kg": [2.35, 2.80, 4.10, 3.65, 5.20],
#     "estoque_kg": [12000, 8500, 3000, 15000, 700],
# }

# df_produtos = pd.DataFrame(dataset)   # "df" é o nome mais comum para um DataFrame
# print(df_produtos)

#%%
# EXIBINDO DF
# No jupyter usamos a função display() para mostrar a tabela formatada
# Escrever só o nome da variável na última linha da célula também funciona
# ...

#%%
# display(df_produtos)

#%%
# VOCABULÁRIO
# DataFrame -> a tabela inteira (uma aba do Excel)
# Series    -> uma coluna da tabela
# index     -> o "número da linha" (à esquerda)
# columns   -> os nomes das colunas
mostrar_animacao("anatomia_dataframe")
# ...

#%%
# print(df_produtos.index)
# print(df_produtos.columns)

#%%
# UMA COLUNA = UMA SERIES
# ...

#%%
# print(df_produtos["estoque_kg"])
# print(type(df_produtos["estoque_kg"]))

#%%
# OPERAÇÕES EM COLUNAS INTEIRAS, SEM PRECISAR DE for!
# ...

#%%
# print("Estoque total (kg):", df_produtos["estoque_kg"].sum())
# print("Custo médio (R$/kg):", df_produtos["custo_kg"].mean())
# print("Maior estoque (kg):", df_produtos["estoque_kg"].max())

#%%
# CRIANDO UMA NOVA COLUNA CALCULADA
# Igual a arrastar uma fórmula no Excel: a conta é feita para TODAS as linhas
mostrar_animacao("coluna_calculada")
# ...

#%%
# df_produtos["valor_estoque"] = df_produtos["custo_kg"] * df_produtos["estoque_kg"]
# print(df_produtos)

#%%
# INFORMAÇÕES BÁSICAS
# shape -> (linhas, colunas)
# ...

#%%
# print("Linhas e colunas:", df_produtos.shape)
# print("Nomes das colunas:", list(df_produtos.columns))
# print("Valor total em estoque: R$", df_produtos["valor_estoque"].sum())

#%%
# COMPARAÇÃO: SEM pandas x COM pandas
# Nos fundamentos, para somar o valor em estoque, faríamos:
#   total = 0
#   for i in range(len(custos)):
#       total += custos[i] * estoques[i]
# Com pandas:
#   (df["custo_kg"] * df["estoque_kg"]).sum()
# Mais curto, mais legível e muito mais rápido em bases grandes
