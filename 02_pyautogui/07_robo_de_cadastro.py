#%%
# ROBÔ DE CADASTRO (LOGIN + CADASTRO AUTOMÁTICO NO SITE)
# Objetivo:
#   Juntar tudo: CSV + pyautogui + if + for + funções
#   Fazer login (se precisar) e cadastrar todos os produtos do CSV no site
# ANTES DE RODAR:
#   Deixe o site rodando em outro terminal (pasta site_treinamento): python main.py
#   Confira no navegador: http://127.0.0.1:8000/login
#   Usuário: treinamento
#   Senha: 12345678
#   Obs: Não mexa no mouse e no teclado enquanto o robô roda

#%%
from animacoes import mostrar_animacao

#%%
# Lógica:
# - Ao abrir /login, o cursor já começa no campo Usuário: usuario -> Tab -> senha -> Enter
# - Se já estiver logado, o site vai direto para a tela de cadastro
# - No cadastro, o cursor começa em Fábrica e o Tab passa para o próximo campo, nesta ordem:
#     Fábrica -> Código do Material -> Nome do Material -> Lote -> Data de Produção ->
#     Data de Validade -> Quantidade -> Unidade de Medida -> Observação -> botão Salvar
# - Unidade de Medida é uma lista de escolha: basta digitar KG, T ou L
# - Observação tem várias linhas, então o Enter quebra a linha: use Tab até o Salvar e depois Enter
# - Depois de salvar, o formulário é limpo e o cursor volta para Fábrica
mostrar_animacao("mapa_tab")

#%%
# IMPORTAÇÕES E CONFIGURAÇÃO
# webbrowser -> abre um endereço no navegador padrão (já vem com o Python)
# ...

#%%
# import time
# import webbrowser
# from pathlib import Path

# import pandas as pd
# import pyautogui
# import pyperclip

# pyautogui.PAUSE = 0.3   # espera 0,3 segundo entre cada comando
# PASTA = Path(__file__).parent

#%%
# FUNÇÃO PARA DIGITAR TEXTOS COM ACENTO (copia e cola)
# ...

#%%
# def digitar(texto):
#     pyperclip.copy(str(texto))
#     pyautogui.hotkey("ctrl", "v")

#%%
# 1) LENDO O CSV
# ...

#%%
# tabela = pd.read_csv(PASTA / "produtos.csv", sep=";", dtype=str)
# tabela = tabela.fillna("")
# print(tabela)

#%%
# 2) CONFIRMAÇÃO ANTES DE COMEÇAR
# Se o usuário clicar em Cancelar, o robô para aqui
# ...

#%%
# resposta = pyautogui.confirm(
#     f"O robô vai cadastrar {len(tabela)} produtos.\n\n"
#     "NÃO mexa no mouse e no teclado durante a execução.\n"
#     "Para parar: leve o mouse a um canto da tela.",
#     title="Robô de Cadastro",
#     buttons=["Iniciar", "Cancelar"],
# )

# if resposta != "Iniciar":
#     raise SystemExit("Execução cancelada pelo usuário")

#%%
# 3) ABRINDO O SITE
# ...

#%%
# webbrowser.open("http://127.0.0.1:8000/login")
# time.sleep(5)

#%%
# 4) FAZENDO LOGIN (SE PRECISAR)
# Verificamos se já está logado pelo título da janela do navegador:
#   Tela de login:    "Login - Cadastro de Produtos"
#   Tela de cadastro: "Cadastro - Cadastro de Produtos"
mostrar_animacao("login_titulo")
# ...

#%%
# titulo = pyautogui.getActiveWindowTitle()
# print("Janela:", titulo)

# if "Login" in titulo:
#     print("Fazendo login...")
#     pyautogui.write("treinamento")
#     pyautogui.press("tab")
#     pyautogui.write("12345678")
#     pyautogui.press("enter")
#     time.sleep(3)
# else:
#     print("Já está logado!")

#%%
# 5) CADASTRANDO OS PRODUTOS
# O cursor começa no campo Fábrica e o Tab passa para o próximo campo
mostrar_animacao("robo_formulario")
# ...

#%%
# inicio = time.time()

# for indice, linha in tabela.iterrows():
#     print(f"Cadastrando {indice + 1}/{len(tabela)}: {linha['codigo_material']}")

#     digitar(linha["fabrica"])
#     pyautogui.press("tab")
#     digitar(linha["codigo_material"])
#     pyautogui.press("tab")
#     digitar(linha["nome_material"])
#     pyautogui.press("tab")
#     digitar(linha["lote"])
#     pyautogui.press("tab")
#     digitar(linha["data_producao"])
#     pyautogui.press("tab")
#     digitar(linha["data_validade"])
#     pyautogui.press("tab")
#     digitar(linha["quantidade"])
#     pyautogui.press("tab")
#     pyautogui.write(linha["unidade_medida"])   # na lista de escolha basta digitar a opção
#     pyautogui.press("tab")
#     digitar(linha["observacao"])
#     pyautogui.press("tab")                     # vai para o botão Salvar
#     pyautogui.press("enter")                   # salva

#     time.sleep(2)

# duracao = time.time() - inicio
# print(f"Fim! {len(tabela)} produtos em {duracao:.0f} segundos")

#%%
# 6) EVIDÊNCIA E AVISO FINAL
# Print da tela como comprovante e confira os produtos em http://127.0.0.1:8000/produtos
# ...

#%%
# pyautogui.screenshot(PASTA / "evidencia_cadastro.png")

# pyautogui.alert(
#     f"Concluído!\n\n{len(tabela)} produtos cadastrados em {duracao:.0f} segundos.",
#     title="Robô de Cadastro",
# )

#%%
# PARA LEVAR PARA UM SISTEMA REAL
# 1. Mapeie a ordem do Tab ou as coordenadas (01_descobrir_posicao.py) / imagens (aula 05) de cada campo e botão
# 2. Se o Tab não funcionar, clique em cada campo antes de digitar:
#       pyautogui.click(x_campo, y_campo)
#       digitar(linha["fabrica"])
# 3. Use time.sleep (ou esperar_imagem) depois de ações que demoram (salvar, carregar tela)
# 4. Teste com 1 ou 2 linhas antes de rodar a planilha inteira: tabela.head(2).iterrows()
