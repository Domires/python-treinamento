#%%
# AGRUPAMENTOS E TABELAS DINÂMICAS

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E PREPARAÇÃO DOS DADOS
# float_format -> mostra os números com separador de milhar e 2 casas decimais
# ...

#%%
# from pathlib import Path
# import pandas as pd

# PASTA_DADOS = Path(__file__).parent / "dados"
# pd.set_option("display.max_columns", 20)
# pd.set_option("display.width", 200)
# pd.set_option("display.float_format", "{:,.2f}".format)

# producao = pd.read_excel(PASTA_DADOS / "producao.xlsx")
# producao["mes"] = producao["data"].dt.month

#%%
# INDICADORES GERAIS
# Atenção: a eficiência GERAL é o total produzido dividido pelo total planejado
# ...

#%%
# total_planejado = producao["qtd_planejada_kg"].sum()
# total_produzido = producao["qtd_produzida_kg"].sum()
# total_refugo = producao["qtd_refugo_kg"].sum()

# print(f"Produção total:   {total_produzido / 1000:,.1f} t")
# print(f"Eficiência geral: {total_produzido / total_planejado:.1%}")
# print(f"Refugo:           {total_refugo / total_produzido:.1%}")
# print(f"Horas paradas:    {producao['horas_paradas'].sum():,.1f} h")
# print(f"Nº de ordens:     {len(producao)}")

#%%
# groupby: AGRUPANDO POR UMA COLUNA
# Estrutura: df.groupby("coluna_para_agrupar")["coluna_para_calcular"].funcao()
# Funções mais usadas: sum, mean, count, min, max, nunique
# Pergunta: "Quanto cada unidade produziu?"
mostrar_animacao("groupby_soma")
# ...

#%%
# por_unidade = producao.groupby("unidade")["qtd_produzida_kg"].sum()
# print(por_unidade)

#%%
# RANKING: ORDENANDO DO MAIOR PARA O MENOR
# reset_index() transforma o resultado de volta em uma tabela "normal"
# ...

#%%
# ranking = por_unidade.sort_values(ascending=False).reset_index()
# ranking.index = ranking.index + 1   # posição começando em 1
# print(ranking)

#%%
# QUEM PRODUZIU MAIS? idxmax devolve o rótulo do maior valor
# ...

#%%
# print(producao.groupby("produto")["qtd_produzida_kg"].sum().idxmax())

#%%
# EFICIÊNCIA POR TURNO
# Somamos planejado e produzido de cada turno e depois dividimos
# Pergunta: "Algum turno rende menos?"
# ...

#%%
# por_turno = producao.groupby("turno")[["qtd_planejada_kg", "qtd_produzida_kg", "qtd_refugo_kg"]].sum()
# por_turno["eficiencia"] = por_turno["qtd_produzida_kg"] / por_turno["qtd_planejada_kg"]
# por_turno["refugo_pct"] = por_turno["qtd_refugo_kg"] / por_turno["qtd_produzida_kg"]
# print(por_turno)

#%%
# AGRUPANDO POR MAIS DE UMA COLUNA
# ...

#%%
# por_unidade_turno = producao.groupby(["unidade", "turno"])["qtd_produzida_kg"].sum().reset_index()
# print(por_unidade_turno)

#%%
# VÁRIOS INDICADORES DE UMA VEZ: agg
# nova_coluna=("coluna_origem", "função")
# Pergunta: "Quais produtos geram mais refugo?"
# ...

#%%
# resumo_produtos = producao.groupby("produto").agg(
#     ordens=("id_ordem", "count"),
#     produzido_kg=("qtd_produzida_kg", "sum"),
#     refugo_kg=("qtd_refugo_kg", "sum"),
#     media_por_ordem=("qtd_produzida_kg", "mean"),
#     unidades=("unidade", "nunique"),
# )
# resumo_produtos["refugo_pct"] = resumo_produtos["refugo_kg"] / resumo_produtos["produzido_kg"] * 100
# print(resumo_produtos.sort_values("refugo_pct", ascending=False))

#%%
# PARADAS: ONDE ESTAMOS PERDENDO TEMPO?
# Somando as horas paradas por motivo
# ...

#%%
# paradas = producao.groupby("motivo_parada")["horas_paradas"].agg(["count", "sum"]).sort_values("sum", ascending=False)
# print(paradas)

#%%
# PARTICIPAÇÃO PERCENTUAL
# ...

#%%
# participacao = por_unidade / por_unidade.sum() * 100
# print(participacao.sort_values(ascending=False).round(1))

#%%
# TABELA DINÂMICA: pivot_table
# index   -> o que vai nas LINHAS
# columns -> o que vai nas COLUNAS
# values  -> o que vai ser calculado
# aggfunc -> como calcular (sum, mean, count...)
# margins -> adiciona linha e coluna de TOTAL
mostrar_animacao("pivot_tabela")
# ...

#%%
# tabela = pd.pivot_table(
#     producao,
#     index="mes",
#     columns="unidade",
#     values="qtd_produzida_kg",
#     aggfunc="sum",
#     fill_value=0,
#     margins=True,
#     margins_name="Total",
# )
# print(tabela)

#%%
# EVOLUÇÃO MENSAL E CRESCIMENTO
# pct_change() -> variação em relação ao mês anterior
# cumsum()     -> soma acumulada
# ...

#%%
# mensal = producao.groupby("mes")["qtd_produzida_kg"].sum().to_frame("produzido_kg")
# mensal["variacao_%"] = mensal["produzido_kg"].pct_change() * 100
# mensal["acumulado_kg"] = mensal["produzido_kg"].cumsum()
# print(mensal)
