pares_lista = list()
impares_lista = list()
lista_completa = list()
for valores in range(0,7):
    numero = int(input("Digite um valor: "))
    if numero % 2 == 0:
        pares_lista.append(numero)
    else:
        impares_lista.append(numero)
pares_lista.sort()
impares_lista.sort()
lista_completa.append(pares_lista)
lista_completa.append(impares_lista)

print(f"A lista de números completos é: {lista_completa}")
print(f"Os valores pares digitados foram: {pares_lista}")
print(f"Os valores ímpares digitados forama: {impares_lista}")
