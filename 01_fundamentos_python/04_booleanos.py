#%%
# BOOLEANOS (VERDADEIRO OU FALSO)
# Muitas vezes precisamos saber se uma expressão é verdadeira ou falsa para criar condições ou validar valores

#%%
from animacoes import mostrar_animacao

#%%
# OPERADORES DE COMPARAÇÃO
# O resultado de uma comparação é sempre True (verdadeiro) ou False (falso)
# ==  igual a (dois sinais de igual!)
# !=  diferente de
# >   maior que
# <   menor que
# >=  maior ou igual a
# <=  menor ou igual a
mostrar_animacao("comparacoes")
# ...

#%%
# print(10 > 9)        # True
# print(10 == 9)       # False
# print(10 < 9)        # False
# print(10 != 9)       # True
# print("SP" == "SP")  # True
# print("SP" == "sp")  # False (maiúsculas importam)

#%%
# GUARDANDO O RESULTADO EM UMA VARIÁVEL
# ...

#%%
# vendas = 1200
# meta = 1000
# bateu_meta = vendas >= meta
# print(bateu_meta)
# print(type(bateu_meta))

#%%
# OPERADORES LÓGICOS
# and ou & -> True se as DUAS condições forem verdadeiras
# or  ou | -> True se PELO MENOS UMA for verdadeira
# not -> inverte o resultado (True vira False e vice-versa)
mostrar_animacao("and_or_not")
# ...

#%%
# valor_compra = 650
# estado = "SP"
# cliente_vip = False

# print(valor_compra > 500 and estado == "SP")
# print(valor_compra > 1000 or cliente_vip)
# print(not cliente_vip)

#%%
# A FUNÇÃO bool()
# Permite avaliar qualquer valor
# Quase todo valor é True, desde que tenha algum conteúdo
mostrar_animacao("verdadeiro_falso")
# ...

#%%
# print(bool("Olá"))
# print(bool(1))
# print(bool([1, 2, 3]))

#%%
# Valores que retornam False: False, None, 0, texto vazio e coleções vazias
# ...

#%%
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

#%%