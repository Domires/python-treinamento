#%%
# LIMPEZA E TRATAMENTO DE DADOS

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E LEITURA DOS DADOS
# ...

#%%
# from pathlib import Path
# import pandas as pd

# PASTA_DADOS = Path(__file__).parent / "dados"
# pd.set_option("display.max_columns", 20)
# pd.set_option("display.width", 200)

# producao = pd.read_excel(PASTA_DADOS / "producao.xlsx")

#%%
# VALORES VAZIOS (NaN)
# NaN = "Not a Number" = célula vazia
# isna() marca as células vazias; .sum() conta por coluna
# ...

#%%
# print(producao.isna().sum())

#%%
# Vendo as linhas com motivo_parada vazio
# Repare: são justamente as ordens SEM parada (horas_paradas = 0)
# ...

#%%
# print(producao[producao["motivo_parada"].isna()].head())

#%%
# OPÇÃO A: PREENCHER COM UM VALOR -> fillna
mostrar_animacao("fillna_dropna")
# ...

#%%
# producao["motivo_parada"] = producao["motivo_parada"].fillna("Sem parada")
# print(producao["motivo_parada"].value_counts())

#%%
# OPÇÃO B: REMOVER AS LINHAS -> dropna
# subset -> considera só as colunas informadas
# Exemplo (não vamos usar aqui, pois perderíamos 2/3 da base!):
#   producao.dropna(subset=["motivo_parada"])
# Antes de remover, sempre pense: esse vazio é um ERRO ou uma INFORMAÇÃO?

#%%
# DUPLICADOS
# duplicated() marca as linhas repetidas | drop_duplicates() remove
# Também é possível considerar apenas algumas colunas: subset=["id_ordem"]
mostrar_animacao("duplicados")
# ...

#%%
# print("Linhas duplicadas:", producao.duplicated().sum())
# print("Ordens repetidas:", producao.duplicated(subset=["id_ordem"]).sum())

# producao = producao.drop_duplicates()

#%%
# RENOMEANDO COLUNAS
# Útil para deixar os nomes mais claros num relatório
# ...

#%%
# relatorio = producao.rename(columns={
#     "id_ordem": "Ordem",
#     "qtd_planejada_kg": "Planejado (kg)",
#     "qtd_produzida_kg": "Produzido (kg)",
#     "qtd_refugo_kg": "Refugo (kg)",
# })
# print(list(relatorio.columns))

#%%
# REMOVENDO COLUNAS
# ...

#%%
# sem_paradas = producao.drop(columns=["horas_paradas", "motivo_parada"])
# print(list(sem_paradas.columns))

#%%
# PADRONIZANDO TEXTOS
# Os mesmos métodos de texto dos fundamentos, mas aplicados à coluna inteira, usando .str antes do método
# ...

#%%
# producao["unidade_curta"] = producao["unidade"].str.replace("Unidade_", "")
# producao["turno_texto"] = "Turno " + producao["turno"]
# print(producao[["unidade", "unidade_curta", "turno", "turno_texto"]].head())

#%%
# CONVERTENDO TIPOS: astype
# Exemplo: extrair o número da ordem ("OP-0123" -> 123)
# ...

#%%
# producao["numero_ordem"] = producao["id_ordem"].str.replace("OP-", "").astype(int)
# print(producao[["id_ordem", "numero_ordem"]].head())
# print(producao["numero_ordem"].dtype)

#%%
# EXEMPLO: DADOS EXPORTADOS DE UM SISTEMA ANTIGO
# Nem sempre os dados chegam "bonitos". Veja este exemplo com problemas comuns:
#   - nomes com espaços e maiúsculas/minúsculas misturadas
#   - quantidade como TEXTO no padrão brasileiro ("1.234,5")
#   - data como TEXTO no formato dia/mês/ano
#   - linha repetida e valor faltando
# ...

#%%
# exportacao = pd.DataFrame({
#     "Unidade": ["  unidade_a", "UNIDADE_B ", "unidade_c", "unidade_c", "Unidade_D"],
#     "Data": ["05/01/2025", "06/01/2025", "07/01/2025", "07/01/2025", "08/01/2025"],
#     "Produzido": ["12.345,5", "9.870,0", "15.002,3", "15.002,3", None],
# })
# print(exportacao)
# exportacao.info()

#%%
# TRATANDO A EXPORTAÇÃO
# strip/title -> padroniza os nomes ("  unidade_a" -> "Unidade_A")
# replace + astype(float) -> tira o ponto de milhar, troca a vírgula por ponto e converte
# pd.to_datetime(..., dayfirst=True) -> o dia vem antes do mês (padrão brasileiro)
mostrar_animacao("conversao_textos")
# ...

#%%
# exportacao = exportacao.drop_duplicates()
# exportacao["Unidade"] = exportacao["Unidade"].str.strip().str.title()
# exportacao["Produzido"] = (
#     exportacao["Produzido"]
#     .str.replace(".", "", regex=False)
#     .str.replace(",", ".", regex=False)
#     .astype(float)
#     .fillna(0)
# )
# exportacao["Data"] = pd.to_datetime(exportacao["Data"], dayfirst=True)
# print(exportacao)
# exportacao.info()

#%%
# SALVANDO A BASE TRATADA (veremos mais sobre salvar na aula 09)
# ...

#%%
# producao.to_excel(PASTA_DADOS / "producao_tratada.xlsx", index=False)
# print("Arquivo producao_tratada.xlsx salvo!")

#%%
# RESUMO DAS FERRAMENTAS DE LIMPEZA
#   df.isna().sum()                  contar vazios
#   df["col"].fillna(valor)          preencher vazios
#   df.dropna(subset=[...])          remover linhas com vazios
#   df.duplicated() / drop_duplicates()  achar / remover duplicados
#   df.rename(columns={...})         renomear colunas
#   df.drop(columns=[...])           remover colunas
#   df["col"].str.strip()            tirar espaços
#   df["col"].str.upper()/.title()   padronizar maiúsculas
#   df["col"].str.replace(a, b)      substituir trechos
#   df["col"].astype(float/int/str)  converter tipo
#   pd.to_datetime(df["col"])        converter para data
