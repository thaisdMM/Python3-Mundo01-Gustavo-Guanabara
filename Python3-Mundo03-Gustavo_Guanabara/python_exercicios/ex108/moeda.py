def dobro(numero = 0):
    resultado = numero * 2
    return resultado


def metade(numero = 0):
    resultado = numero / 2
    return resultado


def aumentar(numero = 0, valor = 0):
    resultado = numero + (numero * valor / 100)
    return resultado


def diminuir(numero = 0, valor = 0):
    resultado = numero - (numero * valor / 100)
    return resultado

# CÓDIGO DO PROFESSOR vai adicionar parametros opcionais

def moeda(numero = 0, moeda = "R$"):
    return f"{moeda}{numero:>.2f}".replace(".", ",")

# Meu código
#  def moeda(numero):
#     resultado = (f"R${numero:.2f}")
#     return resultado