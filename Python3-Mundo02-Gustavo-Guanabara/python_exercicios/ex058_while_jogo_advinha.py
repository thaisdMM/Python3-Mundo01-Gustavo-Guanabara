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
    if numero_jogador != numero_computador:
        print("Errou. Tente novamente.")

print(
    f"Você ACERTOU! Digitou o numero: {numero_jogador} que é igual ao número do computador: {numero_computador}"
)
print(f"Para acertar o número você precisou de {tentativas_acerto} tentativa(s).")
print("\nFIM DO JOGO.")
