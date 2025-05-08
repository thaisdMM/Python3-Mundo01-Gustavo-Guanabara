numeros_completos = []
numeros_pares = []
numeros_impares = []

while True:    
    numeros_completos.append(int(input("Digite um número: ")))
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Opção inválida. Tente novamente.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break

for valor in numeros_completos:
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)
print("=-" * 30)
print(f"A lista completa de números é: {numeros_completos}")
print(f"A lista de números pares é: {numeros_pares}")
print(f"A lista de números ímpares é: {numeros_impares}")
