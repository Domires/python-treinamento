#%%
# MÓDULOS (ORGANIZANDO O CÓDIGO EM ARQUIVOS)

#%%
from animacoes import mostrar_animacao

#%%
# O QUE É UM MÓDULO?
# Um módulo é simplesmente um arquivo .py com funções e variáveis que podemos importar em outro arquivo
# Uma biblioteca (ex: pandas) nada mais é do que um conjunto de módulos
# Vantagens:
#   - reaproveitar as mesmas funções em vários scripts (sem copiar e colar)
#   - deixar os scripts menores e mais organizados
# Nesta pasta existe o arquivo utilitarios.py que vamos usar como exemplo

#%%
# IMPORTANDO O MÓDULO INTEIRO
# O nome do módulo é o nome do arquivo SEM o .py
# O arquivo precisa estar na mesma pasta do script (ou instalado com pip)
mostrar_animacao("importar_modulo")
# ...

#%%
# import utilitarios

# print(utilitarios.formatar_moeda(1234.5))
# print(utilitarios.calcular_desconto(200, 10))
# print(utilitarios.EMPRESA)

#%%
# IMPORTANDO SÓ ALGUMAS FUNÇÕES
# ...

#%%
from utilitarios import formatar_moeda, saudacao

print(formatar_moeda(98765.4))
print(saudacao("Bruno"))

#%%
# IMPORTANDO COM APELIDO
# É o que fazemos com "import pandas as pd"
# ...

#%%
# import utilitarios as ut

# print(ut.formatar_moeda(10))

#%%
# DESCOBRINDO O QUE TEM DENTRO DE UM MÓDULO
# dir()  -> lista os nomes disponíveis
# help() -> mostra a documentação (as docstrings)
# ...

#%%
# import utilitarios

# print(dir(utilitarios))
# help(utilitarios.formatar_moeda)

#%%
# if __name__ == "__main__":
# Todo arquivo .py tem uma variável especial chamada __name__
#   - executando o arquivo diretamente: __name__ vale "__main__"
#   - importando o arquivo:             __name__ vale o nome do módulo ("utilitarios")
# Por isso, o código dentro do if __name__ == "__main__" do utilitarios.py:
#   - RODA quando executamos python utilitarios.py
#   - NÃO RODA quando fazemos import utilitarios
# Usamos esse bloco para testar o módulo sem atrapalhar quem o importa
mostrar_animacao("name_main")
# ...

#%%
# print(__name__)
# print(utilitarios.__name__)

#%%
# CUIDADO COM O NOME DOS SEUS ARQUIVOS!
# Nunca dê a um arquivo o mesmo nome de uma biblioteca: pandas.py, json.py, requests.py, time.py...
# O Python procura primeiro na pasta do script, então o "import requests" importaria o SEU arquivo em vez da biblioteca, gerando erros estranhos

#%%
# ALTEROU O MÓDULO E A MUDANÇA NÃO APARECEU?
# O Python importa cada módulo só uma vez por execução
# Na janela interativa (#%%), reinicie o kernel ("Restart") ou use o importlib.reload
# ...

#%%
# import importlib

# importlib.reload(utilitarios)
