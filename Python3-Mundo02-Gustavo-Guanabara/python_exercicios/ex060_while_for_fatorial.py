# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#  Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

print("\nFATORIAL DE UM NÚMERO COM O FOR:")
numero = int(input("\nDigite um número pra saber o fatorial: "))
fatorial = 1
sequencia_fatorial = " "

for i in range(numero, 0, -1):
    # print(i)
    fatorial = fatorial * i
    if i == 1:
        sequencia_fatorial += f"{i} "
    else:
        sequencia_fatorial += f"{i} x "
#    print(fatorial)
#    print(sequencia_fatorial)

print(f"FATORIAL de {numero}: {sequencia_fatorial} = {fatorial}")

print("\nFATORIAL DE UM NÚMERO COM WHILE:")
numero = int(input("\nDigite um número pra saber o fatorial: "))
fatorial = 1
sequencia_fatorial = " "
numero_fatorial = numero

while numero > 0:
    # print(numero)
    fatorial = fatorial * numero
    sequencia_fatorial += f"{numero}"
    numero -= 1
    if numero == 0:
        sequencia_fatorial += f" "
    else:
        sequencia_fatorial += f" x "
    # print(fatorial)

print(f"Fatorial de {numero_fatorial}! {sequencia_fatorial} = {fatorial}")

# CORREÇÃO PROFESSOR

# com o MÓDULO math e a função factorial

print("\nFATORIAL COM O MODULO MATH - FACTORIAL:")
numero = int(input("Digite um número para calcular seu fatorial: "))
fatorial = factorial(numero)
print(f"O fatorial de {numero}! é {fatorial}")

# WHILE
print("\nFATORIAL COM WHILE:")
numero = int(input("Digite um número pra calcular seu fatorial: "))
contador = numero
# 1 é neutro na multiplicação, igual 0 é neutro na soma e subtração
fatorial = 1
print(f"Calculando {numero}! = ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(" x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1

print(f"{fatorial}")

# Desafio professor: LOOPING FOR

print("\nFATORIAL COM FOR:")
numero = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
print(f"Fatorial de {numero}! = ", end="")
for i in range(numero, 0, -1):
    print(f"{i}", end="")
    print(f" x " if i > 1 else " = ", end="")
    fatorial *= i
print(f"{fatorial}")
