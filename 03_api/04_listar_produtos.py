#%%
# LISTANDO E CONSULTANDO PRODUTOS (GET)

#%%
from animacoes import mostrar_animacao

#%%
# 1) LOGIN PARA PEGAR O TOKEN
# O token vai no cabeçalho (header) de todas as requisições de produtos
# ...

#%%
# import requests

# BASE_URL = "http://127.0.0.1:8000"

# resposta = requests.post(
#     BASE_URL + "/api/auth/login",
#     json={"usuario": "treinamento", "senha": "12345678"},
# )
# token = resposta.json()["access_token"]
# headers = {"Authorization": "Bearer " + token}

#%%
# 2) BUSCANDO TODOS OS PRODUTOS
# A resposta é uma LISTA de dicionários (um para cada produto)
mostrar_animacao("get_listar")
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers)

# print("Status:", resposta.status_code)
# produtos = resposta.json()
# print(f"{len(produtos)} produtos encontrados")

#%%
# 3) PERCORRENDO A LISTA
# ...

#%%
# for produto in produtos:
#     print(produto["id"], "-", produto["nome_material"], "-", produto["quantidade"], produto["unidade_medida"])

#%%
# 4) FILTRANDO COM PARÂMETROS
# A API aceita os filtros: codigo_material, lote e fabrica (busca por "contém")
# O requests monta a URL: /api/produtos?fabrica=Campinas
# ...

#%%
# filtros = {"fabrica": "Campinas"}

# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers, params=filtros)
# print(resposta.url)

# for produto in resposta.json():
#     print(produto["id"], "-", produto["fabrica"], "-", produto["nome_material"])

#%%
# 5) CONSULTANDO UM PRODUTO PELO ID
# O ID vai no final da rota: /api/produtos/{id}
mostrar_animacao("get_por_id")
# ...

#%%
# if produtos:
#     id_produto = produtos[0]["id"]

#     resposta = requests.get(f"{BASE_URL}/api/produtos/{id_produto}", headers=headers)
#     print("Status:", resposta.status_code)
#     print(resposta.json())

#%%
# 6) PRODUTO QUE NÃO EXISTE: 404
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos/999999", headers=headers)
# print("Status:", resposta.status_code)
# print(resposta.json())

#%%
# 7) SEM TOKEN: 401
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos")
# print("Status:", resposta.status_code)
# print(resposta.json())
