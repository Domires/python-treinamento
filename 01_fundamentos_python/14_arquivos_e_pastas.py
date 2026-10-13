#%%
# ARQUIVOS E PASTAS

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES
# pathlib -> biblioteca que trabalha com caminhos de pastas e arquivos
# shutil  -> biblioteca para copiar, mover e apagar arquivos e pastas
# ...

#%%
# from pathlib import Path
# import shutil

#%%
# VERIFICAR DIRETÓRIO ATUAL
# Path(__file__).parent = a pasta onde ESTE arquivo .py está
# Path.cwd() = a pasta de onde o Python está sendo executado
# ...

#%%
# PASTA_ATUAL = Path(__file__).parent
# print(PASTA_ATUAL)
# print(Path.cwd())

#%%
# MONTANDO CAMINHOS
# Usamos a barra / para juntar pastas e arquivos (funciona em qualquer sistema)
mostrar_animacao("caminhos")
# ...

#%%
# PASTA_TESTE = PASTA_ATUAL / "pasta_de_teste"
# print(PASTA_TESTE)
# print(PASTA_TESTE.exists())

#%%
# CRIAR PASTAS
# exist_ok=True -> não dá erro se a pasta já existir
# ...

#%%
# PASTA_TESTE.mkdir(exist_ok=True)

# for mes in ["01_janeiro", "02_fevereiro", "03_marco"]:
#     (PASTA_TESTE / mes).mkdir(exist_ok=True)

# print(PASTA_TESTE.exists())

#%%
# CRIANDO ARQUIVO DE TEXTO COM open()
# Modos: "w" = escrever (apaga o conteúdo anterior) | "a" = adicionar no final | "r" = ler
# O with fecha o arquivo automaticamente ao final do bloco
# encoding="utf-8" garante que os acentos sejam gravados corretamente
mostrar_animacao("modos_arquivo")
# ...

#%%
# arquivo = PASTA_TESTE / "anotacoes.txt"

# with open(arquivo, "w", encoding="utf-8") as f:
#     f.write("Reunião às 14h\n")
#     f.write("Enviar relatório ao diretor\n")

#%%
# ADICIONANDO CONTEÚDO NO FINAL DO ARQUIVO
# ...

#%%
# with open(arquivo, "a", encoding="utf-8") as f:
#     f.write("Conferir estoque\n")

#%%
# LENDO O ARQUIVO
# ...

#%%
# with open(arquivo, "r", encoding="utf-8") as f:
#     conteudo = f.read()

# print(conteudo)

#%%
# LENDO LINHA POR LINHA
# ...

#%%
# with open(arquivo, "r", encoding="utf-8") as f:
#     for linha in f:
#         print("->", linha.strip())

#%%
# ATALHOS DO pathlib
# write_text -> escreve (e sobrescreve) o arquivo inteiro
# read_text  -> lê o arquivo inteiro
# ...

#%%
# for i in range(1, 4):
#     (PASTA_TESTE / f"relatorio_{i}.txt").write_text(f"Relatório número {i}", encoding="utf-8")

# print((PASTA_TESTE / "relatorio_1.txt").read_text(encoding="utf-8"))

#%%
# LISTANDO ARQUIVOS E PASTAS
# iterdir() -> tudo o que existe dentro da pasta
# is_dir()  -> é uma pasta?
# ...

#%%
# for item in PASTA_TESTE.iterdir():
#     if item.is_dir():
#         print(f"[PASTA]   {item.name}")
#     else:
#         print(f"[ARQUIVO] {item.name}")

#%%
# FILTRANDO POR PADRÃO COM glob
# * significa "qualquer coisa"
# .name = nome completo | .stem = nome sem extensão | .suffix = extensão
# ...

#%%
# for arq in PASTA_TESTE.glob("relatorio_*.txt"):
#     print(arq.name, "|", arq.stem, "|", arq.suffix)

#%%
# COPIAR
# shutil.copy(origem, destino)
mostrar_animacao("copiar_mover")
# ...

#%%
# origem = PASTA_TESTE / "relatorio_1.txt"
# shutil.copy(origem, PASTA_TESTE / "01_janeiro" / "relatorio_1_copia.txt")

#%%
# RENOMEAR
# O arquivo continua na mesma pasta, só muda o nome
# ...

#%%
# novo_nome = PASTA_TESTE / "relatorio_vendas.txt"
# if not novo_nome.exists():
#     origem.rename(novo_nome)

#%%
# MOVER
# Mover é "renomear" para outra pasta
# ...

#%%
# shutil.move(PASTA_TESTE / "relatorio_2.txt", PASTA_TESTE / "02_fevereiro" / "relatorio_2.txt")
# print("Arquivos copiados, renomeados e movidos. Abra a pasta e confira!")

#%%
# APAGANDO
# unlink()      -> apaga um arquivo
# shutil.rmtree -> apaga uma pasta inteira (com tudo dentro)
# CUIDADO: apagar pelo Python não manda para a lixeira!
# ...

#%%
# (PASTA_TESTE / "relatorio_3.txt").unlink()
# shutil.rmtree(PASTA_TESTE)
# print(PASTA_TESTE.exists())
