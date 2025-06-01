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


# \t tabulação, as vezes pode ser necessária mais de uma para o codigo ficar formatado
def resumo(preco=0, aumento=10, reducao=5):
    print("-" * 40)
    print("RESUMO DO VALOR".center(40))
    print("-" * 40)
    print(f"Preço analisado: \t{(moeda(preco))}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Metade do preço: \t{(metade(preco, True))}")
    print(f"{aumento}% de aumento: \t{aumentar(preco, aumento, True)}")
    print(f"{reducao}% de reducao: \t{diminuir(preco, reducao, True)}")
    print("-" * 40)
