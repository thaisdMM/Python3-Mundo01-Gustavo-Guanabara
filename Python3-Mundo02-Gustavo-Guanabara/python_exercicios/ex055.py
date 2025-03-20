# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

# MEU CÓDIGO É PARECIDO COM O DO PROFESSOR, Mas nao tem o else

for i in range(0, 5):
    peso = float(input("Digite o seu peso: "))
    if i == 0:
        maior_peso = peso
        menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso

    # DESNECESSÁRIO, se nao entrar dentro do if, mantém os valores
    # else:
    #    maior_peso = maior_peso
    #    menor_peso = menor_peso

print(f"Maior peso: {maior_peso}kg")
print(f"Menor peso: {menor_peso}kg")

# CORREÇÃO PROFESSOR

maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso

        if peso < menor_peso:
            menor_peso = peso

print(f"\nO MAIOR PESO É: {maior_peso}Kg.")
print(f"O MENOR PESO É: {menor_peso}Kg.")
