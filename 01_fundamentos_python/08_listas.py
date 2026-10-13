#%%
# LISTAS

#%%
from animacoes import mostrar_animacao

#%%
# CRIANDO LISTAS
# Listas são usadas para armazenar múltiplos itens em uma única variável
# Usamos colchetes [ ] e separamos os itens por vírgula
# A lista é alterável: podemos alterar, adicionar e remover itens depois que ela foi criada
# Como as listas são indexadas, podem ter itens com o mesmo valor
# ...

#%%
# unidades = ["Jacareí I", "Jacareí II", "Suzano I", "Suzano II", "Cruz Alta"]
# vendas = list((100000, 2000000, 350000, 2500000))   # também podemos usar o construtor list()
# print(unidades)
# print(vendas)

#%%
# ACESSANDO ITENS PELA POSIÇÃO (ÍNDICE)
# ATENÇÃO: a contagem começa em ZERO!
#   unidades = ["Jacareí I", "Jacareí II", "Suzano I", "Suzano II", "Cruz Alta"]
#   posição:         0            1            2           3            4
#   negativa:       -5           -4           -3          -2           -1
mostrar_animacao("lista_indices")
# ...

#%%
# print(unidades[0])     # primeiro
# print(unidades[-1])    # último
# print(unidades[0:2])   # fatia: posições 0 e 1

#%%
# ALTERANDO, ADICIONANDO E REMOVENDO ITENS
# lista[posição] = valor -> altera o item da posição
# append(valor)          -> adiciona no final
# insert(posição, valor) -> adiciona em uma posição específica
# remove(valor)          -> remove pelo valor
# pop(posição)           -> remove pela posição (sem posição, remove o último)
mostrar_animacao("lista_metodos")
# ...

#%%
# unidades[0] = "Mauá"
# print(unidades)

# unidades.append("Jacareí I")
# print(unidades)

# unidades.insert(0, "Cidade Ocidental")
# print(unidades)

# unidades.remove("Cruz Alta")
# print(unidades)

# removido = unidades.pop()
# print(f"Removido: {removido}")
# print(unidades)

#%%
# ORDENAÇÃO
# sort() aplica a ordenação diretamente na lista - é um método
# sorted() não modifica a lista, só retorna os valores ordenados - é uma função
# reverse=True -> ordem decrescente
# ...

#%%
# precos = [10, 12, 52, 55, 70, 21, 39]
# precos.sort(reverse=True)
# print(precos)

# print(sorted(precos))
# print(precos)

#%%
# JUNTANDO LISTAS DIFERENTES
# Método extend()
# ...

#%%
# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_1.extend(lista_2)
# print(lista_1)

#%%
# Operador +
# ...

#%%
# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_3 = lista_1 + lista_2
# print(lista_3)

#%%
# OBTENDO INFORMAÇÕES SOBRE A LISTA
# in  -> verifica se um item existe na lista
# len -> quantidade de itens
# sum, min, max -> soma, menor e maior valor
# ...

#%%
# if "Jacareí I" in unidades:
#     print("Sim, contém Jacareí I.")

# print(len(vendas))
# print(sum(vendas))
# print(min(vendas))
# print(max(vendas))
# print(sum(vendas) / len(vendas))   # média

#%%
# CONTANDO E PROCURANDO
# count(valor) -> quantas vezes o valor aparece
# index(valor) -> posição da primeira ocorrência do valor
# ...

#%%
# notas = [7, 8, 7, 10, 9, 7]
# print(notas.count(7))
# print(notas.index(10))

#%%
# LISTAS PODEM GUARDAR QUALQUER TIPO
# ...

#%%
# lista = ["LOTE-001", "CLIENTE X", 1349, True, 10.99]
# print(lista)

#%%
# COPIAR LISTA
# Não se pode copiar uma lista simplesmente com lista2 = lista1, pois será apenas uma referência:
# as alterações feitas em uma lista serão refletidas automaticamente na outra
mostrar_animacao("lista_copia")
# ...

#%%
# lista_original = [1, 2, 3]
# minha_lista = lista_original
# minha_lista.remove(2)
# print(lista_original)   # [1, 3] -> a original também mudou!

#%%
# Para resolver esse problema usamos o método copy() (ou o fatiamento [:])
# ...

#%%
# lista_original = [1, 2, 3]
# minha_lista = lista_original.copy()
# minha_lista.remove(2)
# print(lista_original)   # [1, 2, 3]

# lista_original = [1, 2, 3]
# minha_lista = lista_original[:]
# minha_lista.remove(2)
# print(lista_original)   # [1, 2, 3]

#%%
# OUTROS MÉTODOS DE LISTA
# reverse() -> inverte a ordem da lista
# clear()   -> remove todos os itens
# ...

#%%
# numeros = [1, 2, 3, 4]
# numeros.reverse()
# print(numeros)
# numeros.clear()
# print(numeros)

#%%
# RESUMO DOS MÉTODOS DE LISTA
# append()  -> adiciona um item no final da lista
# clear()   -> remove todos os itens da lista
# copy()    -> retorna uma cópia da lista
# count()   -> retorna quantas vezes um valor aparece
# extend()  -> adiciona os itens de outra lista no final da lista atual
# index()   -> retorna a posição da primeira ocorrência de um valor
# insert()  -> adiciona um item em uma posição específica
# pop()     -> remove o item de uma posição (padrão: o último)
# remove()  -> remove o primeiro item com o valor informado
# reverse() -> inverte a ordem da lista
# sort()    -> ordena a lista

#%%
# TUPLAS (EXTRA)
# Uma tupla é como uma lista, mas NÃO pode ser alterada depois de criada
# Usamos parênteses ( )
# ...

#%%
# coordenada = (500, 300)
# print(coordenada[0])
# # coordenada[0] = 10   -> TypeError: tuplas não podem ser alteradas
