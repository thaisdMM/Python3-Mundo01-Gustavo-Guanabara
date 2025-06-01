def dobro(numero=0, formatacao=False):
    resultado = numero * 2
    return resultado if not formatacao else moeda(resultado)


def metade(numero=0, formatacao=False):
    resultado = numero / 2
    return resultado if not formatacao else moeda(resultado)


def aumentar(numero=0, valor=0, formatacao=False):
    resultado = numero + (numero * valor / 100)
    return resultado if not formatacao else moeda(resultado)


def diminuir(numero=0, valor=0, formatacao=False):
    resultado = numero - (numero * valor / 100)
    return resultado if not formatacao else moeda(resultado)


def moeda(numero=0, moeda="R$"):
    return f"{moeda}{numero:>.2f}".replace(".", ",")


def resumo(preco, aumento, reducao):
    print("-" * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print("-" * 40)
    print(f"Preço analisado: {(moeda(preco)):>15}")
    print(f"Metade do preço: {(metade(preco, True)):>15}")
    print(f"{aumento:3}% de aumento: {aumentar(preco, aumento, True):>15}")
    print(f"{reducao:3}% de reducao: {diminuir(preco, reducao, True):>15}")
