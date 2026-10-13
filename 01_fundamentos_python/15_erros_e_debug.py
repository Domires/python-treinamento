#%%
# ERROS, TRATAMENTO DE EXCEÇÕES E DEBUG

#%%
from animacoes import mostrar_animacao

#%%
# LENDO UMA MENSAGEM DE ERRO (TRACEBACK)
# Quando algo dá errado, o Python para e mostra uma mensagem em vermelho
# Leia de BAIXO para CIMA:
#   - a ÚLTIMA linha diz o TIPO do erro e o MOTIVO
#   - as linhas acima mostram o ARQUIVO e a LINHA onde aconteceu
# print("Esqueci de fechar as aspas)   # SyntaxError
# Print("Olá")                         # NameError (P maiúsculo)
# print(10 / 0)                        # ZeroDivisionError
# print("Ano: " + 2026)                # TypeError
# int("dez")                           # ValueError
# [1, 2, 3][10]                        # IndexError
# {"a": 1}["b"]                        # KeyError
mostrar_animacao("traceback_leitura")

#%%
# ERROS MAIS COMUNS
# SyntaxError       -> erro de escrita (faltou aspas, parênteses, dois-pontos...)
# IndentationError  -> recuo (espaços) errado
# NameError         -> variável ou função não existe (ou foi escrita errada)
# TypeError         -> operação com tipos incompatíveis (texto + número)
# ValueError        -> valor inválido para a operação (int("dez"))
# ZeroDivisionError -> divisão por zero
# IndexError        -> posição que não existe na lista
# KeyError          -> chave que não existe no dicionário
# FileNotFoundError -> arquivo não encontrado
# ModuleNotFoundError -> biblioteca não instalada (rode o pip install)

#%%
# try / except
# O código dentro do try é "tentado"; se der erro, o Python executa o except em vez de parar o programa
mostrar_animacao("try_except")
# ...

#%%
# try:
#     resultado = 10 / 0
#     print(resultado)
# except:
#     print("Não foi possível fazer a divisão")

# print("O programa continua normalmente")

#%%
# TRATANDO ERROS ESPECÍFICOS
# O ideal é informar QUAL erro queremos tratar
# Podemos ter vários except, um para cada tipo de erro
# ...

#%%
# valores = ["10", "abc", "0"]

# for valor in valores:
#     try:
#         resultado = 100 / int(valor)
#         print(f"100 / {valor} = {resultado}")
#     except ValueError:
#         print(f"'{valor}' não é um número")
#     except ZeroDivisionError:
#         print("Não é possível dividir por zero")

#%%
# MOSTRANDO A MENSAGEM DO ERRO
# Exception pega qualquer erro; "as erro" guarda o erro em uma variável
# ...

#%%
# try:
#     int("dez")
# except Exception as erro:
#     print(f"Deu erro: {erro}")
#     print(f"Tipo do erro: {type(erro).__name__}")

#%%
# else E finally
# else    -> executa se NÃO deu erro
# finally -> executa SEMPRE (com ou sem erro). Útil para "fechar" algo
# ...

#%%
# try:
#     numero = int("25")
# except ValueError:
#     print("Valor inválido")
# else:
#     print(f"Conversão ok: {numero}")
# finally:
#     print("Fim da tentativa")

#%%
# EXEMPLO PRÁTICO: PEDIR UM NÚMERO ATÉ O USUÁRIO DIGITAR CERTO
# ...

#%%
# while True:
#     try:
#         quantidade = int(input("Digite a quantidade: "))
#         break
#     except ValueError:
#         print("Digite apenas números inteiros!")

# print(f"Quantidade informada: {quantidade}")

#%%
# GERANDO UM ERRO DE PROPÓSITO (raise)
# Útil para impedir que o programa continue com um valor errado
# ...

#%%
# def calcular_desconto(preco, percentual):
#     if percentual < 0 or percentual > 100:
#         raise ValueError("O percentual deve estar entre 0 e 100")
#     return preco * (1 - percentual / 100)

# print(calcular_desconto(200, 10))

# try:
#     calcular_desconto(200, 150)
# except ValueError as erro:
#     print(f"Erro: {erro}")

#%%
# DEBUG: ENCONTRANDO ERROS DE LÓGICA
# Nem todo problema gera mensagem de erro: às vezes o código roda, mas o resultado está ERRADO
# Formas de investigar:
#   1. print() -> mostrar o valor das variáveis em cada etapa
#   2. Debugger do VS Code -> pausar o programa e ver tudo o que está acontecendo

#%%
# COMO USAR O DEBUGGER DO VS CODE
# 1. Clique à esquerda do número da linha para criar um BREAKPOINT (bolinha vermelha)
# 2. Execute em modo debug:
#      - arquivo inteiro: F5 -> "Python Debugger: Debug Python File"
#      - célula #%%: clique em "Debug Cell" acima da célula
# 3. O programa PAUSA no breakpoint. No painel da esquerda, em "Variables", veja o valor de cada variável
# 4. Comandos:
#      F10        -> executa a linha atual e vai para a próxima (Step Over)
#      F11        -> entra dentro da função chamada na linha (Step Into)
#      Shift+F11  -> sai da função atual (Step Out)
#      F5         -> continua até o próximo breakpoint
#      Shift+F5   -> para o debug
# 5. No "Debug Console" você pode digitar qualquer variável ou expressão para ver o valor
mostrar_animacao("debug_breakpoint")

#%%
# EXEMPLO DE DEBUG
# A função abaixo deveria calcular a MÉDIA das vendas acima da meta, mas o resultado está errado
# Vamos colocar um breakpoint dentro do for e encontrar o problema com o debugger
# Resultado esperado: 1200.0 -> (1000 + 1400) / 2
# ...

#%%
# def media_acima_da_meta(vendas, meta):
#     soma = 0
#     quantidade = 0
#     for venda in vendas:
#         if venda > meta:
#             soma += venda
#         quantidade += 1
#     return soma / quantidade

# print(media_acima_da_meta([500, 1000, 300, 1400], 800))

#%%
# CORREÇÃO
# O contador "quantidade" estava fora do if, contando TODAS as vendas
# ...

#%%
# def media_acima_da_meta(vendas, meta):
#     soma = 0
#     quantidade = 0
#     for venda in vendas:
#         if venda > meta:
#             soma += venda
#             quantidade += 1
#     return soma / quantidade

# print(media_acima_da_meta([500, 1000, 300, 1400], 800))
