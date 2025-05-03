from random import randint

# MEU CÓDIGO - está correto, mas o do professor é bem mais simples

maior = menor = contador = 0
numeros_aletorios_tupla = (
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
    randint(0, 10),
)
print(f"Os números sorteados entre 0 a 10 foram: {numeros_aletorios_tupla}")
for maior_menor in numeros_aletorios_tupla:
    # print(f"I: {maior_menor}")
    contador += 1
    if contador == 1:
        maior = maior_menor
        menor = maior_menor
    else:
        if maior < maior_menor:
            maior = maior_menor
        if menor > maior_menor:
            menor = maior_menor
    # print(f"MAIOR: {maior}")
    # print(f"MENOR: {menor}")
    # print(contador)
print(f"\nO maior número entre os sorteados foi: {maior}")
print(f"O menor número entre os sorteados foi: {menor}")

# CORREÇÃO PROFESSOR

numeros_aleatorios = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
)
print(f"Os valores sorteados foram: ", end="")
for numeros in numeros_aleatorios:
    print(f"{numeros}", end=" ")
print(f"\nO maior valor sorteado foi: {max(numeros_aleatorios)}")
print(f"O menor valor sorteado foi: {min(numeros_aleatorios)}")
