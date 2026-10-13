#%%
# CADASTRANDO TODOS OS PRODUTOS DO CSV PELA API

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES
# ...

#%%
# import time
# from pathlib import Path

# import pandas as pd
# import requests

# BASE_URL = "http://127.0.0.1:8000"
# PASTA = Path(__file__).parent

#%%
# 1) LOGIN
# ...

#%%
# resposta = requests.post(
#     BASE_URL + "/api/auth/login",
#     json={"usuario": "treinamento", "senha": "12345678"},
# )
# token = resposta.json()["access_token"]
# headers = {"Authorization": "Bearer " + token}

#%%
# 2) LENDO O CSV
# ...

#%%
# tabela = pd.read_csv(PASTA / "produtos.csv", sep=";", dtype=str)
# tabela = tabela.fillna("")   # células vazias viram texto vazio
# print(tabela)

#%%
# 3) CONVERTENDO AS DATAS
# No CSV estão como DIA/MÊS/ANO, mas a API quer ANO-MÊS-DIA
# pd.to_datetime lê o texto como data e .dt.strftime escreve no formato desejado
# ...

#%%
# tabela["data_producao"] = pd.to_datetime(tabela["data_producao"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")
# tabela["data_validade"] = pd.to_datetime(tabela["data_validade"], format="%d/%m/%Y").dt.strftime("%Y-%m-%d")

# print(tabela[["codigo_material", "data_producao", "data_validade"]])

#%%
# 4) CADASTRANDO LINHA POR LINHA
# Para cada linha do CSV montamos o dicionário do produto e enviamos com POST
# A quantidade precisa ser número inteiro: int()
mostrar_animacao("csv_para_api")
# ...

#%%
# inicio = time.time()
# resultados = []

# for indice, linha in tabela.iterrows():
#     produto = {
#         "fabrica": linha["fabrica"],
#         "codigo_material": linha["codigo_material"],
#         "nome_material": linha["nome_material"],
#         "lote": linha["lote"],
#         "data_producao": linha["data_producao"],
#         "data_validade": linha["data_validade"],
#         "quantidade": int(linha["quantidade"]),
#         "unidade_medida": linha["unidade_medida"],
#         "observacao": linha["observacao"],
#     }

#     resposta = requests.post(BASE_URL + "/api/produtos", json=produto, headers=headers)
#     print(linha["codigo_material"], "->", resposta.status_code)
#     resultados.append(resposta.status_code)

# print(f"Fim! {len(tabela)} produtos em {time.time() - inicio:.2f} segundos")

#%%
# 5) RESUMO DA EXECUÇÃO
# Guardamos o status de cada linha para saber o que deu certo
# ...

#%%
# tabela["status_api"] = resultados
# print(tabela[["codigo_material", "nome_material", "status_api"]])

# sucesso = (tabela["status_api"] == 201).sum()
# print(f"Cadastrados com sucesso: {sucesso} de {len(tabela)}")

#%%
# 6) CONFERINDO: LISTANDO O QUE FOI CADASTRADO
# Abra também http://127.0.0.1:8000/produtos no navegador
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers)
# for produto in resposta.json():
#     print(produto["id"], "-", produto["codigo_material"], "-", produto["nome_material"])

#%%
# EXTRA: SALVANDO A LISTA DE PRODUTOS DA API EM UM EXCEL
# pd.DataFrame transforma a lista de dicionários (JSON) direto em uma tabela
# ...

#%%
# df_produtos = pd.DataFrame(resposta.json())
# df_produtos.to_excel(PASTA / "produtos_api.xlsx", index=False)
# print(df_produtos.head())
