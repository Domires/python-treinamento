#%%
# CADASTRANDO UM PRODUTO (POST)

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
# 2) DADOS DO PRODUTO
# As chaves do dicionário são os campos que a API espera (veja em /docs)
# ATENÇÃO: na API as datas são no formato ANO-MÊS-DIA
# unidade_medida aceita somente: KG, T ou L
# ...

#%%
# produto = {
#     "fabrica": "Fábrica São Paulo",
#     "codigo_material": "MAT-9999",
#     "nome_material": "Produto de Teste",
#     "lote": "L-TESTE",
#     "data_producao": "2026-10-01",
#     "data_validade": "2027-10-01",
#     "quantidade": 100,
#     "unidade_medida": "KG",
#     "observacao": "Cadastrado pela API",
# }

#%%
# 3) ENVIANDO (POST)
# json=produto -> o requests converte o dicionário em JSON e coloca no body
mostrar_animacao("post_cadastro")
# ...

#%%
# resposta = requests.post(BASE_URL + "/api/produtos", json=produto, headers=headers)

# print("Status:", resposta.status_code)   # 201 = cadastrado
# print("Resposta:", resposta.json())

#%%
# 4) A RESPOSTA TRAZ O PRODUTO CADASTRADO, COM O ID GERADO PELO SISTEMA
# ...

#%%
# cadastrado = resposta.json()
# print("ID gerado:", cadastrado["id"])
# print("Criado em:", cadastrado["criado_em"])

#%%
# 5) ENVIANDO DADOS INVÁLIDOS: 422
# A API valida os dados e explica o que está errado
# Aqui: unidade de medida inexistente e data no formato brasileiro
mostrar_animacao("erro_422")
# ...

#%%
# produto_errado = produto.copy()
# produto_errado["unidade_medida"] = "CX"
# produto_errado["data_producao"] = "01/10/2026"

# resposta = requests.post(BASE_URL + "/api/produtos", json=produto_errado, headers=headers)
# print("Status:", resposta.status_code)

# for erro in resposta.json()["detail"]:
#     print(erro["loc"][-1], "->", erro["msg"])

#%%
# 6) VERIFICANDO SE DEU CERTO ANTES DE CONTINUAR
# Boa prática: sempre conferir o status
# ...

#%%
# produto["codigo_material"] = "MAT-9998"
# produto["nome_material"] = "Segundo Produto de Teste"

# resposta = requests.post(BASE_URL + "/api/produtos", json=produto, headers=headers)

# if resposta.status_code == 201:
#     print("Produto cadastrado! ID:", resposta.json()["id"])
# else:
#     print("Falha no cadastro:", resposta.status_code, resposta.text)
