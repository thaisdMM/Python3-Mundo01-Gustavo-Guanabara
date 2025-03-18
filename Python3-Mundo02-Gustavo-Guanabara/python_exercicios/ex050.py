print("Soma dos números pares digitados: \n")
soma = 0
numeros_pares = " "
for i in range(0,6):
   numero = int(input("Digite um número inteiro: "))
   if numero % 2 == 0:
      numeros_pares += f"{numero}, "
      soma += numero
print(f"Os números pares digitados foram: {numeros_pares}")
print(f"A soma dos números pares digitados foi: {soma}")
