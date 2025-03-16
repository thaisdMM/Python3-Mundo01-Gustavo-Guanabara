from random import choice

print("-=-" * 13)
print("Vamos jogar PEDRA, PAPEL OU TESOURA")
print("-=-" * 13)

opcoes_computador = ["pedra","papel", "tesoura"]
escolha_computador = choice(opcoes_computador)
#print(escolha_computador)

escolha_jogador = input("\nDigite: pedra ou pepel ou tesoura: ").strip().lower()
print(escolha_jogador)

if escolha_computador == "pedra" and escolha_jogador == "tesoura":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. PEDRA ganha de TESOURA. Computador ganhou.")

elif escolha_jogador == "pedra" and escolha_computador == "tesoura":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador}. PEDRA ganha de TESOURA. Jogador ganhou!")
elif escolha_computador == "papel" and escolha_jogador == "pedra":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. PAPEL ganha de PEDRA. Computador ganhou!")
elif escolha_jogador == "papel" and escolha_computador == "pedra":
   print(f"\nComputador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. PAPEL ganha de PEDRA. Jogador ganhou!")
elif escolha_computador == "tesoura" and escolha_jogador == "papel":
   print(f"Computador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. TESOURA ganha de PAPEL. Computador ganhou!")
elif escolha_jogador == "tesoura" and escolha_computador == "papel":
   print(f"Computador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. TESOURA ganha de PAPEL. Jogador ganhou!")
else:
   print(f"Computador: {escolha_computador.upper()}, Jogador: {escolha_jogador.upper()}. EMPATE!")