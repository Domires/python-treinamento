#%%
# ENTRADA DE DADOS (input)

#%%
from animacoes import mostrar_animacao

#%%
# COMANDO input()
# Mostra uma pergunta, espera o usuário digitar algo e apertar Enter
# Podemos armazenar o que foi digitado numa variável
mostrar_animacao("input_fluxo")
# ...

#%%
# nome = input("Qual é o seu nome? ")
# print(f"Olá, {nome}!")

#%%
# input() SEMPRE DEVOLVE UM TEXTO
# Mesmo que a pessoa digite 100, o Python recebe "100" (texto)
# Para fazer contas, precisamos converter com int() ou float()
mostrar_animacao("input_sempre_texto")
# ...

#%%
# peso = float(input("Digite seu peso (kg): "))
# altura = float(input("Digite sua altura (m): "))

# imc = peso / (altura ** 2)

# print(f"Seu IMC é: {imc:.2f}")

#%%
# EXEMPLO: CALCULADORA DE COMISSÃO
# ...

#%%
# vendedor = input("Nome do vendedor: ")
# valor_vendido = float(input("Valor vendido no mês: "))
# percentual = float(input("Percentual de comissão (ex: 5 para 5%): "))

# comissao = valor_vendido * percentual / 100

# print(f"Vendedor: {vendedor}")
# print(f"Vendas:   R$ {valor_vendido:,.2f}")
# print(f"Comissão: R$ {comissao:,.2f}")
