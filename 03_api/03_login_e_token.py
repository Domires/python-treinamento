#%%
# FAZENDO LOGIN NA API E PEGANDO O TOKEN

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÃO E ENDEREÇO DA API
# ...

#%%
# import requests

# BASE_URL = "http://127.0.0.1:8000"

#%%
# DADOS DE LOGIN
# A documentação (/docs) diz que a rota POST /api/auth/login espera um JSON com usuario e senha
# ...

#%%
# url = BASE_URL + "/api/auth/login"

# dados = {
#     "usuario": "treinamento",
#     "senha": "12345678",
# }

#%%
# FAZENDO O LOGIN (POST)
mostrar_animacao("login_post_token")
# ...

#%%
# resposta = requests.post(url, json=dados)

# print("Status:", resposta.status_code)   # 200 = deu certo
# print("Resposta:", resposta.json())

#%%
# PEGANDO O TOKEN DA RESPOSTA
# A resposta é um dicionário: o token fica na chave "access_token"
# ...

#%%
# token = resposta.json()["access_token"]
# print("Token:", token)
# print("Expira em:", resposta.json()["expira_em"])

#%%
# LOGIN COM SENHA ERRADA: 401
# ...

#%%
# resposta = requests.post(url, json={"usuario": "treinamento", "senha": "errada"})
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())

#%%
# VALIDANDO O TOKEN
# A rota GET /api/auth/me devolve quem é o dono do token
# O token vai no cabeçalho (header) da requisição, no formato "Bearer <token>"
# ...

#%%
# headers = {"Authorization": "Bearer " + token}

# resposta = requests.get(BASE_URL + "/api/auth/me", headers=headers)
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())

#%%
# TOKEN INVÁLIDO: 401
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/auth/me", headers={"Authorization": "Bearer token-falso"})
# print("Status:", resposta.status_code)
# print("Resposta:", resposta.json())

#%%
# CRIANDO UMA FUNÇÃO DE LOGIN
# Vamos usar esta função no começo de todas as próximas aulas
# ...

#%%
# def fazer_login():
#     """Faz login na API e devolve o header com o token."""
#     resposta = requests.post(
#         BASE_URL + "/api/auth/login",
#         json={"usuario": "treinamento", "senha": "12345678"},
#     )
#     resposta.raise_for_status()   # para o programa se o login falhar
#     token = resposta.json()["access_token"]
#     return {"Authorization": "Bearer " + token}

# headers = fazer_login()
# print(headers)
