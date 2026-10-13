#%%
# CONTROLANDO O TECLADO

#%%
from animacoes import mostrar_animacao

#%%
# OS COMANDOS DE TECLADO
# pyautogui.write("texto", interval=0.05) -> digita o texto (letra por letra)
# pyautogui.press("enter")                -> aperta UMA tecla
# pyautogui.press("tab", presses=3)       -> aperta a tecla 3 vezes
# pyautogui.hotkey("ctrl", "c")           -> atalho (aperta junto e solta)
#
# Nomes de teclas mais usados:
#   "enter", "tab", "esc", "space", "backspace", "delete",
#   "up", "down", "left", "right", "home", "end", "pageup", "pagedown",
#   "f1" ... "f12", "ctrl", "alt", "shift", "win"
# Lista completa: print(pyautogui.KEYBOARD_KEYS)
mostrar_animacao("write_press_hotkey")

#%%
# IMPORTAÇÕES
# pyperclip -> biblioteca para copiar e colar (área de transferência)
# ...

#%%
# import time
# import pyautogui
# import pyperclip

# pyautogui.PAUSE = 0.3

#%%
# ABRINDO O BLOCO DE NOTAS
# Win + R abre o "Executar"; digitamos notepad e Enter
# Ctrl + N cria um documento novo (caso o Bloco de Notas abra com um arquivo anterior)
# ...

#%%
# pyautogui.hotkey("win", "r")
# time.sleep(1)
# pyautogui.write("notepad")
# pyautogui.press("enter")
# time.sleep(3)
# pyautogui.hotkey("ctrl", "n")
# time.sleep(1)

#%%
# DIGITANDO UM TEXTO
# ...

#%%
# pyautogui.write("Hello World!", interval=0.05)

#%%
# PRESSIONANDO UMA TECLA
# ...

#%%
# pyautogui.press("enter")
# pyautogui.press("enter", presses=2)

#%%
# ATALHO COM DUAS TECLAS
# ctrl + a = selecionar tudo; end = vai para o fim da linha
# ...

#%%
# import pyautogui
# import time
# time.sleep(1)
# pyautogui.hotkey("ctrl", "a")
# time.sleep(1)
# pyautogui.press("end")
# pyautogui.press("enter")

#%%
# PROBLEMA COM ACENTOS
# O write() não digita letras com acento (á, ç, ã, é...)
mostrar_animacao("acentos_pyperclip")
# ...

#%%
# pyautogui.write("MAUÁ")
# pyautogui.press("enter")

#%%
# SOLUÇÃO: copiar o texto para a área de transferência e colar com Ctrl + V
# ...

#%%
# pyperclip.copy("Fábrica São Paulo")
# pyautogui.hotkey("ctrl", "v")
# pyautogui.press("enter")

#%%
# CRIANDO UMA FUNÇÃO utilitária -> digitar()
# ...

#%%
# def digitar(texto):
#     """Digita qualquer texto, inclusive com acentos, usando copiar e colar."""
#     pyperclip.copy(str(texto))
#     pyautogui.hotkey("ctrl", "v")

# digitar("Atenção: este texto tem acentuação e ç funcionando!")
# pyautogui.press("enter")

#%%
# DIGITANDO OS DADOS DE UMA LISTA
# ...

#%%
# tarefas = [
#     "Conferir notas fiscais",
#     "Atualizar planilha de custos",
#     "Enviar relatório à diretoria",
# ]

# pyautogui.press("enter")
# digitar("TAREFAS DO DIA:")
# pyautogui.press("enter")

# for numero, tarefa in enumerate(tarefas, start=1):
#     digitar(f"{numero}. {tarefa}")
#     pyautogui.press("enter")

#%%
# COPIANDO E COLANDO COM ATALHOS
# Ctrl + End vai para o final do documento
# ...

#%%
# pyautogui.hotkey("ctrl", "a")
# pyautogui.hotkey("ctrl", "c")
# pyautogui.hotkey("ctrl", "end")
# pyautogui.press("enter")
# digitar("Cópia do conteúdo acima")
# pyautogui.press("enter")
# pyautogui.hotkey("ctrl", "v")

#%%
# LENDO O QUE ESTÁ NA ÁREA DE TRANSFERÊNCIA
# pyperclip.paste() devolve o texto copiado (útil para "ler" informações de outro programa)
# ...

#%%
# texto_copiado = pyperclip.paste()
# print(texto_copiado)

#%%
# OUTROS ATALHOS ÚTEIS
# pyautogui.hotkey("alt", "tab")  -> troca de janela
# pyautogui.hotkey("ctrl", "s")   -> salvar
# pyautogui.hotkey("alt", "f4")   -> fechar janela
# pyautogui.hotkey("win", "d")    -> mostrar a área de trabalho
# pyautogui.hotkey("ctrl", "l")   -> barra de endereço do navegador
# pyautogui.hotkey("win", "up")   -> maximizar a janela

#%%
# SEGURANDO UMA TECLA
# keyDown -> aperta e segura | keyUp -> solta
# Exemplo: Shift + seta para a esquerda 5 vezes = seleciona 5 caracteres
# ...

#%%
# pyautogui.keyDown("shift")
# pyautogui.press("left", presses=5)
# pyautogui.keyUp("shift")

#%%
