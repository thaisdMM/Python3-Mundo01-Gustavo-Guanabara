# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
# CÓDIGO DO PROFESSOR
# # Código do PROFESSOR faz isso para 0, 1, 2 do computador. EU FIZ DIFERENTE
# if escolha_computador == 0: # COMPUTADOR: PEDRA
#    if escolha_jogador ==0:
#       print("EMPATE.")
#    elif escolha_jogador == 1:
#       print("JOGADOR VENCE")
#    elif escolha_jogador == 2:
#       print("COMPUTADOR VENCE")
#    else:
#       print("Jogada inválida!")

from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
escolha_computador = randint(0, 2)
# print(f"O computador escolheu {itens[escolha_computador]}")
escolha_jogador = int(input("Qual é a sua jogada? "))

# tratar escolha Jogador OUT OF RANGE EXEPTION
if escolha_jogador not in [0, 1, 2]:
    print("ESCOLHA INVÁLIDA. tente novamente.")
else:
    print("""SUAS OPÇÕES:
   [ 0 ] PEDRA
   [ 1 ] PAPEL
   [ 2 ] TESOURA
   """)

    print("JO")
    sleep(1)
    print("KEN")
    sleep(1)
    print("PO!!!")
    sleep(1)

    print("-=-" * 11)
    print(f"Computador jogou: {itens[escolha_computador].upper()}")
    print(f"Jogador jogou: {itens[escolha_jogador].upper()}")
    print("-=-" * 11)

    # EMPATE:

    if escolha_computador == escolha_jogador:
        print("EMPATE!")

    # VENCE COMPUTADOR
    elif escolha_computador == 0 and escolha_jogador == 2 or escolha_computador == 1 and escolha_jogador == 0 or escolha_computador == 2 and escolha_jogador == 1:
        print("COMPUTADOR VENCEU!")

    # VENCE JOGADOR
    elif escolha_jogador == 0 and escolha_computador == 2 or escolha_jogador == 1 and escolha_computador == 0 or escolha_jogador == 2 and escolha_computador == 1:
        print("JOGADOR VENCEU")

    # 2 tentativa de tratar escolha inválida - nao funciona
    else:
        print("Escolha inválida.")

print("Programa finalizado.")
