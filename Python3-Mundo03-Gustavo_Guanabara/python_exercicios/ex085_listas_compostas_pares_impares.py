lista_completa = [[], []]
for valores in range(0, 7):
    numero = int(input("Digite um valor: "))

    if numero % 2 == 0:
        lista_completa[0].append(numero)
    else:
        lista_completa[1].append(numero)
lista_completa[0].sort()
lista_completa[1].sort()

print(f"A lista de números completos é: {lista_completa}")
print(f"Os valores pares digitados foram: {lista_completa[0]}")
print(f"Os valores ímpares digitados foram: {lista_completa[1]}")
