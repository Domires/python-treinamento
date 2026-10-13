#%%
# FUNÇÕES
# Já utilizamos várias funções prontas: print(), len(), round(), sum()...
# Agora vamos criar as nossas

#%%
from animacoes import mostrar_animacao

#%%
# SINTAXE
# def nome_da_funcao():
#     bloco de código
# A função só é executada quando for chamada pelo nome
# ...

#%%
# def ola():
#     print("Olá!")

# ola()
# ola()

#%%
# POR QUE USAR FUNÇÕES?
# Imagine que você precisa realizar uma mesma tarefa várias vezes durante o seu script:
# você teria que escrever repetidamente o mesmo código
# ...

#%%
# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)

# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)

# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

#%%
# Com funções, você escreve uma única vez e pode reutilizar quantas vezes quiser
mostrar_animacao("funcao_maquina")
# ...

#%%
# def fahrenheit_para_celsius(fahrenheit):
#     print((fahrenheit - 32) * 5 / 9)

# fahrenheit_para_celsius(77)
# fahrenheit_para_celsius(95)
# fahrenheit_para_celsius(50)

#%%
# PARÂMETRO E ARGUMENTO
# Um parâmetro é a variável listada dentro dos parênteses na definição da função
# Um argumento é o valor real que é enviado à função quando ela é chamada
# ...

#%%
# def saudar(nome, departamento):   # nome e departamento são parâmetros
#     print(f"Olá, {nome}! Bem-vindo(a) ao time de {departamento}.")

# saudar("Ana", "Logística")         # "Ana" e "Logística" são argumentos
# saudar("Rafael", "Financeiro")

#%%
# ARGUMENTOS NOMEADOS
# Informando o nome do parâmetro, a ordem não importa
# ...

#%%
# saudar(departamento="Comercial", nome="Bruno")

#%%
# RETORNO
# print() só MOSTRA na tela; o resultado não pode ser usado depois
# A função abaixo não tem return, então ela devolve None:
mostrar_animacao("print_vs_return")
# ...

#%%
# retorno = fahrenheit_para_celsius(50)
# print(retorno)   # None
# # print(retorno + 10)   -> TypeError

#%%
# As funções podem enviar dados de volta para o código que as chamou usando a instrução "return"
# ...

#%%
# def fahrenheit_para_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9

# retorno = fahrenheit_para_celsius(50)
# print(retorno + 10)

#%%
# PARÂMETROS COM VALOR PADRÃO
# Se o argumento não for informado, usa o valor padrão
# ...

#%%
# def calcular_imposto(valor, aliquota=18):
#     return valor * aliquota / 100

# print(calcular_imposto(1000))       # usa 18 -> 180.0
# print(calcular_imposto(1000, 12))   # usa 12 -> 120.0

#%%
# RETORNANDO MAIS DE UM VALOR
# Os valores voltam juntos e podemos desempacotá-los em variáveis
# ...

#%%
# def estatisticas(valores):
#     return min(valores), max(valores), sum(valores) / len(valores)

# menor, maior, media = estatisticas([10, 20, 30, 40])
# print(menor, maior, media)

#%%
# DOCUMENTANDO A FUNÇÃO (DOCSTRING)
# O texto entre """ """ logo abaixo do def explica o que a função faz
# Passe o mouse sobre o nome da função no VS Code para vê-lo
# ...

#%%
# def formatar_moeda(valor):
#     """Converte 1234.5 em 'R$ 1.234,50' (padrão brasileiro)."""
#     texto = f"{valor:,.2f}"
#     texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
#     return f"R$ {texto}"

# print(formatar_moeda(1234567.8))

#%%
# COMBINANDO FUNÇÕES COM if E for
# ...

#%%
# def classificar_cliente(total_compras):
#     """Classifica o cliente pelo total comprado no ano."""
#     if total_compras >= 100000:
#         return "Ouro"
#     elif total_compras >= 30000:
#         return "Prata"
#     else:
#         return "Bronze"

# clientes = {"Loja A": 150000, "Loja B": 28000, "Loja C": 67000}
# for nome, compras in clientes.items():
#     print(f"{nome}: {formatar_moeda(compras)} -> {classificar_cliente(compras)}")

#%%
# FUNÇÕES QUE RETORNAM True OU False
# Muito úteis dentro de um if
# ...

#%%
# def estoque_baixo(quantidade):
#     return quantidade < 500

# if estoque_baixo(300):
#     print("Fazer pedido de compra")

#%%
# VARIÁVEIS LOCAIS E GLOBAIS
# Variáveis criadas fora das funções são globais e podem ser lidas em todo lugar
mostrar_animacao("escopo")
# ...

#%%
# x = "World"

# def minha_funcao():
#     print("Hello " + x)

# minha_funcao()

#%%
# Se você criar uma variável com o mesmo nome dentro de uma função, ela será uma variável local
# A variável local só existe dentro da função e não altera a global
# ...

#%%
# nome = "Alex"

# def minha_funcao():
#     nome = "João"
#     print("Dentro da função: " + nome)

# minha_funcao()
# print("Fora da função: " + nome)

#%%
# Para alterar uma variável global dentro de uma função, usamos a palavra-chave "global"
# Use com moderação: prefira receber parâmetros e devolver valores com return
# ...

#%%
# ano = "2025"

# def atualizar_ano():
#     global ano
#     ano = "2026"

# atualizar_ano()
# print("Estamos em " + ano)

#%%
# *args -> NÚMERO VARIÁVEL DE ARGUMENTOS
# Se você não sabe quantos argumentos serão enviados, coloque um * antes do parâmetro
# A função recebe os valores como uma tupla
# ...

#%%
# def somar(*numeros):
#     print(numeros)
#     return sum(numeros)

# print(somar(1, 2))
# print(somar(10, 20, 30, 40))

#%%
# **kwargs -> NÚMERO VARIÁVEL DE ARGUMENTOS NOMEADOS
# Com ** antes do parâmetro, a função recebe os argumentos nomeados como um dicionário
# ...

#%%
# def cadastrar_produto(**dados):
#     print(dados)
#     for campo, valor in dados.items():
#         print(f"{campo}: {valor}")

# cadastrar_produto(codigo="MAT-0001", nome="Açúcar Cristal", quantidade=500)

#%%
# FUNÇÃO RECURSIVA
# É uma função que chama a si mesma
# Precisa SEMPRE de uma condição de parada, senão nunca termina (RecursionError)
# Exemplo: contagem regressiva
mostrar_animacao("recursao")
# ...

#%%
# def contagem_regressiva(numero):
#     if numero == 0:          # condição de parada
#         print("Fim!")
#         return
#     print(numero)
#     contagem_regressiva(numero - 1)

# contagem_regressiva(5)

#%%
# Exemplo clássico: fatorial (5! = 5 x 4 x 3 x 2 x 1 = 120)
# ...

#%%
# def fatorial(n):
#     if n <= 1:
#         return 1
#     return n * fatorial(n - 1)

# print(fatorial(4))
# # fatorial(3)
# # return 3 * fatorial(2)
# # return 2 * fatorial(1)
# # if n <= 1:
# #     return 1
# # fatorial(1) retorna 1
# # fatorial(2) retorna 2 * 1 = 2
# # fatorial(3) retorna 3 * 2 = 6

#%%
# FUNÇÃO LAMBDA
# É uma função pequena, de uma linha só, sem nome
# Sintaxe: lambda parâmetros: expressão
# ...

#%%
# dobro = lambda x: x * 2
# print(dobro(5))

# produtos = [("Sulfurgran", 30), ("Premix", 10), ("Molibdato", 20)]
# print(sorted(produtos, key=lambda item: item[1]))   # ordena pela quantidade

# def pegar_valor(item):
#     return item[1]

# print(sorted(produtos, key=pegar_valor))