"""Módulo de exemplo da aula 16: funções úteis reaproveitadas em vários scripts.

Para usar em outro arquivo da MESMA pasta:
    import utilitarios
    utilitarios.formatar_moeda(1234.5)
"""

EMPRESA = "ICL"

def formatar_moeda(valor):
    """Converte 1234.5 em 'R$ 1.234,50' (padrão brasileiro)."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def calcular_desconto(preco, percentual):
    """Devolve o preço com o desconto (percentual de 0 a 100)."""
    return preco * (1 - percentual / 100)


def saudacao(nome):
    """Monta uma mensagem de boas-vindas."""
    return f"Olá, {nome}! Bem-vindo(a) à {EMPRESA}."


# Este bloco só roda quando ESTE arquivo é executado diretamente.
# Quando o arquivo é importado por outro script, ele é ignorado.
if __name__ == "__main__":
    print("Testando o módulo utilitarios...")
    print(formatar_moeda(1234.5))
    print(calcular_desconto(200, 10))
    print(saudacao("Ana"))
