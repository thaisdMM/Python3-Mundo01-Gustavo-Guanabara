# ler um numero inteiro e imprimir tabuada

# FORMA1 que fiz primeiro
# numero = int(input("Digite um número inteiro: "))
# tabuada = numero * 1, numero * 2, numero * 3, numero * 4, numero * 5, numero * 6, numero * 7, numero * 8, numero * 9, numero * 10
# print(f"A tabuada de multiplicação do numero {numero} é: \n {tabuada}")

# FORMA2 QUE FIZ DE ACORDO COM AS INSTRUÇÕES DO PROF
# numero = int(input("Digite um número inteiro: "))
# tabuada1 = numero * 1
# tabuada2 = numero * 2
# tabuada3 = numero * 3
# tabuada4 = numero * 4
# tabuada5 = numero * 5
# tabuada6 = numero * 6
# tabuada7 = numero * 7
# tabuada8 = numero * 8
# tabuada9 = numero * 9
# tabuada10 = numero * 10
# print(f"A tabuada de multiplicação do numero {numero} é: \n {numero:} x 1 = {tabuada1} \n {numero} x 2 = {tabuada2} \n {numero} x 3 = {tabuada3} \n {numero} x 4 = {tabuada4} \n {numero} x 5 = {tabuada5} \n {numero} x 6 = {tabuada6} \n {numero} x 7 = {tabuada7}  \n {numero} x 8 = {tabuada8} \n {numero} x 9 = {tabuada9} \n {numero} x 10 = {tabuada10:}")

# forma que o prof fez :2 é pera formatar 2 digitos e ficar retinho

num = int(input("Digite um número para ver sua tabuada: "))
print("-"*12)
print(f"{num} x {1:2} = {num*1}")
print(f"{num} x {2:2} = {num*2}")
print(f"{num} x {3:2} = {num*3}")
print(f"{num} x {4:2} = {num*4}")
print(f"{num} x {5:2} = {num*5}")
print(f"{num} x {6:2} = {num*6}")
print(f"{num} x {7:2} = {num*7}")
print(f"{num} x {8:2} = {num*8}")
print(f"{num} x {9:2} = {num*9}")
print(f"{num} x {10:2} = {num*10}")
print("-"*12)