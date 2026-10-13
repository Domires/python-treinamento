#%%
# JSON (JavaScript Object Notation)
# É o formato de texto que as APIs usam para enviar e receber dados
# Ele é MUITO parecido com os dicionários e listas do Python

#%%
from animacoes import mostrar_animacao

#%%
# COMO É UM JSON
# {
#     "codigo_material": "MAT-0001",
#     "quantidade": 500,
#     "ativo": true,
#     "observacao": null
# }
# Só 3 diferenças para o dicionário do Python:
#   true / false -> True / False
#   null         -> None
#   textos SEMPRE com aspas duplas
mostrar_animacao("json_vs_python")

#%%
# IMPORTAÇÃO
# A biblioteca json já vem com o Python
# ...

#%%
# import json

#%%
# TEXTO JSON -> PYTHON: json.loads()
# É o que fazemos com a RESPOSTA de uma API: transformar o texto em dicionário
# Depois disso, acessamos os valores pela chave, como em qualquer dicionário
mostrar_animacao("dumps_loads")
# ...

#%%
# texto = '{"usuario": "treinamento", "ativo": true, "perfil": null}'

# dados = json.loads(texto)
# print(dados)
# print(type(dados))
# print(dados["usuario"])

#%%
# LISTA DE OBJETOS
# É o formato mais comum de resposta de uma API: uma lista de dicionários
# Percorremos com um for, como nos fundamentos
# ...

#%%
# texto = '[{"id": 1, "nome_material": "Açúcar", "quantidade": 500}, {"id": 2, "nome_material": "Óleo", "quantidade": 1200}]'

# produtos = json.loads(texto)
# for produto in produtos:
#     print(produto["id"], "-", produto["nome_material"], "-", produto["quantidade"])

#%%
# PYTHON -> TEXTO JSON: json.dumps()
# É o que acontece quando ENVIAMOS dados para uma API
# indent=4 deixa o texto organizado | ensure_ascii=False mantém os acentos
# ...

#%%
# novo_produto = {"codigo_material": "MAT-0001", "quantidade": 500, "ativo": True, "observacao": None}

# texto_json = json.dumps(novo_produto, indent=4, ensure_ascii=False)
# print(texto_json)
# print(type(texto_json))

#%%
# NA PRÁTICA, COM O requests (próximas aulas)
# O requests faz essas conversões sozinho, então quase não usamos o json.loads/json.dumps:
#   resposta.json()                     -> transforma a resposta em dicionário/lista (faz o json.loads)
#   requests.post(url, json=produto)    -> transforma o dicionário em texto JSON (faz o json.dumps)
# O importante é saber LER a resposta: dicionário -> ["chave"] | lista -> for

#%%
# RESUMO
# json.loads(texto)  -> texto JSON para Python (receber)
# json.dumps(objeto) -> Python para texto JSON (enviar)

