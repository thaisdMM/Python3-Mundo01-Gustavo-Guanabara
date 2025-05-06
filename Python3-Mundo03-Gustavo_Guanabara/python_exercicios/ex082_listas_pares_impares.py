numeros_completos = []
numeros_pares = []
numeros_impares = []

while True:
    numero = int(input("Digite um número: "))
    numeros_completos += [
        numero,
    ]
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida. Tente novamente.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break

for valor in numeros_completos:
    if valor % 2 == 0:
        numeros_pares += [
            valor,
        ]
    else:
        numeros_impares += [
            valor,
        ]

print(f"A lista completa de números é: {numeros_completos}")
print(f"Os números pares da lista são {numeros_pares}")
print(f"Os números ímpares da lista são {numeros_impares}")
