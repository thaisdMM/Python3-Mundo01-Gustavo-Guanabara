# # Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

# soma = 0
# contador = 0
# continuar = True

# while continuar:
#     numero = int(input("Digite um número: "))
#     contador += 1
#     soma += numero
#     continuar = input("Quer continuar? [N] para  NÃO. ").strip().upper()[0]
#     if continuar in "Nn":
#         print(f"Você digitou {continuar} e deseja sair do programa.")
#         continuar = False

# print(f"Você digitou {contador} números. A soma entre eles foi {soma}")
# print(f"A média dos números digitados foi {soma / contador}")

# CORREÇÃO PROFESSOR

resposta = "S"
media = soma = contador = 0
while resposta in "Ss":
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1

    resposta = input("Quer continuar? [S/N]").strip().upper()[0]
media = soma / contador
print(f"Você digitou {contador} números e média entre eles foi {media}")