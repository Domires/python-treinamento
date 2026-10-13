#%%
# SELECIONANDO, FILTRANDO E ORDENANDO

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
# SELECIONANDO UMA COLUNA
# df["coluna"] -> devolve uma Series
# ...

#%%
# print(producao["produto"].head())

#%%
# SELECIONANDO VÁRIAS COLUNAS
# df[["col1", "col2"]] -> atenção aos DOIS colchetes (é uma lista dentro do [ ])
# ...

#%%
# resumo = producao[["data", "unidade", "produto", "qtd_produzida_kg"]]
# print(resumo.head())

#%%
# FILTRANDO LINHAS COM UMA CONDIÇÃO
# A estrutura é: df[ condição ]
# Lê-se: "quero as linhas do df ONDE a condição for verdadeira"
mostrar_animacao("filtro_mascara")
# ...

#%%
# unidade_b = producao[producao["unidade"] == "Unidade_B"]
# print(f"Ordens da Unidade_B: {len(unidade_b)}")
# print(unidade_b.head())

#%%
# Por trás do filtro existe uma Series de True/False (uma para cada linha)
# ...

#%%
# print((producao["horas_paradas"] > 0).head())

# com_parada = producao[producao["horas_paradas"] > 0]
# print(f"Ordens que tiveram parada: {len(com_parada)}")

#%%
# VÁRIAS CONDIÇÕES: & (E) e | (OU)
# ATENÇÃO: no pandas usamos & e | (e não "and" / "or"), e CADA condição deve ficar entre parênteses
mostrar_animacao("filtro_e_ou")
# ...

#%%
# b_turno_c = producao[(producao["unidade"] == "Unidade_B") & (producao["turno"] == "C")]
# print(f"Unidade_B no turno C: {len(b_turno_c)}")

# produtos_e_h = producao[(producao["produto"] == "Produto_E") | (producao["produto"] == "Produto_H")]
# print(f"Ordens do Produto_E OU Produto_H: {len(produtos_e_h)}")

#%%
# isin -> o valor está em uma lista?
# ...

#%%
# unidades_sp = producao[producao["unidade"].isin(["Unidade_A", "Unidade_B"])]
# print(f"Ordens das unidades de SP (A e B): {len(unidades_sp)}")

#%%
# ~ -> inverte o filtro (NÃO)
# ...

#%%
# fora_turno_a = producao[~(producao["turno"] == "A")]
# print(f"Ordens fora do turno A: {len(fora_turno_a)}")

#%%
# str.contains -> o texto contém um trecho?
# O | dentro do texto significa "ou"
# ...

#%%
# paradas_manutencao = producao[producao["motivo_parada"].str.contains("Manutenção", na=False)]
# print(f"Paradas por manutenção: {len(paradas_manutencao)}")
# # na=False -> as linhas sem motivo (vazias) contam como "não contém"

#%%
# FILTRANDO POR DATA
# ...

#%%
# primeiro_trimestre = producao[(producao["data"] >= "2025-01-01") & (producao["data"] <= "2025-03-31")]
# print(f"Ordens no 1º trimestre: {len(primeiro_trimestre)}")

#%%
# between -> entre dois valores (inclusive)
# ...

#%%
# ordens_medias = producao[producao["qtd_produzida_kg"].between(10000, 20000)]
# print(f"Ordens entre 10 e 20 toneladas: {len(ordens_medias)}")

#%%
# FILTRO COM UMA CONTA
# Ordens com refugo acima de 5% do que foi produzido
# ...

#%%
# refugo_alto = producao[producao["qtd_refugo_kg"] > producao["qtd_produzida_kg"] * 0.05]
# print(f"Ordens com refugo acima de 5%: {len(refugo_alto)}")

#%%
# FILTRAR E ESCOLHER COLUNAS AO MESMO TEMPO: .loc
# df.loc[ condição_das_linhas , lista_de_colunas ]
# ...

#%%
# resultado = producao.loc[producao["horas_paradas"] >= 4, ["data", "unidade", "horas_paradas", "motivo_parada"]]
# print(resultado.head())

#%%
# FILTRO COM query (EXTRA)
# Escreve a condição como texto, de forma mais legível
# ...

#%%
# resultado = producao.query("unidade == 'Unidade_C' and turno == 'C'")
# print(resultado.head())

#%%
# ORDENANDO
# ascending=True (padrão) -> crescente | ascending=False -> decrescente
mostrar_animacao("ordenacao")
# ...

#%%
# maiores = producao.sort_values("qtd_produzida_kg", ascending=False)
# print(maiores[["data", "unidade", "produto", "qtd_produzida_kg"]].head(5))

#%%
# ORDENANDO POR MAIS DE UMA COLUNA
# ...

#%%
# ordenado = producao.sort_values(["unidade", "data"])
# print(ordenado[["unidade", "data", "produto"]].head())

#%%
# MAIORES E MENORES (atalho)
# nlargest(n, coluna) / nsmallest(n, coluna)
# ...

#%%
# print(producao.nlargest(3, "horas_paradas")[["unidade", "horas_paradas", "motivo_parada"]])
# print(producao.nsmallest(3, "qtd_produzida_kg")[["unidade", "produto", "qtd_produzida_kg"]])
