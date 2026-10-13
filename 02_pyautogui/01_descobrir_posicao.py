#%%
# DESCOBRINDO A POSIÇÃO DO MOUSE
# Para automatizar, precisamos saber ONDE clicar (coordenadas x e y da tela)

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÃO time E pyautogui
# ...

#%%
import time
import pyautogui

#%%
# POSIÇÃO ATUAL DO MOUSE
mostrar_animacao("coordenadas_tela")
# ...

#%%
time.sleep(3)
x, y = pyautogui.position()
print(f"x={x}, y={y}")

#%%
# MOSTRANDO A POSIÇÃO CONTINUAMENTE
# Mostra a posição (x, y)
# Passe o mouse sobre botões e campos e ANOTE as coordenadas
# Para encerrar: Ctrl + C no terminal (ou o botão "Interrupt" da janela interativa)
# ...

#%%
# print("Mostrando a posição do mouse. Pressione Ctrl + C para sair.")

# while True:
#     x, y = pyautogui.position()
#     print(f"x={x:5d},y={y:5d}")
#     time.sleep(0.2)

# %%
