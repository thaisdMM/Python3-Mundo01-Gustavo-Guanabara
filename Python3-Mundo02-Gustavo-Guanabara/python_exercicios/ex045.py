# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

# MEU CÓDIGO antes de ver a correação. Funciona normalmente, apesar de nao ter criado excessao para escolha invalida

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
escolha_jogador = int(input("Qual é a sua jogada? "))

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

# # Código do PROFESSOR:
# if escolha_computador == 0: # COMPUTADOR: PEDRA
#    if escolha_jogador ==0:
#       print("EMPATE.")
#    elif escolha_jogador == 1:
#       print("JOGADOR VENCE")
#    elif escolha_jogador == 2:
#       print("COMPUTADOR VENCE")
#    else:
#       print("Jogada inválida!")

# MEU CÓDIGO - juntando aula e meus conhecimentos

# #  tentativa de tratar escolha Jogador INVALIDA
# if escolha_jogador != 1 and escolha_jogador != 2 and escolha_jogador != 3:
#    print("Escolha inválida! Tente novamente.")

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