#%%
# ALTERANDO UM PRODUTO (PATCH E PUT)

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
# Buscamos pelo código do material usando o filtro (params) e pegamos o ID do primeiro resultado
# Também poderíamos simplesmente escrever o ID: id_produto = 1
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers, params={"codigo_material": "MAT-9999"})
# encontrados = resposta.json()

# if encontrados:
#     id_produto = encontrados[0]["id"]
#     print("ID do produto:", id_produto)
#     print(encontrados[0])
# else:
#     print("Produto MAT-9999 não encontrado. Rode a aula 05 primeiro.")

#%%
# 3) ALTERANDO SÓ A QUANTIDADE (PATCH)
# Com o PATCH enviamos só os campos que queremos mudar
mostrar_animacao("patch_vs_put")
# ...

#%%
# alteracao = {"quantidade": 999}

# resposta = requests.patch(f"{BASE_URL}/api/produtos/{id_produto}", json=alteracao, headers=headers)

# print("Status:", resposta.status_code)   # 200 = alterado
# print("Resposta:", resposta.json())

#%%
# 4) ALTERANDO MAIS DE UM CAMPO (PATCH)
# ...

#%%
# alteracao = {
#     "lote": "L-TESTE-02",
#     "observacao": "Alterado pela API",
# }

# resposta = requests.patch(f"{BASE_URL}/api/produtos/{id_produto}", json=alteracao, headers=headers)
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())

#%%
# 5) ALTERANDO TODOS OS CAMPOS (PUT)
# Com o PUT precisamos enviar o produto COMPLETO (todos os campos obrigatórios)
# Se faltar algum campo, a API devolve 422
# ...

#%%
# produto_completo = {
#     "fabrica": "Fábrica Campinas",
#     "codigo_material": "MAT-9999",
#     "nome_material": "Produto de Teste (atualizado)",
#     "lote": "L-TESTE-03",
#     "data_producao": "2026-10-05",
#     "data_validade": "2027-04-05",
#     "quantidade": 250,
#     "unidade_medida": "L",
#     "observacao": "Atualizado com PUT",
# }

# resposta = requests.put(f"{BASE_URL}/api/produtos/{id_produto}", json=produto_completo, headers=headers)
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())

#%%
# 6) PUT SEM TODOS OS CAMPOS: 422
# ...

#%%
# resposta = requests.put(f"{BASE_URL}/api/produtos/{id_produto}", json={"quantidade": 1}, headers=headers)
# print("Status:", resposta.status_code)

#%%
# 7) DADO INVÁLIDO: 422
# Exemplo: data de validade anterior à data de produção
# ...

#%%
# resposta = requests.patch(
#     f"{BASE_URL}/api/produtos/{id_produto}",
#     json={"data_validade": "2020-01-01"},
#     headers=headers,
# )
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())
