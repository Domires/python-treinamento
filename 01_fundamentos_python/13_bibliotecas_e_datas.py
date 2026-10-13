#%%
# BIBLIOTECAS E DATAS

#%%
from animacoes import mostrar_animacao

#%%
# GERENCIADOR DE PACOTES pip
# Usamos o "pip" no TERMINAL (não no Python) para instalar bibliotecas
# Verificar a instalação do pip:
#   pip --version
# Instalar um pacote:
#   pip install pandas
# Instalar vários pacotes:
#   pip install pandas pyautogui requests
# Instalar a partir de um arquivo com a lista de pacotes:
#   pip install -r requirements.txt
# Remover um pacote:
#   pip uninstall pandas
# Listar os pacotes instalados:
#   pip list

#%%
# COMO IMPORTAR
# import biblioteca               -> importa a biblioteca inteira
# from biblioteca import parte    -> importa somente uma parte dela
# import biblioteca as apelido    -> importa com um apelido
mostrar_animacao("importar")
# ...

#%%
# import math
# from datetime import datetime
# import random as rd

#%%
# BIBLIOTECA math
# floor -> arredonda para baixo
# ceil  -> arredonda para cima (útil para "quantas caixas preciso?")
# sqrt  -> raiz quadrada
# ...

#%%
# print(math.floor(10.9))
# print(math.ceil(10.1))
# print(math.sqrt(144))

#%%
# DATA E HORA (datetime)
# datetime.now() -> data e hora atuais
# date.today()   -> data de hoje
# ...

#%%
from datetime import date, timedelta

# agora = datetime.now()
# hoje = date.today()

# print("Agora:", agora)
# print("Hoje:", hoje)
# print("Ano:", hoje.year, "| Mês:", hoje.month, "| Dia:", hoje.day)

#%%
# CRIANDO UMA DATA ESPECÍFICA
# date(ano, mês, dia)
# ...

#%%
# natal = date(2026, 12, 25)
# print(natal)

#%%
# FORMATANDO DATAS (strftime = "string format time")
# Converte uma data em TEXTO no formato que quisermos
# %d dia | %m mês | %Y ano (4 dígitos) | %H hora | %M minuto | %S segundo
mostrar_animacao("strftime_codigos")
# ...

#%%
# print(hoje.strftime("%d/%m/%Y"))
# print(agora.strftime("%d/%m/%Y %H:%M"))
# print(agora.strftime("relatorio_%Y%m%d"))   # ótimo para nomes de arquivos!

#%%
# CONVERTENDO TEXTO EM DATA (strptime = "string parse time")
# Informamos o texto e o formato em que ele está
# ...

#%%
# vencimento = datetime.strptime("15/12/2026", "%d/%m/%Y").date()
# print("Vencimento:", vencimento)

#%%
# CONTAS COM DATAS
# timedelta representa um intervalo de tempo (days, hours, minutes...)
mostrar_animacao("datas_timedelta")
# ...

#%%
# prazo = hoje + timedelta(days=30)
# print(f"Prazo de 30 dias: {prazo.strftime('%d/%m/%Y')}")

# ontem = hoje - timedelta(days=1)
# print(f"Ontem: {ontem.strftime('%d/%m/%Y')}")

#%%
# DIFERENÇA ENTRE DATAS
# Subtraindo duas datas temos um timedelta; .days devolve o número de dias
# ...

#%%
# dias_ate_vencimento = (vencimento - hoje).days
# if dias_ate_vencimento < 0:
#     print(f"Título vencido há {-dias_ate_vencimento} dias")
# else:
#     print(f"Faltam {dias_ate_vencimento} dias para o vencimento")

#%%
# BIBLIOTECA random
# randint -> número inteiro aleatório entre dois valores
# choice  -> sorteia um item de uma lista
# ...

#%%
# print(rd.randint(1, 100))
# print(rd.choice(["Ana", "Bruno", "Carla"]))

#%%
# BIBLIOTECA time
# time.sleep(segundos) -> pausa o programa (muito usado no pyautogui!)
# time.time()          -> "relógio" em segundos, útil para medir duração
# ...

#%%
# import time

# inicio = time.time()
# print("Aguardando 2 segundos...")
# time.sleep(2)
# print(f"Pronto! Levou {time.time() - inicio:.1f} segundos")
