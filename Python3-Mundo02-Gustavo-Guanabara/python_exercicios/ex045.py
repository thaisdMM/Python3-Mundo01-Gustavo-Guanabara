from random import choice

print("-=-" * 13)
print("Vamos jogar PEDRA, PAPEL OU TESOURA")
print("-=-" * 13)

opcoes_computador = ["pedra","papel", "tesoura"]
escolha_computador = choice(opcoes_computador)
#print(escolha_computador)

escolha_jogador = input("\nDigite: pedra ou pepel ou tesoura: ").strip().lower()
#print(escolha_jogador)

if escolha_computador == "pedra" and escolha_jogador == "tesoura" or escolha_computador == "papel" and escolha_jogador == "pedra" or escolha_computador == "tesoura" and escolha_jogador == "papel":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. {escolha_computador.upper()} ganha de {escolha_jogador.upper()}. Computador ganhou.")


elif escolha_jogador == "pedra" and escolha_computador == "tesoura" or escolha_jogador == "papel" and escolha_computador == "pedra" or escolha_jogador == "tesoura" and escolha_computador == "papel":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador}. {escolha_jogador.upper()} ganha de {escolha_computador.upper()}. Jogador ganhou!")

else:
   print(f"Computador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. EMPATE!")
print("\nJogo finalizado.")