# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
computador = randint(1,10)
print(computador)

print("-=-" * 10)
print("Vamos jogar PAR ou ÍMPAR")
print("-=-" * 10)

while True:
    jogador = int(input("Digite um valor: "))
    escolha_jogador = input("PAR ou ÍMPAR? [P/I]").strip().upper()
    numeros_jogados = computador + jogador
    print(numeros_jogados)
    if numeros_jogados % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    print(resultado)
    
    if resultado == escolha_jogador:
        print("Você Venceu!")
    else:
        print("Você Perdeu.")
        break