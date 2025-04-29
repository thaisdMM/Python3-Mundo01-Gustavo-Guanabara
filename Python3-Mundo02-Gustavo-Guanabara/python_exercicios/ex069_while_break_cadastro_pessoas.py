# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print("+-+" * 10)
print("CADASTRO DE PESSOAS")
print("+-+" * 10)
# continuar = "S"
maior_18 = 0
total_homens = 0
while True:
    continuar = " "
    while continuar not in "sSNn":
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar in "nN":
        break
    idade = int(input("Idade: "))
    print(idade)
    if idade > 18:
        maior_18 += 1
    sexo = " "
    while sexo not in "MF":
        sexo = input("[M/F] ").strip().upper()[0]
    if sexo == "M":
        total_homens += 1
    print(sexo)

print(f"O total de pessoas com mais de 18 anos é: {maior_18}")
print(f"O total de homens cadastrados foi: {total_homens}")
print("\nPrograma finalizado.")
