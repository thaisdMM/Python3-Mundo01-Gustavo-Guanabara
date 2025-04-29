# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("-=-" * 10)
print("Vamos jogar PAR ou ÍMPAR")
print("-=-" * 10)
vezes_jogadas = 0
while True:
    computador = randint(1, 10)
    print(computador)
    jogador = int(input("Digite um valor: "))
    escolha_jogador = input("PAR ou ÍMPAR? [P/I]").strip().upper()
    total = computador + jogador
    print(total)
    if total % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"
    print(resultado)

    # if resultado == "P":
    #     resultado = "par"
    # else:
    #     resultado = "ímpar"

    print(f"Você jogou {jogador} e o computador jogou {computador}. O total foi: {total}. ", end="")

    if resultado == escolha_jogador:
        print("Você Venceu!")
        print("Vamos jogar novamente...")
        vezes_jogadas += 1
    else:
        print("Você Perdeu. ")
        print("\nPrograma finalizado!")
        break
