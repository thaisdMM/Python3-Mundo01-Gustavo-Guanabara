# # tupla - imutável
# num = (2, 5, 9, 1)
# print(num)
# # num[2] = 3
# # print(num)
# # TypeError: 'tuple' object does not support item assignment

# LISTA é mutável

num = [2, 5, 9, 1]
print(num)
# mudou o 9 para 3
num[2] = 3
print(num)
print(len(num))
# dá erro, pois nao pode adicionar valores da maneira abaixo
# num[4] = 7
# IndexError: list assignment index out of range

# APPEND para adicionar valor
num.append(7)
print(num)

# SORTED - para colocar a lista em ordem
num.sort()
print(num)

# SORTED(REVERSE = TRUE) - para ordernar a lista em ordem decrescente
num.sort(reverse=True)
print(num)

# LEN
print(f"Essa lista tem {len(num)} elementos.")

# INSERT - adicionar valores a "uma determinada posição"
num.insert(2, 0)
print(num)

# REMOÇÃO DE ELEMENTOS
# POP - sem parametros remove o último elemento
num.pop()
print(num)

# POP com paramentro
num.pop(2)
print(num)

# RESULTADO DO TERMINAL DO CÓDIGO ATÉ AGORA
# 2, 5, 9, 1]
# [2, 5, 3, 1]
# 4
# [2, 5, 3, 1, 7]
# [1, 2, 3, 5, 7]
# [7, 5, 3, 2, 1]
# Essa lista tem 5 elementos.
# [7, 5, 0, 3, 2, 1]
# [7, 5, 0, 3, 2]
# [7, 5, 3, 2]

# # adicionando um elemento que já exista na lista
num2 = [7, 5, 0, 3, 2, 1]
num2.insert(2,2)
print(num2)

# REMOVE
# remove(2) - existem 2 dois > ele remove o primeiro elemento que ele encontra e elimina
# > se quiser eliminar todos os elementos selecionados tem que fazer laços
num2.remove(2)
print("Removi o primeiro valor 2")
print(num2)

# # se usar o remove com um valor que não está na lista, ele dá erro
# num2.remove(4)
# print(num2)
# ValueError: list.remove(x): x not in list

# para evitar o erro acima e tentar remover um valor que nao tem certeza que está na lista tem que fazer um if
if 4 in num2:
    num2.remove(4)
else:
    print("Não achei o número 4")

if 5 in num2:
    num2.remove(5)
    print("Removi o valor 5 da lista.")
else:
    print("Não achei o valor 5.")
print(num2)

# # RESPOSTA DO TERMINAL PARA NUM2
# [7, 5, 2, 0, 3, 2, 1]
# Removi o primeiro valor 2
# [7, 5, 0, 3, 2, 1]
# Não achei o número 4
# Removi o valor 5 da lista.
# [7, 0, 3, 2, 1]

# É a mesma coisa 
# valores = list() = valores = []

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

# para exibir a lista de outra maneira

for valor in valores:
    print(f"{valor}...", end="")

# ENUMERATE

for chave, valor in enumerate(valores):
    print(f"\nNa posição {chave}, encontrei o valor {valor}!")
print("Chguei ao final da lista")

for contador in range(0,5):
    valores.append(int(input("Digite um valor: ")))
for chave, valor in enumerate(valores):
    print(f"Na posição {chave} encontrei o valor {valor}")
print("Cheguei ao final da lista.")

a = [2, 3, 4, 7]
b = a
print(f"Lista a {a}")
print(f"Lista b {b}")

# O código abaixo muda as duas lista porque nao são cópias, uma está ligada à outra
b[2] = 8
print("\nLista b está ligada a lista a, assim mudando só a b, também muda a lista a. O código foi: b[2] = 8")
print(f"Lista a {a}")
print(f"Lista b {b}")

# para fazer CÓPIA DA LISTA
a = [2, 3, 4, 7]
b = a[:] # b recebe todos os valores de a, cria uma cópia de a dentro de b
print(f"Lista a {a}")
print(f"Lista b cópia a {b}")
b[2] = 8
print(f"Lista a {a}")
print(f"Lista b cópia a b[2] = 8 {b}")
