#%%
# REPETIÇÕES COM for

#%%
from animacoes import mostrar_animacao

#%%
# PERCORRENDO UMA LISTA
# Lê-se: "PARA CADA "item" NA lista de "itens", faça..."
# O bloco de dentro do for fica com recuo (igual ao if)
mostrar_animacao("for_lista")
# ...

#%%
# vendedores = ["Ana", "Bruno", "Carlos"]

# for vendedor in vendedores:
#     print(f"Enviando relatório para {vendedor}")

# print("Todos os relatórios enviados!")   # fora do for (sem recuo)

#%%
# PERCORRENDO UM TEXTO
# Um texto também é uma sequência (de caracteres)
# ...

#%%
# for letra in "ICL":
#     print(letra)

#%%
# ACUMULANDO UM TOTAL
# Começamos a variável com zero e, a cada volta, somamos mais um valor
mostrar_animacao("for_acumulador")
# ...

#%%
# vendas = [10, 24, 122, 183, 18]

# total = 0
# for valor in vendas:
#     total += valor

# print(total, sum(vendas))

#%%
# for + if: CONTANDO E FILTRANDO
# ...

#%%
# vendas = [10, 24, 122, 183, 18]
# meta = 20
# acima_da_meta = 0
# vendas_altas = []

# for valor in vendas:
#     if valor >= meta:
#         acima_da_meta += 1
#         vendas_altas.append(valor)

# print(f"{acima_da_meta} vendas atingiram a meta: {vendas_altas}")

#%%
# PARAR O LOOP -> instrução break
# O break interrompe o for imediatamente
mostrar_animacao("break_continue")
# ...

#%%
# for venda in vendas:
#     print(venda)
#     if venda >= 100:
#         print("Encontrei uma venda acima de 100!")
#         break

#%%
# PULAR PARA A PRÓXIMA VOLTA -> instrução continue
# O continue ignora o restante do bloco e vai para o próximo item
# ...

#%%
# for venda in vendas:
#     if venda < 20:
#         continue
#     print(f"Venda considerada: {venda}")

#%%
# REPETIR N VEZES -> range()
# range(5)        -> 0, 1, 2, 3, 4
# range(1, 6)     -> 1, 2, 3, 4, 5
# range(0, 10, 2) -> 0, 2, 4, 6, 8
mostrar_animacao("range_numeros")
# ...

#%%
# for mes in range(1, 13):
#     print(f"Gerando fechamento do mês {mes:02d}")

#%%
# POSIÇÃO + VALOR -> enumerate()
# ...

#%%
# for posicao, vendedor in enumerate(vendedores, start=1):
#     print(f"{posicao}º lugar: {vendedor}")

#%%
# PERCORRENDO DICIONÁRIOS
# .items() devolve a chave e o valor a cada volta
# ...

#%%
# estoque = {"Sulfurgran": 1000, "Sulfurball": 2000, "Molibdato": 400, "Premix": 0}

# for produto, quantidade in estoque.items():
#     if quantidade == 0:
#         print(f"{produto}: estoque esgotado!")
#     elif quantidade <= 500:
#         print(f"{produto}: estoque baixo!")
#     else:
#         print(f"{produto}: estoque ok")

#%%
# PERCORRENDO UMA "PLANILHA" (lista de dicionários)
# ...

#%%
# pedidos = [
#     {"pedido": 101, "cliente": "Loja A", "valor": 1500.00, "status": "pago"},
#     {"pedido": 102, "cliente": "Loja B", "valor": 320.50, "status": "pendente"},
#     {"pedido": 103, "cliente": "Loja C", "valor": 4890.00, "status": "pago"},
#     {"pedido": 104, "cliente": "Loja D", "valor": 760.00, "status": "pendente"},
# ]

# total_pendente = 0
# for pedido in pedidos:
#     if pedido["status"] == "pendente":
#         print(f"Cobrar {pedido['cliente']} - pedido {pedido['pedido']} - R$ {pedido['valor']:.2f}")
#         total_pendente += pedido["valor"]

# print(f"Total a receber: R$ {total_pendente:,.2f}")

#%%
# FOR DENTRO DE FOR (ANINHADO)
# ...

#%%
# unidades = ["Jacareí", "Suzano"]
# meses = ["Jan", "Fev", "Mar"]

# for unidade in unidades:
#     for mes in meses:
#         print(f"{unidade} - {mes}")

#%%
# LIST COMPREHENSION (EXTRA)
# Forma curta de criar uma lista a partir de outra
# ...

#%%
# vendas_com_bonus = [valor * 1.1 for valor in vendas]
# print(vendas_com_bonus)

# vendas_grandes = [valor for valor in vendas if valor >= 100]
# print(vendas_grandes)
