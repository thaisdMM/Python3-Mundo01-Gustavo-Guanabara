from random import choice

print("-=-" * 13)
print("Vamos jogar PEDRA, PAPEL OU TESOURA")
print("-=-" * 13)

escolha_computador = ["pedra","papel", "tesoura"]
print(choice(escolha_computador))
escolha_jogador = input("\nDigite: pedra ou pepel ou tesoura: ").strip().lower()
print(escolha_jogador)



# numero_computador == 1 = "pedra"
# numero_computador == 2 = "papel"
# numero_computador == 3 = "tesoura"
# print(numero_computador)
# if numero_computador == 1 and numero_jogador == 2:
#    print("Computador: pedra, Jogador: papel. Você ganhou")
# if numero_computador == numero_jogador:
#    print("Empate")
# if numero_computador == 1:
#    jogada_computador = "pedra"
# elif numero_computador == 2:
#    jogada_computador = "papel"
# elif numero_computador == 3:
#    jogada_computador = "tesoura"