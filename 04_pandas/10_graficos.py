#%%
# GRÁFICOS
# O pandas desenha gráficos usando a biblioteca matplotlib (pip install matplotlib)
# Rodando pelo terminal, cada gráfico abre numa janela: FECHE a janela para ir para o próximo

#%%
from animacoes import mostrar_animacao

#%%
# IMPORTAÇÕES E PREPARAÇÃO DOS DADOS
# Para os gráficos, vamos trabalhar em TONELADAS (kg / 1000)
mostrar_animacao("qual_grafico")
# ...

#%%
# from pathlib import Path
# import pandas as pd
# import matplotlib.pyplot as plt

# PASTA = Path(__file__).parent
# PASTA_SAIDA = PASTA / "relatorios"
# PASTA_SAIDA.mkdir(exist_ok=True)

# producao = pd.read_excel(PASTA / "dados" / "producao.xlsx")
# producao["produzido_t"] = producao["qtd_produzida_kg"] / 1000
# producao["refugo_pct"] = producao["qtd_refugo_kg"] / producao["qtd_produzida_kg"] * 100
# producao["mes"] = producao["data"].dt.month

#%%
# GRÁFICO DE BARRAS: PRODUÇÃO POR UNIDADE
# Estrutura: dados.plot(kind="tipo") + ajustes do plt (título, rótulos...)
# tight_layout() ajusta as margens | savefig() salva como imagem | show() mostra na tela
mostrar_animacao("tabela_para_grafico")
# ...

#%%
# por_unidade = producao.groupby("unidade")["produzido_t"].sum().sort_values(ascending=False)

# por_unidade.plot(kind="bar", color="steelblue", figsize=(8, 5))
# plt.title("Produção por Unidade - 2025")
# plt.xlabel("Unidade")
# plt.ylabel("Produção (t)")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_unidades.png")
# plt.show()

#%%
# GRÁFICO DE BARRAS HORIZONTAIS: HORAS PARADAS POR MOTIVO
# ...

#%%
# paradas = producao.groupby("motivo_parada")["horas_paradas"].sum().sort_values()

# paradas.plot(kind="barh", color="indianred", figsize=(8, 5))
# plt.title("Horas Paradas por Motivo")
# plt.xlabel("Horas")
# plt.ylabel("")
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_paradas.png")
# plt.show()

#%%
# GRÁFICO DE LINHA: EVOLUÇÃO MENSAL
# marker="o" -> marca cada ponto | grid -> linhas de grade
# ...

#%%
# mensal = producao.groupby("mes")["produzido_t"].sum()

# mensal.plot(kind="line", marker="o", figsize=(9, 5))
# plt.title("Evolução Mensal da Produção")
# plt.xlabel("Mês")
# plt.ylabel("Produção (t)")
# plt.xticks(range(1, 13))
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_mensal.png")
# plt.show()

#%%
# GRÁFICO DE PIZZA: PARTICIPAÇÃO DE CADA PRODUTO
# autopct -> mostra o percentual de cada fatia
# ...

#%%
# por_produto = producao.groupby("produto")["produzido_t"].sum()

# por_produto.plot(kind="pie", autopct="%1.1f%%", figsize=(6, 6))
# plt.title("Participação de Cada Produto")
# plt.ylabel("")
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_produtos.png")
# plt.show()

#%%
# GRÁFICO DE BARRAS AGRUPADAS: PRODUÇÃO POR UNIDADE E TURNO
# Com uma tabela dinâmica, cada coluna vira uma barra (e uma legenda)
# ...

#%%
# tabela = producao.pivot_table(index="unidade", columns="turno", values="produzido_t", aggfunc="sum")

# tabela.plot(kind="bar", figsize=(10, 5))
# plt.title("Produção por Unidade e Turno")
# plt.xlabel("")
# plt.ylabel("Produção (t)")
# plt.xticks(rotation=0)
# plt.legend(title="Turno")
# plt.tight_layout()
# plt.savefig(PASTA_SAIDA / "grafico_turnos.png")
# plt.show()

#%%
# HISTOGRAMA: DISTRIBUIÇÃO DO REFUGO
# Mostra quantas ordens existem em cada faixa de % de refugo
# ...

#%%
# producao["refugo_pct"].plot(kind="hist", bins=20, figsize=(8, 5), color="gray")
# plt.title("Distribuição do Refugo por Ordem")
# plt.xlabel("Refugo (%)")
# plt.ylabel("Quantidade de ordens")
# plt.tight_layout()
# plt.show()

# print(f"Gráficos salvos em: {PASTA_SAIDA}")
