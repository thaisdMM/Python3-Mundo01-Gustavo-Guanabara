# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

# MEU CÓDIGO
#  from random import choice

# print("-=-" * 13)
# print("Vamos jogar PEDRA, PAPEL OU TESOURA")
# print("-=-" * 13)

# opcoes_computador = ["pedra","papel", "tesoura"]
# escolha_computador = choice(opcoes_computador)
# #print(escolha_computador)

# escolha_jogador = input("\nDigite: pedra ou pepel ou tesoura: ").strip().lower()
# #print(escolha_jogador)

# if escolha_computador == "pedra" and escolha_jogador == "tesoura" or escolha_computador == "papel" and escolha_jogador == "pedra" or escolha_computador == "tesoura" and escolha_jogador == "papel":
#    print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. {escolha_computador.upper()} ganha de {escolha_jogador.upper()}. Computador ganhou.")


# elif escolha_jogador == "pedra" and escolha_computador == "tesoura" or escolha_jogador == "papel" and escolha_computador == "pedra" or escolha_jogador == "tesoura" and escolha_computador == "papel":
#    print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador}. {escolha_jogador.upper()} ganha de {escolha_computador.upper()}. Jogador ganhou!")

# else:
#    print(f"Computador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. EMPATE!")
# print("\nJogo finalizado.")

# CÓDIGO DO PROFESSOR

from random import randint
from time import sleep

itens = ("Pedra", "Papel", "Tesoura")
escolha_computador = randint(0,2)
#print(f"O computador escolheu {itens[escolha_computador]}")

print("""SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")

escolha_jogador = int(input("Qual é a sua jogada? "))
#if escolha_computador == 0 and escolha_jogador == 2:


# print("JO")
# sleep(1)
# print("KEN")
# sleep(1)
# print("PO!!!")
# sleep(1)

# print("-=-" * 20)
print(f"Computador jogou: {itens[escolha_computador].upper()}")
print(f"Jogador jogou: {itens[escolha_jogador].upper()}")
# print("-=-" * 20)