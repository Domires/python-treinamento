#%%
# CONTROLANDO O MOUSE

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E CONFIGURAÇÃO
# ...

#%%
import time

import pyautogui

pyautogui.PAUSE = 0.5

largura, altura = pyautogui.size()

centro_x = largura // 2
centro_y = altura // 2
# print("Tamanho da tela:", largura, altura)

#%%
# MOVENDO O MOUSE
# moveTo(x, y, duration=segundos) -> vai até a posição (absoluta)
# move(dx, dy, duration=segundos)  -> anda a partir de onde está (relativa)
mostrar_animacao("moveto_vs_move")
# ...

#%%
# pyautogui.moveTo(500, 500, duration=1)
# pyautogui.moveTo(centro_x, centro_y, duration=1)

#%%
# Desenhando um retângulo com movimentos relativos
# ...

#%%
# pyautogui.moveTo(100, 100, duration=0.5)
# pyautogui.move(300, 0, duration=0.5)    # 300 pixels para a direita
# pyautogui.move(0, 200, duration=0.5)    # 200 pixels para baixo
# pyautogui.move(-300, 0, duration=0.5)   # volta para a esquerda
# pyautogui.move(0, -200, duration=0.5)   # volta para cima

#%%
# CLICANDO
# click()             -> clica onde o mouse está
# click(x, y)         -> move e clica
# doubleClick(x, y)   -> clique duplo
# rightClick(x, y)    -> botão direito
# click(x, y, clicks=3) -> clique triplo (seleciona a linha toda)
mostrar_animacao("cliques")
# ...

#%%
# pyautogui.click(centro_x, centro_y)
# pyautogui.rightClick(centro_x, centro_y)   # abre o menu de contexto
# time.sleep(1)
# pyautogui.press("esc")                      # fecha o menu (teclado: próxima aula)

#%%
# ROLANDO A TELA (scroll)
# Valores positivos sobem; negativos descem
mostrar_animacao("scroll")
# ...

#%%
# pyautogui.scroll(-500)
# time.sleep(1)
# pyautogui.scroll(500)

#%%
# ABRINDO O PAINT
# Atalho Win + R abre a janela "Executar" do Windows
# Aumente o time.sleep se o computador for lento
# ...

#%%
# time.sleep(2)
# pyautogui.press("win")
# time.sleep(1)
# pyautogui.write("mspaint")
# pyautogui.press("enter")
# time.sleep(4)
# pyautogui.hotkey("win", "up")
# time.sleep(1)

#%%
# ARRASTANDO: DESENHANDO UM QUADRADO
# dragTo(x, y, duration) -> segura o botão, move até (x, y) e solta
# drag(dx, dy, duration) -> mesmo, mas relativo à posição atual
mostrar_animacao("drag_quadrado")
# ...

#%%
# time.sleep(2)
# pyautogui.press("win")
# time.sleep(1)
# pyautogui.write("mspaint")
# pyautogui.press("enter")
# time.sleep(4)
# pyautogui.hotkey("win", "up")
# time.sleep(1)

# pyautogui.moveTo(centro_x - 300, centro_y - 100)
# pyautogui.drag(200, 0, duration=0.5)
# pyautogui.drag(0, 200, duration=0.5)
# pyautogui.drag(-200, 0, duration=0.5)
# pyautogui.drag(0, -200, duration=0.5)

#%%
# DESENHANDO UMA ESCADA COM for
# ...

#%%
# time.sleep(2)
# pyautogui.press("win")
# time.sleep(1)
# pyautogui.write("mspaint")
# pyautogui.press("enter")
# time.sleep(4)
# pyautogui.hotkey("win", "up")
# time.sleep(1)

# pyautogui.moveTo(centro_x, centro_y)
# for degrau in range(6):
#     pyautogui.drag(40, 0, duration=0.2)
#     pyautogui.drag(0, 40, duration=0.2)

#%%