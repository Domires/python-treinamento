#%%
# LENDO OS DADOS DO CSV
# O CSV é um arquivo de texto onde cada linha é um registro e as colunas são separadas por um caractere (aqui, o ponto e vírgula)
# Vamos usar o pandas para ler o arquivo (veremos o pandas com mais detalhes no módulo 4)

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES
# pip install pandas
# ...

#%%
from pathlib import Path
import pandas as pd

PASTA = Path(__file__).parent

#%%
# LENDO O CSV
# sep=";"   -> as colunas são separadas por ponto e vírgula
# dtype=str -> lê tudo como texto (assim "0001" não vira 1, além disso os valores obtidos pelo robô precisam ser do tipo str)
mostrar_animacao("csv_para_tabela")
# ...

#%%
tabela = pd.read_csv(PASTA / "produtos.csv", sep=";", dtype=str)
print(tabela)

#%%
# CÉLULAS VAZIAS
# Células vazias viram NaN ("Not a Number"). Para o robô, é melhor transformá-las em texto vazio
# ...

#%%
tabela = tabela.fillna("")
display(tabela)

#%%
# INFORMAÇÕES BÁSICAS
# ...

#%%
# print(len(tabela), "linhas")
# print(list(tabela.columns))

#%%
# PERCORRENDO LINHA POR LINHA
# iterrows() devolve, a cada volta, o índice da linha e a linha (que funciona como um dicionário)
mostrar_animacao("iterrows_linhas")
# ...

#%%
# for indice, linha in tabela.iterrows():
#     print(linha["codigo_material"], "-", linha["nome_material"])

#%%
# ALTERNATIVA SEM PANDAS: biblioteca csv (já vem com o Python)
# DictReader lê cada linha como um dicionário
# encoding="utf-8-sig" ignora o caractere invisível (BOM) que o Excel coloca no início do arquivo
# ...

#%%
# import csv

# with open(PASTA / "produtos.csv", encoding="utf-8-sig") as arquivo:
#     for linha in csv.DictReader(arquivo, delimiter=";"):
#         print(linha["codigo_material"], "-", linha["nome_material"])
