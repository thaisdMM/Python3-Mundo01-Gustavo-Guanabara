# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_18 = total_homens = mulheres_menor_20 = total_cadastro = 0
while True:
    print("+-+" * 10)
    print("CADASTRO DE PESSOAS")
    print("+-+" * 10)

    idade = int(input("\nIdade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo: [M/F] ").strip().upper()[0]
    if idade > 18:
        maior_18 += 1
    if sexo == "M":
        total_homens += 1
    if sexo == "F" and idade < 20:
        mulheres_menor_20 += 1
    total_cadastro += 1
    continuar = " "
    while continuar not in "SN":
        continuar = input("\nQuer continuar? [S/N] ").strip().upper()[0]
    if continuar in "nN":
        break

print(f"O total de pessoas cadastradas foi: {total_cadastro}")
print(f"O total de pessoas com mais de 18 anos é: {maior_18}")
print(f"O total de homens cadastrados foi: {total_homens}")
print(f"O total de mulheres com menos de 20 anos é: {mulheres_menor_20}")
print("\nPrograma finalizado.")
