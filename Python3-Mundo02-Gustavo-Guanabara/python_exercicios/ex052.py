# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print("DESCOBRINDO SE É NÚMERO PRIMO")
numero = int(input("\nDigite um número para saber se é ou não número primo: "))
vezes_divisao_numero = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        vezes_divisao_numero += 1
        # print(vezes_divisao_numero) # teste
if vezes_divisao_numero == 2:
    primo = "É PRIMO"
else:
    primo = "NÃO É PRIMO"
print(f"\nO número {numero} foi dividido {vezes_divisao_numero}x e {primo}!")
print("Fim do programa.")

# CORREÇÃO PROFESSOR:

numero = int(input("\nDigite um número: "))
vezes_divisao_numero = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print("\033[34m", end=" ")
        vezes_divisao_numero += 1
    else:
        print("\033[31m", end=" ")
    print(i, end=" ")
print(f"\n\033[mO número {numero} foi divisível {vezes_divisao_numero} vezes.")
if vezes_divisao_numero == 2:
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO É PRIMO!")
