#%%
# LENDO E EXPLORANDO DADOS

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E CONFIGURAÇÃO
# set_option -> mostra mais colunas no terminal, sem cortar com "..."
# ...

#%%
# from pathlib import Path
# import pandas as pd

# PASTA_DADOS = Path(__file__).parent / "dados"

# pd.set_option("display.max_columns", 20)
# pd.set_option("display.width", 200)

#%%
# LENDO UM EXCEL
mostrar_animacao("ler_arquivos")
# ...

#%%
# producao = pd.read_excel(PASTA_DADOS / "producao.xlsx")
# print(producao)

#%%
# OPÇÕES ÚTEIS DO read_excel
# sheet_name="Nome da Aba" -> lê uma aba específica (padrão: a primeira)
# skiprows=3               -> pula as 3 primeiras linhas (títulos, logos...)
# usecols="A:E"            -> lê só algumas colunas
# ...

#%%
# producao_resumo = pd.read_excel(PASTA_DADOS / "producao.xlsx", sheet_name="Producao", usecols="A:E")
# print(producao_resumo.head())

#%%
# LENDO UM CSV
# Abra o produtos.csv no Bloco de Notas: as colunas são separadas por ; e o decimal usa vírgula (2,35)
# sep=";"          -> separador das colunas (no Brasil é comum o ponto e vírgula)
# decimal=","      -> separador decimal brasileiro
# encoding="utf-8" -> codificação dos acentos (se der erro, tente "latin1")
# ...

#%%
# produtos = pd.read_csv(PASTA_DADOS / "produtos.csv", sep=";", decimal=",", encoding="utf-8")
# print(produtos)

#%%
# PRIMEIRAS E ÚLTIMAS LINHAS
# head(n) -> primeiras n linhas (padrão 5) | tail(n) -> últimas n linhas
# ...

#%%
# print(producao.head())
# print(producao.tail(3))

#%%
# TAMANHO E COLUNAS
# ...

#%%
# print("Formato (linhas, colunas):", producao.shape)
# print("Quantidade de ordens:", len(producao))
# print("Colunas:", list(producao.columns))

#%%
# TIPOS DE DADOS E VALORES VAZIOS
# info() mostra cada coluna, quantos valores preenchidos e o tipo:
#   int64 = inteiro | float64 = decimal | str/object = texto | datetime64 = data
# Repare: motivo_parada tem MENOS valores preenchidos (só existe quando houve parada)
# ...

#%%
# producao.info()

#%%
# TIPO DE CADA COLUNA
# ...

#%%
# print(producao.dtypes)

#%%
# RESUMO ESTATÍSTICO
# describe() calcula contagem, média, desvio padrão, mínimo, quartis e máximo das colunas numéricas
# ...

#%%
# print(producao.describe())

#%%
# CONHECENDO OS VALORES DE UMA COLUNA
# unique()  -> valores diferentes
# nunique() -> quantidade de valores diferentes
# ...

#%%
# print("Unidades:", list(producao["unidade"].unique()))
# print("Quantidade de produtos diferentes:", producao["produto"].nunique())

#%%
# CONTANDO OS VALORES
# value_counts() conta quantas vezes cada valor aparece (como uma tabela dinâmica de contagem)
# ...

#%%
# print(producao["turno"].value_counts())
# print(producao["motivo_parada"].value_counts())

#%%
# LENDO JSON
# O pandas também lê JSON (o formato das APIs)
# Pode ser um arquivo (pd.read_json("arquivo.json")) ou um texto, usando o StringIO
# ...

#%%
# from io import StringIO

# ordens_json = '[{"ordem": "OP-9001", "produzido_kg": 12000}, {"ordem": "OP-9002", "produzido_kg": 9800}]'
# ordens = pd.read_json(StringIO(ordens_json))
# print(ordens)
