# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

numero_computador = randint(0, 10)
# print(numero_computador)
numero_jogador = -1
tentativas_acerto = 0
print("-x-" * 13)
print(" JOGO DE ADIVINHAÇÃO ")
print("-x-" * 13)
print("Computador pensando em um número...")
sleep(2)
print("\nTENTE ADVINHAR UM NÚMERO DE 0 A 10 ")
while numero_computador != numero_jogador:
    numero_jogador = int(input("\nDigite seu número: "))
    tentativas_acerto += 1
    if numero_computador > numero_jogador:
        print("Mais... Tente novamente.")
    elif numero_computador < numero_jogador:
        print("Menos... Tente novamente.")

print(
    f"Você ACERTOU! Digitou o numero: {numero_jogador} que é igual ao número do computador: {numero_computador}"
)
print(f"Para acertar o número você precisou de {tentativas_acerto} tentativa(s).")
print("\nFIM DO JOGO.")

# CORREÇÃO DO PROFESSOR:

computador = randint(0, 10)
print("Sou seu computador... Acabei de pensar em um número entre 0 e 10. ")
print("Será que você consegue advinhar qual foi? ")
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual é o seu palpite? "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... Tente mais uma vez.")
print(f"Acertou com {palpites} tentativas. Parabéns!")
