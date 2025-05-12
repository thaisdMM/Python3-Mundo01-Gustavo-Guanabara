# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_completa = [[], []]
for valores in range(1, 8):
    numero = int(input(f"Digite o {valores}° valor: "))
    if numero % 2 == 0:
        lista_completa[0].append(numero)
    else:
        lista_completa[1].append(numero)
lista_completa[0].sort()
lista_completa[1].sort()
print("=-" * 30)
print(f"A lista de números completos é: {lista_completa}")
print(f"Os valores pares digitados foram: {lista_completa[0]}")
print(f"Os valores ímpares digitados foram: {lista_completa[1]}")
