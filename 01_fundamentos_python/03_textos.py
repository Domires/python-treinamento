#%%
# TRABALHANDO COM TEXTOS (STRINGS)

#%%
from animacoes import mostrar_animacao

#%%
# F-STRING
# Usamos f-strings para montar mensagens customizadas
# Coloque um f antes das aspas e as variáveis entre { }
mostrar_animacao("f_string")
# ...

#%%
# nome = "João"
# local = "São Paulo"
# cargo = "Analista"

# print(f"O {nome} trabalha como {cargo} em {local}")

#%%
# Dá para fazer contas dentro das chaves
# ...

#%%
# vendas = 37
# preco = 49.90
# print(f"Faturamento: {vendas * preco}")

#%%
# FORMATAÇÃO DE NÚMEROS
# {valor:.2f}  -> 2 casas decimais
# {valor:,.2f} -> separador de milhar + 2 casas decimais
# {valor:.1%}  -> percentual com 1 casa decimal (0.256 vira 25.6%)
# {valor:02d}  -> inteiro com 2 dígitos (1 vira 01)
# ...

#%%
# faturamento = 1234567.891
# taxa = 0.256
# mes = 3

# print(f"{faturamento:.2f}")    # 1234567.89
# print(f"{faturamento:,.2f}")   # 1,234,567.89 (padrão americano)
# print(f"{taxa:.1%}")           # 25.6%
# print(f"{mes:02d}")            # 03

#%%
# Truque para o padrão brasileiro (R$ 1.234.567,89):
# formata no padrão americano e troca os separadores
# ...

#%%
# valor_br = f"{faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
# print(f"R$ {valor_br}")

#%%
# PRINCIPAIS MÉTODOS DE STRING
# Métodos são usados com um ponto depois da variável (diferente das funções)
# Podemos usar um método seguido de outros
# upper   -> tudo maiúsculo
# lower   -> tudo minúsculo
# title   -> primeira letra de cada palavra maiúscula
# strip   -> remove espaços do início e do fim
# replace -> substitui um valor
mostrar_animacao("metodos_texto")
# ...

#%%
# produto = "  sulfurgran premium  "

# print(produto.upper())
# print(produto.lower())
# print(produto.title())
# print(produto.strip())
# print(produto.replace("premium", "standard"))
# print(produto.strip().upper())

#%%
# VERIFICAÇÕES
# in         -> contém
# startswith -> começa com
# endswith   -> termina com
# len        -> quantidade de caracteres (é uma função, não um método)
# ...

#%%
# email = "joao.silva@empresa.com.br"

# print("@" in email)
# print(email.startswith("joao"))
# print(email.endswith(".com.br"))
# print(len(email))

#%%
# DIVIDINDO E JUNTANDO TEXTOS
# split -> quebra um texto em partes (gera uma lista)
# join  -> junta uma lista de textos usando um separador
mostrar_animacao("split_join")
# ...

#%%
# linha_csv = "2026-01-15;Cliente A;1500.00"
# partes = linha_csv.split(";")
# print(partes)
# print(partes[1])

# usuario = email.split("@")[0]
# print(usuario)

# print(" | ".join(partes))

#%%
# FATIAMENTO (SLICING)
# Usamos para obter uma parte de um texto: texto[inicio:fim]
# A contagem começa em 0 e o "fim" não entra
# Ao omitir o índice inicial, o intervalo começa no primeiro caractere
# Ao omitir o índice final, o intervalo vai até o fim
# Use índices negativos para começar a contar a partir do final
mostrar_animacao("fatiamento")
# ...

#%%
# email = "alex.rangel@icl-group.com"
# print(email[0:11])
# print(email[:11])
# print(email[12:])
# print(email[-13:])

#%%
# CONCATENAÇÃO
# Podemos juntar textos com o operador +
# ...

#%%
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

#%%
# Não podemos combinar textos e números com +
# Converta o número com str() ou use f-string
# ...

#%%
# ano = 2026
# # texto = "Estamos em " + ano
# texto = "Estamos em " + str(ano)
# print(texto)
# print(f"Estamos em {ano}")

#%%
# CARACTERES DE ESCAPE
# \n -> cria uma nova linha (quebra de linha)
# \t -> insere uma tabulação (espaço de tab)
# \\ -> insere uma barra invertida
# \' -> insere uma aspa simples dentro de strings delimitadas por aspas simples
# \" -> insere uma aspa dupla dentro de strings delimitadas por aspas duplas
# ...

#%%
# print("Linha 1\nLinha 2")
# print("Produto:\tSulfurgran")
# print("C:\\Users\\Documentos")
# print("Ele disse: \"Olá\"")
