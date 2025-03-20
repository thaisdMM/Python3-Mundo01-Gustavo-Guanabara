# Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print("Soma dos números pares digitados: \n")
soma = 0
contador_pares = 0
numeros_pares = " "
for i in range(0, 6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        numeros_pares += f"{numero}, "
        soma += numero
        contador_pares += 1
print(f"Foram digitados {contador_pares} números pares: {numeros_pares}")
print(f"A soma dos números pares digitados foi: {soma}")
