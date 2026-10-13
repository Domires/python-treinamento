#%%
# TIRANDO PRINTS E LOCALIZANDO IMAGENS
# Podemos encontrar um botão na tela a partir de uma imagem dele
# Problema das coordenadas fixas: se a janela mudar de lugar, o robô clica no lugar errado
# Solução: dar ao robô uma "foto" do botão e pedir para ele procurar onde esse botão está agora

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E CONFIGURAÇÃO
# useImageNotFoundException(False) -> quando não encontrar a imagem, devolve None em vez de dar erro
# ...

#%%
import time
from pathlib import Path
import pyautogui
time.sleep(1)
pyautogui.PAUSE = 0.5
pyautogui.useImageNotFoundException(False)
PASTA_IMAGENS = Path(__file__).parent / "imagens"
PASTA_IMAGENS.mkdir(exist_ok=True)

#%%
# PRINT DA TELA INTEIRA
mostrar_animacao("screenshot_regiao")
# ...

#%%
time.sleep(3)
print_tela = pyautogui.screenshot()
print_tela.save(PASTA_IMAGENS / "tela_inteira.png")
print("Print salvo em imagens/tela_inteira.png")

#%%
# PRINT DE UMA REGIÃO
# region=(x, y, largura, altura)
# Útil como "evidência" de que o robô executou uma etapa (auditoria)
# ...

#%%
# pyautogui.screenshot(PASTA_IMAGENS / "canto_superior.png", region=(0, 0, 400, 300))

#%%
# LOCALIZANDO UMA IMAGEM NA TELA
# Passo a passo
#   Abra a tela que você quer automatizar
#   Use a Ferramenta de Captura (Win + Shift + S) e recorte SÓ o botão
#   Salve a imagem na pasta "imagens" (ex: imagens/botao_salvar.png)
#   Use pyautogui.locateCenterOnScreen("imagens/botao_salvar.png")
mostrar_animacao("localizar_imagem")

#%%
# PROCURANDO A IMAGEM
# locateCenterOnScreen -> devolve o CENTRO (x, y) da imagem na tela, ou None se não encontrar
# ...

#%%
# posicao = pyautogui.locateCenterOnScreen(str(PASTA_IMAGENS / "alvo.png"))

# if posicao is None:
#     print("Imagem NÃO encontrada na tela.")
# else:
#     print(f"Imagem encontrada no centro: {posicao}")
#     pyautogui.moveTo(posicao)
#     pyautogui.click(posicao)

#%%
# ESPERANDO ALGO APARECER NA TELA
# É útil quando um sistema demora para carregar
# O robô espera o botão aparecer antes de clicar (em vez de um time.sleep "chutado")
mostrar_animacao("esperar_imagem")
# ...

#%%
# def esperar_imagem(caminho_imagem, tempo_maximo=30):
#     """Procura a imagem a cada 1 segundo até encontrar ou estourar o tempo."""
#     for segundo in range(tempo_maximo):
#         posicao = pyautogui.locateCenterOnScreen(str(caminho_imagem))
#         if posicao is not None:
#             return posicao
#         time.sleep(1)
#     return None

# resultado = esperar_imagem(PASTA_IMAGENS / "alvo.png", tempo_maximo=5)
# print("Resultado:", resultado)

#%%
# DICAS IMPORTANTES
#   A imagem precisa ser IDÊNTICA ao que está na tela (mesmo zoom, mesmo tema claro/escuro, mesmo estado do botão)
#   Cuidado com imagem do botão com hover/selecição
#   Recorte imagens pequenas e únicas (só o ícone/texto do botão)
#   Instalando o opencv (pip install opencv-python) você pode usar confidence=0.8 para aceitar pequenas diferenças -> Fica muito mais rápido para encontrar


#%%
# import pyautogui
# pyautogui.locateCenterOnScreen(str(PASTA_IMAGENS / "alvo.png"), confidence=0.8)

#%%