# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

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

    # VENCE JOGADOR - se não é empate, nem computador ganhou só sobra 1 escolha do computador. Essa escolha perde da do jogador.
    else:
        print("JOGADOR VENCEU")

print("Programa finalizado.")
