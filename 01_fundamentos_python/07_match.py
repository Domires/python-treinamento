#%%
# MATCH (ESCOLHA ENTRE VÁRIOS CASOS)

#%%
from animacoes import mostrar_animacao

#%%
# Em vez de escrever muitas declarações if, podemos usar a instrução match
# Sintaxe:
# match expressão:
#     case x:
#         bloco de código
#     case y:
#         bloco de código
#     case _:
#         bloco de código (quando nenhum caso anterior for atendido)
mostrar_animacao("match_casos")
# ...

#%%
# dia = 1
# match dia:
#     case 1:
#         print("Segunda")
#     case 2:
#         print("Terça")
#     case 3:
#         print("Quarta")
#     case 4:
#         print("Quinta")
#     case 5:
#         print("Sexta")
#     case 6:
#         print("Sábado")
#     case 7:
#         print("Domingo")
#     case _:
#         print("Não encontrado")

#%%
# VÁRIOS VALORES NO MESMO CASO
# Usamos | (ou) para combinar valores
# ...

#%%
# match dia:
#     case 1 | 2 | 3 | 4 | 5:
#         print("É um dia da semana")
#     case 6 | 7:
#         print("É final de semana")

#%%
# FUNCIONA COM TEXTOS TAMBÉM
# ...

#%%
# unidade = "KG"
# match unidade:
#     case "KG":
#         print("Quilograma")
#     case "T":
#         print("Tonelada")
#     case "L":
#         print("Litro")
#     case _:
#         print("Unidade desconhecida")

#%%
# CASE COM CONDIÇÃO (if)
# Podemos capturar o valor em uma variável e testar uma condição
# ...

#%%
# quantidade = 350
# match quantidade:
#     case 0:
#         print("Estoque esgotado")
#     case q if q < 500:
#         print(f"Estoque baixo: {q}")
#     case _:
#         print("Estoque ok")
