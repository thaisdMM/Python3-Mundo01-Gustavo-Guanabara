# 1- AJUDA INTERATIVA - HELP()

help(print)
help(input)

# pode ser feito direto no terminal interativo do python3
# help> input()
# No Python documentation found for 'input()'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.

# help> input

# help> print

# help> len

# help> datetime

# help>

# # AJUDA INTERATIVA - IMPRIMIR O DOC INTERNO DO COMANDO - prof nao gosta

print(input.__doc__)

# 2- DOCSTRING
# > dá o manual da função
# > ajuda quando vc não sabe sobre informações sobre o comando


def contador(i, f, p):
    # a informação abaixo é a docstring:
    # tem que ser sempre abaixo do def
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Funçao criada por Gustavo Guanabara do canal Curso em Vídeo.
    """
    cont = i
    while cont <= f:
        print(f"{cont}", end="..")
        cont += p
    print("FIM!")


# contador(0,100,10)
help(contador)
# # sem fazer a docstring, aparece apenas isso ao rodar o comando help(contador)
# Help on function contador in module __main__:

# contador(i, f, p)

# 3- PARÂMETRO OPCIONAL
# > o end= do print é um parâmetro opcional


def somar(a, b, c):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 4, 5)
somar(8, 4)
# # dá erro pois folta um parâmetro
# somar(8,4)
# TypeError: somar() missing 1 required positional argument: 'c'


def somar(a, b, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 4, 5)
# com o parãmetro opcional no c=0 o código abaixo funciona
somar(8, 4)
# # como os codigos a e b não foram passados como parâmetro opcional dá erro no código abaixo
# somar()
# TypeError: somar() missing 2 required positional arguments: 'a' and 'b'


# # agora todos são opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 4, 5)
# com o parãmetro opcional no c=0 o código abaixo funciona
somar(8, 4)
somar()
# ## se colocar mais de 3 parâmetros dá erro, pois a função foi definida com 3 parâmetros, teria que utilizar a técnica de multipos parâmetros(*numero)
# somar(3, 1, 7, 2)
# TypeError: somar() takes from 0 to 3 positional arguments but 4 were given
somar(b=4, c=2)
somar(c=7, a=3)

# # # terminal
# # A soma vale 12
# # A soma vale 12
# # A soma vale 0
# # A soma vale 6
# # A soma vale 10

# #4- ESCOPO DE VARIÁVEL


def teste():
    x = 8
    print(f"Na função teste, n vale {n}")
    print(f"Na função teste, x vale {x}")


# programa principal
# n tem escopo global
n = 2
print(f"No programa principal, n vale {n}")
teste()
# # o código abaixo dá erro pois x é uma variavel local, só existe na função def
# print(f"No programa principal, x vale{x}")
# NameError: name 'x' is not defined


def teste(b):
    b += 4
    c = 2
    print(f"A dentro da função vale {a}")
    print(f"B dentro da função vale {b}")
    print(f"C dentro da função vale {c}")


# escopo global
a = 5
teste(a)
print(f"A fora da função vale {a}")
# como teste chama a,b vai receber o valor de a, assim  b = ao valor de a + 4, pois no codigo b +=4
# A dentro da função vale 5
# B dentro da função vale 9
# C dentro da função vale 2
# A fora da função vale 5

# se colocar uma varável a local os valores de dentro da função vão usar a variavel a local e não a global


def teste(b):
    a = 8
    b += 4
    c = 2
    print(f"A dentro da função vale {a}")
    print(f"B dentro da função vale {b}")
    print(f"C dentro da função vale {c}")


# escopo global
a = 5
teste(a)
print(f"A fora da função vale {a}")

# # # terminal

# # A dentro da função vale 8
# # B dentro da função vale 9
# # C dentro da função vale 2
# # A fora da função vale 5


# se usar a palavra global para a variavel dentro do escopo local
# > mesmo existindo a mesma variavel fora da função, que seria global, a palavra global tranforma a variavel dentro da funçao em global.
# > assim ao dar print em a fora da função no caso abaixo a fora da função será 8 e nao 5
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro da função vale {a}")
    print(f"B dentro da função vale {b}")
    print(f"C dentro da função vale {c}")


# A dentro da função vale 8
# B dentro da função vale 9
# C dentro da função vale 2
# A fora da função vale 8

# escopo global
a = 5
teste(a)
print(f"A fora da função vale {a}")


def funcao():
    n1 = 4
    print(f"n1 local  vale {n1}")


n1 = 2
print(f"n1 global vale {n1}")
funcao()

# existe escopo local e global na importação de biblioteca na chamada de função

# 5- RETURN


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f"A soma vale {s}")


somar(3, 2, 5)
somar(2, 2)
somar(6)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f"Meus cálculos deram {r1}, {r2} e {r3}")
# terminal
# Meus cálculos deram 10, 4 e 6

# PRÁTICA FATORIAL


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


# variável global
n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}")

# PRÁTICA FATORIAL


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f"Os resultados são {f1}, {f2} e {f3}")


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input("Digite um número: "))
if par(num):
    print("É par.")
else:
    print("Não é par.")
