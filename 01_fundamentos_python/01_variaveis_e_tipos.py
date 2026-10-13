#%%
# PRIMEIROS PASSOS, VARIÁVEIS E TIPOS

#%%
from animacoes import mostrar_animacao

#%%
# COMENTÁRIOS
# Toda linha que começa com # é um comentário
# O Python ignora os comentários: eles servem para nós explicarmos o código

#%%
# O COMANDO print()
# Mostra uma mensagem na tela (no terminal)
# Textos ficam entre aspas; números não precisam de aspas
# Podemos mostrar várias coisas separadas por vírgula
# ...

#%%
# print("Olá, mundo!")
# print(2026)
# print("O resultado de 10 + 5 é", 10 + 5)

#%%
# O PYTHON LÊ DE CIMA PARA BAIXO
# Os comandos são executados na ordem em que aparecem, como uma receita
mostrar_animacao("cima_para_baixo")
# ...

#%%
# print("Passo 1: Abrir o Excel")
# print("Passo 2: Copiar os dados")
# print("Passo 3: Colar no relatório")

#%%
# CRIAÇÃO DE VARIÁVEIS
# Variáveis são usadas para armazenar valores (uma "caixinha com etiqueta")
# O Python não tem comando para declarar uma variável
# Uma variável é criada no momento em que se atribui um valor a ela
# O sinal de = significa "guarde este valor nesta variável"
mostrar_animacao("variavel_caixa")
# ...

#%%
# quantidade = 123
# unidade = "Jacareí I"

#%%
# IMPRIMIR VALORES DAS VARIVÁVEIS
# ...

#%%
# print(quantidade)
# print(unidade)

#%%
# VARIÁVEIS PODEM MUDAR DE VALOR
mostrar_animacao("variavel_muda_valor")
# ...

#%%
# estoque = 1000
# print(estoque)
# estoque = 2000
# print(estoque)
# estoque = estoque - 300   # pega o valor atual, subtrai 300 e guarda de novo
# print(estoque)

#%%
# CONSTANTES
# Em Python não existem constantes
# Para indicar que uma variável deve ser tratada como constante, escreve-se o nome inteiramente em letras maiúsculas
# ...

#%%
# QUANTIDADE_MAXIMA = 50000

#%%
# TIPOS DE DADOS
# Os principais tipos são:
# str   -> texto                       "Ana", "São Paulo", "123"
# int   -> número inteiro              10, -5, 2026
# float -> número decimal              19.90, -0.75 (use PONTO, não vírgula)
# bool  -> lógico (verdadeiro ou falso) True, False
mostrar_animacao("tipos_de_dados")
# ...

#%%
# nome = "Ana"
# idade = 34
# salario = 5750.50
# ativo = True

#%%
# VERIFICAR TIPO
# Para obtermos o tipo de dado de uma variável, usamos a função type()
# obs: variáveis string podem ser declaradas com aspas simples ou duplas
# ...

#%%
# print(type(nome))
# print(type(idade))
# print(type(salario))
# print(type(ativo))

#%%
# CUIDADO: "10" É DIFERENTE DE 10
# Com aspas é texto; sem aspas é número
mostrar_animacao("texto_vs_numero")
# ...

#%%
# numero = 10
# texto = "10"
# print(numero + numero)   # 20   -> soma
# print(texto + texto)     # 1010 -> junta os textos

#%%
# CASTING (CONVERSÃO DE TIPOS)
# Para especificar/converter o tipo de dado de uma variável, usamos casting
# str()   -> converte para texto
# int()   -> converte para inteiro
# float() -> converte para decimal
# bool()  -> converte para lógico
mostrar_animacao("casting")
# ...

#%%
# valor = "10"
# x = str(valor)
# y = int(valor)
# z = float(valor)
# print(x, y, z)
# print(y + 50)

#%%
# CASE-SENSITIVE (SENSÍVEL A MAIÚSCULAS E MINÚSCULAS)
# nome e Nome são variáveis diferentes
# ...

#%%
# nome = "Ana"
# Nome = "João"
# print(nome)
# print(Nome)

#%%
# STRING COM VÁRIAS LINHAS
# Podemos atribuir uma string de várias linhas a uma variável usando 3 aspas
# ...

#%%
# texto = """Esse é um texto
# com várias linhas
# ...
# """
# print(texto)

#%%
# REGRAS PARA NOMEAR VARIÁVEIS
# - Não pode começar com número
# - Não pode ter espaço
# - Deve começar com letra ou underscore
# - Só pode conter caracteres alfanuméricos e underscores (A-z, 0-9 e _)
# - Evite acentos e caracteres especiais
# - Dê nomes que expliquem o conteúdo (faturamento_mensal é melhor que x)
# ...

#%%
# myvar = "valor"
# my_var = "valor"
# _my_var = "valor"
# myVar = "valor"
# MYVAR = "valor"
# myvar2 = "valor"

#%%
# ATRIBUIÇÃO DE MÚLTIPLOS VALORES
# Podemos atribuir valores a múltiplas variáveis em uma só linha
# ...

#%%
# x, y, z = 1, 2, 3
# print(x, y, z)

#%%
# ATRIBUIÇÃO DE UM VALOR EM MÚLTIPLAS VARIÁVEIS
# ...

#%%
# x = y = z = 2026
# print(x, y, z)

#%%
# DESEMPACOTAMENTO
# Quando temos uma estrutura de dados com vários itens (ex: lista), podemos atribuir seus valores diretamente a várias variáveis em uma única linha
mostrar_animacao("desempacotamento")
# ...

#%%
# minha_lista = [1, 2, 3]
# x, y, z = minha_lista
# print(x, y, z)
