#%%
# EXCLUINDO UM PRODUTO (DELETE)

#%%
from animacoes import mostrar_animacao

#%%
# 1) LOGIN
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
# 2) DESCOBRINDO O ID DO PRODUTO
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers, params={"codigo_material": "MAT-9999"})
# encontrados = resposta.json()

# if encontrados:
#     id_produto = encontrados[0]["id"]
#     print("ID do produto:", id_produto)
# else:
#     print("Produto MAT-9999 não encontrado. Rode a aula 05 primeiro.")

#%%
# 3) EXCLUINDO
# A resposta 204 não tem conteúdo (por isso não usamos o .json() aqui)
mostrar_animacao("delete_produto")
# ...

#%%
# resposta = requests.delete(f"{BASE_URL}/api/produtos/{id_produto}", headers=headers)
# print("Status:", resposta.status_code)   # 204 = excluído

#%%
# 4) CONFERINDO: AGORA O PRODUTO NÃO EXISTE MAIS (404)
# ...

#%%
# resposta = requests.get(f"{BASE_URL}/api/produtos/{id_produto}", headers=headers)
# print("Status:", resposta.status_code)
# print(resposta.json())

#%%
# 5) EXCLUINDO VÁRIOS PRODUTOS DE UMA VEZ
# Exemplo: apagar todos os produtos de teste (código começando com "MAT-99")
# CUIDADO: exclusão não tem volta!
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers, params={"codigo_material": "MAT-99"})

# for produto in resposta.json():
#     resposta = requests.delete(f"{BASE_URL}/api/produtos/{produto['id']}", headers=headers)
#     print(produto["codigo_material"], "->", resposta.status_code)
