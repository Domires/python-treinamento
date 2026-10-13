#%%
# DICIONÁRIOS

#%%
from animacoes import mostrar_animacao

#%%
# CRIANDO UM DICIONÁRIO
# Dicionários são usados para armazenar valores em pares chave: valor
# Usamos chaves { } e o formato "chave": valor
# Um dicionário é ordenado, alterável e não permite chaves duplicadas
mostrar_animacao("dicionario_chave_valor")
# ...

#%%
# carro = {
#     "marca": "Ford",
#     "modelo": "Mustang",
#     "ano": 1964,
# }
# print(carro)

#%%
# ACESSANDO VALORES PELA CHAVE
# ...

#%%
# print(carro["marca"])
# print(carro["ano"])

#%%
# O método .get() é uma forma segura de obter um valor:
# se a chave não existir, devolve None (ou o valor padrão informado) em vez de dar erro
# ...

#%%
# print(carro.get("modelo"))
# print(carro.get("cor"))                     # None
# print(carro.get("cor", "Não cadastrada"))   # Não cadastrada
# # print(carro["cor"])                       # KeyError: a chave não existe

#%%
# NÃO PERMITE CHAVES DUPLICADAS
# Se a mesma chave aparecer duas vezes, o último valor substitui o anterior
# ...

#%%
# carro = {
#     "marca": "Ford",
#     "modelo": "Mustang",
#     "ano": 1964,
#     "ano": 2020,
# }
# print(carro)

#%%
# CONSTRUTOR dict()
# Também podemos criar um dicionário com o construtor dict()
# ...

#%%
# carro = dict(marca="Ford", modelo="Mustang", ano=1964)
# print(carro)

#%%
# CHAVES, VALORES E ITENS
# .keys()   -> todas as chaves
# .values() -> todos os valores
# .items()  -> pares (chave, valor)
# len()     -> quantidade de itens
# in        -> verifica se uma CHAVE existe
# ...

#%%
# print(carro.keys())
# print(carro.values())
# print(carro.items())
# print(len(carro))
# print("modelo" in carro)

#%%
# ALTERANDO VALORES
# Dicionários são alteráveis: podemos alterar, adicionar ou remover itens depois de criados
mostrar_animacao("dicionario_alterar")
# ...

#%%
# carro["ano"] = 2022
# print(carro)

# carro.update({"ano": 2024})
# print(carro)

#%%
# ADICIONANDO ITENS
# Se a chave não existir, ela é criada
# ...

#%%
# carro["cor"] = "vermelho"
# print(carro)

#%%
# REMOVENDO ITENS
# pop(chave) -> remove a chave e devolve o valor
# del        -> remove a chave
# ...

#%%
# cor = carro.pop("cor")
# print(cor)
# print(carro)

# del carro["modelo"]
# print(carro)

#%%
# DICIONÁRIO COMO TABELA DE CONSULTA (tipo PROCV)
# ...

#%%
# tabela_precos = {
#     "Sulfurgran": 2.50,
#     "Sulfurball": 18.90,
#     "Molibdato": 129.00,
# }

# produto = "Sulfurball"
# print(f"O preço do {produto} é R$ {tabela_precos[produto]:.2f}")

# regioes = {"SP": "Sudeste", "RJ": "Sudeste", "BA": "Nordeste", "RS": "Sul"}
# uf = "BA"
# print(f"{uf} fica na região {regioes[uf]}")

#%%
# LISTA DE DICIONÁRIOS = UMA "PLANILHA"
# Cada dicionário é uma linha; a lista é a planilha inteira
# Guarde essa ideia: é assim que trabalharemos com APIs (JSON) e com o pandas
mostrar_animacao("lista_de_dicionarios")
# ...

#%%
# pedidos = [
#     {"pedido": 1, "local": "SP", "valor": 50000.00},
#     {"pedido": 2, "local": "RJ", "valor": 40000.00},
#     {"pedido": 3, "local": "MG", "valor": 100000.00},
# ]

# print(pedidos[0])            # primeira linha
# print(pedidos[0]["valor"])   # valor da primeira linha
# print(pedidos[2]["local"])   # local da terceira linha

#%%
# DICIONÁRIO DENTRO DE DICIONÁRIO
# ...

#%%
# funcionario = {
#     "nome": "Ana",
#     "endereco": {"cidade": "Jacareí", "uf": "SP"},
# }
# print(funcionario["endereco"]["cidade"])

#%%
# RESUMO DOS MÉTODOS DE DICIONÁRIO
# clear()      -> remove todos os itens
# copy()       -> retorna uma cópia do dicionário
# fromkeys()   -> cria um dicionário com as chaves informadas e um mesmo valor
# get()        -> retorna o valor da chave (sem erro se não existir)
# items()      -> retorna os pares (chave, valor)
# keys()       -> retorna as chaves
# pop()        -> remove a chave informada e retorna o valor
# popitem()    -> remove o último par inserido
# setdefault() -> retorna o valor da chave; se não existir, cria com o valor informado
# update()     -> atualiza o dicionário com os pares informados
# values()     -> retorna os valores
