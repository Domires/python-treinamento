#%%
# INTRODUÇÃO

#%%
from animacoes import mostrar_animacao

#%%
# O QUE É O PYAUTOGUI?
# O pyautogui é uma biblioteca de RPA (Robotic Process Automation): ela controla o seu mouse e teclado, como se fosse uma pessoa usando o computador
# Serve para automatizar tarefas repetitivas que você precise realizar (em qualquer programa)
# Instalação (no terminal): pip install pyautogui pyperclip
# Obs:
#  - Enquanto o robô roda, NÃO mexa no mouse/teclado (ele não roda em background)
#  - Para parar o robô: leve o mouse para um dos 4 cantos da tela
#  - Teste sempre com pausas e depois acelere essas pausas se necessário
#  - Posições de tela mudam de um computador para outro (resolução, zoom, tamanho da janela)

#%%
# IMPORTAÇÃO time E pyautogui
# ...

#%%
import time
import pyautogui

#%%
# TRAVAS DE SEGURANÇA
# FAILSAFE = True -> mouse em um canto da tela interrompe o robô (já é o padrão)
# PAUSE = 0.5     -> espera 0,5 segundo entre CADA comando do pyautogui
mostrar_animacao("failsafe")
mostrar_animacao("pause")
# ...

#%%
# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 0.5

#%%
# TAMANHO DA TELA
# O pyautogui considera a tela como um plano cartesiano de pixels, onde o canto superior esquerdo é o ponto (0, 0)
# ...

#%%
largura, altura = pyautogui.size()
print(largura, altura)

#%%
# ONDE ESTÁ O MOUSE?
# ...

#%%
# x, y = pyautogui.position()
# print(f"O mouse está em x={x}, y={y}")

#%%
# O PONTO ESTÁ DENTRO DA TELA?
# ...

#%%
print(pyautogui.onScreen(100, 100))
print(pyautogui.onScreen(largura + 10, 100))

#%%
# CAIXAS DE MENSAGEM
# Úteis para avisar o usuário que o robô vai começar ou terminou
# O programa fica parado até o usuário responder
mostrar_animacao("caixas_mensagem")

#%%
# ALERTA
# Mostra uma mensagem com o botão OK
# ...

#%%
# pyautogui.alert("O robô terminou! Clique em OK.", title="Aviso")

#%%
# CONFIRMAÇÃO
# Mostra botões e devolve o texto do botão clicado
# ...

#%%
# resposta = pyautogui.confirm("Deseja continuar?", buttons=["Sim", "Não"])
# print(resposta)

# if resposta == "Sim":
#     print("Continuando...")
# else:
#     print("Cancelado pelo usuário")

#%%
# PROMPT
# Pede para o usuário digitar um texto (devolve None se clicar em Cancelar)
# ...

#%%
# nome = pyautogui.prompt("Digite seu nome:")
# print(nome)

#%%
# SENHA
# Igual ao prompt, mas esconde o que é digitado
# ...

#%%
# senha = pyautogui.password("Digite a senha:", mask="*")
# print(len(senha) if senha else 0, "caracteres digitados")

#%%