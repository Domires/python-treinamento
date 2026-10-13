#%%
# TOMANDO DECISÕES (if / elif / else)

#%%
from animacoes import mostrar_animacao

#%%
# CONDIÇÕES MATEMÁTICAS
# Igual: a == b
# Diferente: a != b
# Menor que: a < b
# Menor ou igual a: a <= b
# Maior que: a > b
# Maior ou igual a: a >= b

#%%
# INSTRUÇÃO if
# Avalia uma condição booleana e, se for verdadeira, executa o bloco de código de dentro
# ESTRUTURA:
#   a linha do if termina com dois-pontos (:)
#   os comandos "de dentro" ficam com recuo (normalmente TAB)
#   o recuo (indentação) é obrigatório no Python
# ...

#%%
# idade = 20
# if idade >= 18:
#     print("Adulto")
# print("Esta linha sempre aparece (está fora do if)")

#%%
# INSTRUÇÃO else
# É executada quando as condições anteriores forem falsas
mostrar_animacao("if_fluxo")
# ...

#%%
# idade = 15
# if idade >= 18:
#     print("Adulto")
# else:
#     print("Menor de idade")

#%%
# INSTRUÇÃO elif ("senão, se")
# Utilizamos quando precisamos avaliar mais de uma expressão
# O Python testa de cima para baixo e para no PRIMEIRO que for verdadeiro
mostrar_animacao("elif_cascata")
# ...

#%%
# idade = 40
# if idade <= 12:
#     print("Criança")
# elif idade < 18:
#     print("Jovem")
# elif idade < 60:
#     print("Adulto")
# else:
#     print("Idoso")

#%%
# OPERADORES LÓGICOS NO if
# and -> as duas condições precisam ser verdadeiras
# or  -> basta uma ser verdadeira
# not -> inverte o resultado
# obs: no pandas usaremos & (e) e | (ou) no lugar de and e or
# ...

#%%
# valor_compra = 15000
# estado_cliente = "SP"
# cliente_vip = False

# if valor_compra > 10000 and estado_cliente == "SP":
#     print("Frete grátis")

# if cliente_vip or valor_compra > 20000:
#     print("Ganhou desconto")
# else:
#     print("Sem desconto")

# if not cliente_vip:
#     print("Que tal se tornar VIP?")

#%%
# O OPERADOR in
# Verifica se um valor está dentro de uma lista (ou de um texto)
# ...

#%%
# estado = "MG"
# if estado in ["SP", "RJ", "MG", "ES"]:
#     print("Região Sudeste")

#%%
# IF ANINHADO
# Podemos colocar um if dentro de outro
# ...

#%%
# valor = 800
# if valor > 0:
#     if valor > 500:
#         print("Pedido grande")
#     else:
#         print("Pedido pequeno")

#%%
# ABREVIAÇÕES
# Instrução if em uma linha
# ...

#%%
# a = 50
# b = 10
# if a > b: print(f"{a} é maior que {b}")

#%%
# Instrução if else em uma linha (operador ternário)
# ...

#%%
# print(f"{a} é maior") if a > b else print(f"{b} é maior")

#%%
# Atribuir o resultado em uma variável
# ...

#%%
# maior = a if a > b else b
# print(f"O maior é {maior}")
