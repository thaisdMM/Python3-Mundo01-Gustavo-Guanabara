# Faça um programa que laig o paso de cinco passoas. No final, mostra qual foi o maior a o menor paso lidos.

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

print(f"Maior peso: {maior_peso}")
print(f"Menor peso: {menor_peso}")
