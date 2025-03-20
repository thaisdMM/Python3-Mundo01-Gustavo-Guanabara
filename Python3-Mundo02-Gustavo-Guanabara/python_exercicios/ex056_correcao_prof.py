# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma_idades = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = " "
mulher_menor_20 = 0

for pessoa in range(1, 5):
    print(f"-------- {pessoa}ª PESSOA -------")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    soma_idades += idade

    if pessoa == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome

    if sexo in "Ff" and idade < 20:
        mulher_menor_20 += 1


media_idade = soma_idades // 4
print(f"A média de idade do grupo é {media_idade} anos")
print(
    f"O homem mais velho tem {maior_idade_homem} anos e se chama: {nome_homem_mais_velho}")
print(f"Ao todo são {mulher_menor_20} mulher(es) com menos de 20 anos.")
