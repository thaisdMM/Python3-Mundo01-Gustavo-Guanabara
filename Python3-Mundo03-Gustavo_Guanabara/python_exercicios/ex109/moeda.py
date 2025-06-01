def moeda(numero=0, moeda="R$"):
    return f"{moeda}{numero:>.2f}".replace(".", ",")


def dobro(numero=0, formatacao=False):
    resultado = numero * 2
    if formatacao == True:
        resultado = moeda(resultado, moeda="R$")
    return resultado


def metade(numero=0, formatacao=False):
    resultado = numero / 2
    if formatacao:
        resultado = moeda(resultado, moeda="R$")
    return resultado


def aumentar(numero=0, valor=0, formatacao=False):
    resultado = numero + (numero * valor / 100)
    if formatacao:
        resultado = moeda(resultado, moeda="R$")
    return resultado


def diminuir(numero=0, valor=0, formatacao=False):
    resultado = numero - (numero * valor / 100)
    if formatacao:
        resultado = moeda(resultado, moeda="R$")
    return resultado
