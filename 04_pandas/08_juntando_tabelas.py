#%%
# JUNTANDO TABELAS E ARQUIVOS

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
# produtos = pd.read_csv(PASTA_DADOS / "produtos.csv", sep=";", decimal=",")
# unidades = pd.read_excel(PASTA_DADOS / "unidades.xlsx")

# print(produtos)
# print(unidades)

#%%
# merge: O "PROCV" DO PANDAS
# Queremos trazer a CATEGORIA e o CUSTO POR KG de cada produto para a base de produção
# on="produto" -> a coluna em comum entre as duas tabelas
# how="left"   -> mantém TODAS as linhas da tabela da esquerda (producao)
mostrar_animacao("merge_procv")
# ...

#%%
# producao_custo = producao.merge(produtos, on="produto", how="left")
# print(producao_custo[["data", "unidade", "produto", "categoria", "custo_kg", "qtd_produzida_kg"]].head())

#%%
# AGORA DÁ PARA CALCULAR O CUSTO DE PRODUÇÃO
# custo = quantidade produzida (kg) x custo por kg (R$)
# ...

#%%
# producao_custo["custo_producao"] = producao_custo["qtd_produzida_kg"] * producao_custo["custo_kg"]
# producao_custo["custo_refugo"] = producao_custo["qtd_refugo_kg"] * producao_custo["custo_kg"]

# custos = producao_custo.groupby("unidade")[["custo_producao", "custo_refugo"]].sum().round(2)
# print(custos)
# print(f"Dinheiro perdido com refugo no ano: R$ {producao_custo['custo_refugo'].sum():,.2f}")

#%%
# JUNTANDO COM O CADASTRO DE UNIDADES
# Trazemos a cidade, o gerente e a meta de cada unidade
# ...

#%%
# completo = producao.merge(unidades, on="unidade", how="left")
# print(completo[["data", "unidade", "cidade", "gerente", "qtd_produzida_kg"]].head())

#%%
# QUEM NÃO FOI ENCONTRADO? (o "#N/D" do PROCV)
# A Unidade_F aparece na produção, mas não está no cadastro
# ...

#%%
# nao_encontradas = completo[completo["gerente"].isna()]["unidade"].unique().tolist()
# print("Unidades sem cadastro:", nao_encontradas)

#%%
# TIPOS DE JUNÇÃO (how=)
# "left"  -> tudo da esquerda + o que encontrar da direita (o mais comum)
# "inner" -> só o que existe nas DUAS tabelas
# "right" -> tudo da direita + o que encontrar da esquerda
# "outer" -> tudo das duas tabelas
mostrar_animacao("tipos_join")
# ...

#%%
# so_cadastradas = producao.merge(unidades, on="unidade", how="inner")
# print(f"Linhas com left: {len(completo)} | com inner: {len(so_cadastradas)}")

#%%
# COLUNAS COM NOMES DIFERENTES NAS DUAS TABELAS
# left_on -> nome na tabela da esquerda | right_on -> nome na tabela da direita
# ...

#%%
# cadastro = unidades.rename(columns={"unidade": "nome_unidade"})
# junto = producao.merge(cadastro, left_on="unidade", right_on="nome_unidade", how="left")
# print(junto[["unidade", "nome_unidade", "gerente"]].head())

#%%
# EXEMPLO DE ANÁLISE: META x REALIZADO
# A meta do cadastro é MENSAL. Comparamos com a média mensal produzida em 2025
# ...

#%%
# realizado = producao.groupby("unidade")["qtd_produzida_kg"].sum().reset_index()
# realizado["media_mensal_kg"] = realizado["qtd_produzida_kg"] / 12

# meta_x_real = realizado.merge(unidades[["unidade", "gerente", "meta_mensal_kg"]], on="unidade", how="left")
# meta_x_real["atingimento_%"] = (meta_x_real["media_mensal_kg"] / meta_x_real["meta_mensal_kg"] * 100).round(1)

# print(meta_x_real.sort_values("atingimento_%", ascending=False))

#%%
# concat: EMPILHANDO VÁRIAS PLANILHAS
# Situação comum: todo mês chega uma planilha nova e precisamos de uma base única com o ano inteiro
# Antes: copiar e colar 12 vezes. Agora: algumas linhas de código!
# glob("*.xlsx") encontra todos os arquivos .xlsx da pasta (aula de arquivos e pastas)
mostrar_animacao("concat_empilhar")
# ...

#%%
# pasta_mensal = PASTA_DADOS / "producao_mensal"

# lista_tabelas = []
# for arquivo in sorted(pasta_mensal.glob("*.xlsx")):
#     print(f"Lendo {arquivo.name}...")
#     tabela_mes = pd.read_excel(arquivo)
#     tabela_mes["arquivo_origem"] = arquivo.name   # para saber de onde veio cada linha
#     lista_tabelas.append(tabela_mes)

# consolidado = pd.concat(lista_tabelas, ignore_index=True)

# print(f"Base consolidada: {len(consolidado)} linhas de {len(lista_tabelas)} arquivos")
# print(consolidado["arquivo_origem"].value_counts().sort_index())
