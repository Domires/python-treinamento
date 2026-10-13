#%%
# OPERAÇÕES MATEMÁTICAS

#%%
from animacoes import mostrar_animacao

#%%
# OPERADORES
# +  soma
# -  subtração
# *  multiplicação
# /  divisão
# ** potência
# // divisão inteira (descarta a parte decimal)
# %  resto da divisão
mostrar_animacao("operadores")
mostrar_animacao("divisao_e_resto")
# ...

#%%
# print(10 + 3)    # 13
# print(10 - 3)    # 7
# print(10 * 3)    # 30
# print(10 / 3)    # 3.3333...
# print(10 ** 3)   # 1000
# print(10 // 3)   # 3
# print(10 % 3)    # 1

#%%
# ORDEM DAS OPERAÇÕES
# Primeiro **; depois * e /; por último + e -
# Usamos parênteses para deixar claro o que vem primeiro
mostrar_animacao("ordem_operacoes")
# ...

#%%
# print(1 + 1 * 5)     # 6
# print((1 + 1) * 5)   # 10

#%%
# ARREDONDAMENTO
# round(valor, casas_decimais) -> arredonda para o valor mais próximo
# Sem informar as casas decimais, arredonda para inteiro
# ...

#%%
# custo = 10.46
# print(round(custo, 1))      # 10.5
# print(round(10 / 3, 2))     # 3.33
# print(round(1234.5678))     # 1235

#%%
# OPERADORES DE ATRIBUIÇÃO
# Podemos usar o operador matemático seguido do "=" para atribuir um valor calculado
# total += 50 é o mesmo que total = total + 50
mostrar_animacao("operadores_atribuicao")
# ...

#%%
# total = 100
# total += 50
# print(total) 
# total -= 20
# print(total)
# total *= 2
# print(total)

#%%
# FUNÇÕES MATEMÁTICAS
# abs -> valor absoluto
# min -> valor mínimo
# max -> valor máximo
# sum -> soma de uma lista
# ...

#%%
# print(abs(-500))              
# print(min(10, 45, 3, 22))     
# print(max(10, 45, 3, 22))     
# print(sum([10, 45, 3, 22]))   
