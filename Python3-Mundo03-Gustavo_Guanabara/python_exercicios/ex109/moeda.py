# Meu código: está correto, mas o do professor é mais simples

# def dobro(numero=0, formatacao=False):
#     resultado = numero * 2
#     if formatacao == True:
#         resultado = moeda(resultado, moeda="R$")
#     return resultado


# def metade(numero=0, formatacao=False):
#     resultado = numero / 2
#     if formatacao:
#         resultado = moeda(resultado, moeda="R$")
#     return resultado


# def aumentar(numero=0, valor=0, formatacao=False):
#     resultado = numero + (numero * valor / 100)
#     if formatacao:
#         resultado = moeda(resultado, moeda="R$")
#     return resultado


# def diminuir(numero=0, valor=0, formatacao=False):
#     resultado = numero - (numero * valor / 100)
#     if formatacao:
#         resultado = moeda(resultado, moeda="R$")
#     return resultado


# def moeda(numero=0, moeda="R$"):
#     return f"{moeda}{numero:>.2f}".replace(".", ",")


# CORREÇÃO DO PROFESSOR


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
