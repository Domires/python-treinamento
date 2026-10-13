#%%
# REPETIÇÕES COM while
# Diferença:
#   for   -> "para cada item" (sabemos quantas vezes vai repetir)
#   while -> "enquanto algo for verdade" (não sabemos quantas vezes)

#%%
from animacoes import mostrar_animacao

#%%
# ESTRUTURA DO while
# Com o while, podemos executar um conjunto de instruções enquanto uma condição for verdadeira
# Lembre-se de alterar a variável da condição, senão o loop nunca termina
mostrar_animacao("while_loop")
# ...

#%%
# i = 1
# while i < 6:
#     print(i)
#     i += 1

#%%
# EXEMPLO: EM QUANTOS MESES UM INVESTIMENTO DOBRA COM 1% DE RENDIMENTO AO MÊS?
# ...

#%%
# saldo = 1000.00
# meses = 0

# while saldo < 2000:
#     saldo = saldo * 1.01
#     meses += 1

# print(f"O valor dobra em {meses} meses (saldo final R$ {saldo:,.2f})")

#%%
# CUIDADO COM O LOOP INFINITO!
# Se a condição NUNCA ficar falsa, o programa nunca para. Exemplo (não execute):
#   contador = 1
#   while contador > 0:
#       contador += 1
# Se acontecer, aperte Ctrl + C no terminal (ou o botão de interromper do VS Code)

#%%
# break: SAINDO DA REPETIÇÃO
# Podemos criar um menu que se repete até o usuário digitar "sair"
# while True repete "para sempre"... até encontrar um break
# ATENÇÃO: primeiro verificamos se é "sair" e só depois convertemos para número
mostrar_animacao("while_true_break")
# ...

#%%
# total = 0

# while True:
#     entrada = input("Digite um valor (ou 'sair' para finalizar): ")

#     if entrada == "sair":
#         break

#     total += float(entrada)
#     print(f"Subtotal: R$ {total:.2f}")

# print(f"Total: R$ {total:.2f}")

#%%
# continue: PULANDO PARA A PRÓXIMA VOLTA
# Exemplo: mostrar só os números ímpares de 1 a 10
# ...

#%%
# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(numero)

#%%
# EXEMPLO: TENTATIVAS DE SENHA
# ...

#%%
# senha_correta = "1234"
# tentativas = 0

# while tentativas < 3:
#     senha = input("Digite a senha: ")
#     tentativas += 1
#     if senha == senha_correta:
#         print("Acesso liberado!")
#         break
#     print(f"Senha incorreta ({tentativas}/3)")
# else:
#     print("Acesso bloqueado!")   # o else do while roda quando o loop termina SEM break
