from random import randint

print("-=-" * 13)
print("Vamos jogar PEDRA, PAPEL OU TESOURA")
print("-=-" * 13)

numero_computador = randint(1,3)
print(numero_computador)
numero_jogador = int(input("\nDigite: 1 para pedra, 2 para pepel, 3 para tesoura: "))
# numero_computador == 1 = "pedra"
# numero_computador == 2 = "papel"
# numero_computador == 3 = "tesoura"
# print(numero_computador)
if numero_computador == 1 and numero_jogador == 2:
   print("Computador: pedra, Jogador: papel. Você ganhou")
# if numero_computador == numero_jogador:
#    print("Empate")
if numero_computador == 1:
   jogada_computador = "pedra"
elif numero_computador == 2:
   jogada_computador = "papel"
elif numero_computador == 3:
   jogada_computador = "tesoura"