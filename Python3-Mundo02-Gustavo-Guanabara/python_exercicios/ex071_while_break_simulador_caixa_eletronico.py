# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("-" * 15)
print("BANCO MOREIRA")
print("-" * 15)
cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
while True:
    valor = int(input("Qual o valor você quer sacar? R$ "))

    for i in range(valor):
        if valor / 50:
            cedulas_50 = valor // 50
        if (valor % 50 != 0) / 20:
            cedulas_20 = (valor % 50) // 20
        if (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) / 10:
            cedulas_10 = (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) // 10
        if (valor - ((cedulas_50 * 50) + (cedulas_20 * 20) + (cedulas_10 * 10))) / 1:
            cedulas_1 = (
                valor - ((cedulas_50 * 50) + (cedulas_20 * 20) + (cedulas_10 * 10))
            ) // 1
    break

print(f"Total de {cedulas_50} cedulas de R$50")
print(f"Total de {cedulas_20} cédulas de R$20")
print(f"Total de {cedulas_10} cédulas de R$10")
print(f"Total de {cedulas_1} cédulas de R$1")

print("\nFim do Programa.")
