# funções são utizadas em atividades repetitivas, veja o exemplo abaixo
# 3 trechos quase iguais
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)

# podemos substituir por:


def soma(a, b):
    s = a + b
    print(s)


# progama principal
soma(4, 5)
soma(8, 9)
soma(2, 1)

##  abaixo dá erro pois a função soma foram passados dois parâmetros(a, b) e só digitei  1
## soma(4)
## TypeError: soma() missing 1 required positional argument: 'b'

# # o parâmetro pode ser explicito


def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B = {s}")


soma(a=4, b=5)
# pode mudar a ordem do parâmetro, mas no print printa o valor de a e o valor de b, se já definido
soma(b=5, a=4)

## não pode colocar assim que dá erro, se for explicitar, tem que explicitar todos os valores do parâmetro:
## soma(a=4, 5)
## SyntaxError: positional argument follows keyword argument

# Se não explicitar o 1° valor vai para a e o 2º valor para b
soma(7, 2)

# # terminal:
# A = 4 e B = 5
# A soma de A + B = 9
# A = 4 e B = 5
# A soma de A + B = 9
# A = 7 e B = 2
# A soma de A + B = 9

# # erro:
# soma(3,9,5)
# TypeError: soma() takes 2 positional arguments but 3 were given

# EMPACOTAR PARÂMETROS


def contador(*num):
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 4, 6, 2)

# resposta terminal do print(num), criou uma tupla com os valores em contador
# (2, 1, 7)
# (8, 0)
# (4, 4, 4, 6, 2)


def contador(*num):
    for valor in num:
        print(f"{valor} ", end="")
    print("FIM!")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 4, 6, 2)


# fez uma função que recebeu os números e também contou quantos são com o len
def contador(*num):
    tamanho = len(num)
    print(f"Recebi os valores {num} e são ao todo {tamanho} números.")


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 4, 6, 2)

## Trabalhando com listas
valores = [6, 3, 9, 1, 0, 2]
print(valores)

# no código abaixo vai 2 listas na memória: lista e valores, tudo que acontece em lista vai interferir em valores, já que valores foi passado como parametro
# > isso não é um desempacotamento


def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


# DESEMPACOTAMENTO
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}")


soma(5, 2)
soma(2, 9, 4)
