# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Meu código

# numeros_extenso = (
#     "zero",
#     "um",
#     "dois",
#     "três",
#     "quatro",
#     "cinco",
#     "seis",
#     "sete",
#     "oito",
#     "nove",
#     "dez",
#     "onze",
#     "doze",
#     "treze",
#     "quatorze",
#     "quinze",
#     "dezesseis",
#     "dezessete",
#     "dezoito",
#     "dezenove",
#     "vinte",
# )
# while True:
#     numero = int(input("Digite um número de 0 a 20 para ver ele escrito por extenso: "))
#     # print(f"Tupla {numeros_extenso}")
#     # print(numero)
#     # erro
#     # print(numeros_extenso.index[numero])
#     if numero < 0 or numero > 20:
#         print("Número inválido.")
#     else:
#         for contador in range(0, len(numeros_extenso)):
#             # print(contador, end=" ")
#             if numero == contador:
#                 print(f"Você digitou o número {numeros_extenso[contador]}")
#         break

# CORREÇÃO PROFESSOR

numeros_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
contador_numeros_extenso = 0
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {numeros_extenso[numero]}")
        contador_numeros_extenso += 1
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        #continuar = " "
        while continuar not in "SN":
            print("Comando inválido. Tente novamente.")
            continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        
        if continuar == "N":
            break
        if continuar == "S":
            print("Voce escolheu continuar.")
    else:
        print("Tente novamente. ", end="")
print(f"Você exibiu {contador_numeros_extenso} números por extenso.")
print("Programa finalizado.")
