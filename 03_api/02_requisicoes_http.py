#%%
# REQUISIÇÕES HTTP COM A BIBLIOTECA requests
# ANTES DE RODAR: deixe o site rodando em outro terminal (pasta site_treinamento):
#   python main.py


#%%
from animacoes import mostrar_animacao

#%%
# O QUE É UMA API?
# API (Application Programming Interface) é uma "porta de entrada" que um sistema oferece para OUTROS PROGRAMAS conversarem com ele
# Com o pyautogui, o robô usa a tela como uma pessoa. Com a API, o programa conversa direto com o sistema:
#   - muito mais rápido
#   - não depende da tela, do mouse ou da resolução
#   - menos sujeito a erros
#
# Funciona como um restaurante:
#   - você (cliente) faz um PEDIDO (requisição / request)
#   - o garçom (API) leva o pedido para a cozinha (servidor)
#   - e traz de volta a RESPOSTA (response)
mostrar_animacao("request_response")

#%%
# PARTES DE UMA REQUISIÇÃO
# URL     -> o endereço:  http://127.0.0.1:8000/api/produtos
#              base (servidor): http://127.0.0.1:8000
#              rota (endpoint): /api/produtos
# Método  -> o que queremos fazer (GET, POST, PUT, PATCH, DELETE)
# Headers -> informações extras (cabeçalho), como o token de acesso
# Body    -> os dados enviados (normalmente em JSON), usado no POST, PUT e PATCH
# Params  -> filtros enviados na URL: /api/produtos?fabrica=Recife&lote=L2026

#%%
# VERBOS (MÉTODOS) HTTP
# GET    -> consultar / listar         (como abrir uma planilha para ler)
# POST   -> cadastrar algo novo        (inserir uma linha)
# PUT    -> atualizar TODOS os campos  (reescrever a linha inteira)
# PATCH  -> atualizar ALGUNS campos    (alterar algumas células)
# DELETE -> excluir                    (apagar a linha)
mostrar_animacao("verbos_http")

#%%
# CÓDIGOS DE STATUS (A RESPOSTA DIZ SE DEU CERTO)
# 2xx -> sucesso
#   200 OK          -> deu certo
#   201 Created     -> cadastrado
#   204 No Content  -> deu certo e não há conteúdo de retorno (ex: excluído)
# 4xx -> erro de quem fez o pedido (nós)
#   400 Bad Request  -> pedido mal feito
#   401 Unauthorized -> sem token, token inválido ou login errado
#   403 Forbidden    -> autenticado, mas sem permissão
#   404 Not Found    -> não encontrado
#   422 Unprocessable Entity -> algum dado foi enviado errado
# 5xx -> erro do servidor
#   500 Internal Server Error
mostrar_animacao("status_codes")

#%%
# AUTENTICAÇÃO x AUTORIZAÇÃO x TOKEN
# Autenticação -> provar QUEM você é (usuário e senha)
# Autorização  -> o que você PODE fazer depois de autenticado
# Token        -> um "crachá" temporário que a API entrega após o login
#   - enviamos o token no header de cada requisição: Authorization: Bearer <token>
#   - assim não precisamos mandar usuário e senha toda hora
#   - o token expira (neste site, em 8 horas)
mostrar_animacao("token_autenticacao")

#%%
# DOCUMENTAÇÃO DA API
# Toda API tem uma documentação que diz quais rotas existem e o que enviar
# A do nosso site fica em: http://127.0.0.1:8000/docs (Swagger)
# Lá dá para testar cada rota direto pelo navegador

#%%
# INSTALAÇÃO E IMPORTAÇÃO
# pip install requests
# ...

#%%
# import requests

# BASE_URL = "http://127.0.0.1:8000"

#%%
# PRIMEIRA REQUISIÇÃO (GET)
# requests.get(url) -> faz a requisição e devolve a resposta
# ...

#%%
# resposta = requests.get(BASE_URL + "/docs")
# print(resposta.status_code)

#%%
# FORMA GENÉRICA: requests.request(método, url, argumentos)
# requests.get, requests.post, requests.put, requests.patch e requests.delete são atalhos para ela
# ...

#%%
# resposta = requests.request("GET", BASE_URL + "/docs")
# print(resposta.status_code)

#%%
# O QUE VEM NA RESPOSTA
# .status_code -> código de status (200, 404...)
# .ok          -> True se o status for de sucesso (menor que 400)
# .headers     -> cabeçalhos da resposta
# .text        -> conteúdo como texto
# .json()      -> conteúdo convertido de JSON para Python (dicionário ou lista)
# ...

#%%
# resposta = requests.get(BASE_URL + "/openapi.json")
# print(resposta.status_code)
# print(resposta.ok)
# print(resposta.headers["content-type"])
# print(resposta.text[:100])

# documentacao = resposta.json()
# print(documentacao["info"]["title"])

#%%
# LISTANDO AS ROTAS DA API (lidas da própria documentação)
# ...

#%%
# for rota, metodos in documentacao["paths"].items():
#     print(rota, "->", [metodo.upper() for metodo in metodos])

#%%
# AUTORIZAÇÃO NA PRÁTICA
# Sem token, a API recusa o pedido: 401 Unauthorized
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos")
# print(resposta.status_code)
# print(resposta.json())

#%%
# AUTENTICAÇÃO: FAZENDO LOGIN PARA RECEBER O TOKEN
# Os dados vão no body em formato JSON: usamos o argumento json= (o requests converte o dicionário automaticamente)
# ...

#%%
# resposta = requests.post(
#     BASE_URL + "/api/auth/login",
#     json={"usuario": "treinamento", "senha": "12345678"},
# )
# print(resposta.status_code)
# token = resposta.json()["access_token"]
# print(token)

#%%
# ENVIANDO O TOKEN NO HEADER
# Agora a API autoriza o acesso: 200 OK
# ...

#%%
# headers = {"Authorization": f"Bearer {token}"}

# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers)
# print(resposta.status_code)
# print(resposta.json())

#%%
# PARÂMETROS (FILTROS NA URL)
# Podemos escrever na URL (?fabrica=Recife) ou usar o argumento params= (mais organizado)
mostrar_animacao("parametros_url")
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/produtos", headers=headers, params={"fabrica": "Recife"})
# print(resposta.url)
# print(resposta.json())

#%%
# ROTA QUE NÃO EXISTE: 404 Not Found
# ...

#%%
# resposta = requests.get(BASE_URL + "/api/rota-que-nao-existe", headers=headers)
# print(resposta.status_code)

#%%
# TRATANDO ERROS
# raise_for_status() -> gera um erro se o status for 4xx ou 5xx
# timeout=10         -> desiste se o servidor não responder em 10 segundos
# ConnectionError    -> o servidor está desligado ou o endereço está errado
# ...

#%%
# try:
#     resposta = requests.get(BASE_URL + "/api/produtos", timeout=10)
#     resposta.raise_for_status()
# except requests.exceptions.HTTPError as erro:
#     print("Erro HTTP:", erro)
# except requests.exceptions.ConnectionError:
#     print("Não foi possível conectar. O site está rodando? (python main.py)")
