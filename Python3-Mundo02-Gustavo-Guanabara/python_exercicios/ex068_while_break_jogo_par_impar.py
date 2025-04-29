# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print("-=-" * 10)
print("Vamos jogar PAR ou ÍMPAR")
print("-=-" * 10)
vezes_jogadas = 0
while True:
    computador = randint(0, 10)
    # print(computador)
    jogador = int(input("Digite um valor: "))
    escolha_jogador = " "
    while escolha_jogador not in "PI":
        escolha_jogador = input("PAR ou ÍMPAR? [P/I]").strip().upper()[0]
    if escolha_jogador == "P":
        escolha_jogador = "par"
    else:
        escolha_jogador = "ímpar"

    total = computador + jogador
    # print(total)
    if total % 2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"
    # print(resultado)

    print("_" * 80)
    print(
        f"Você jogou {jogador} e o computador jogou {computador}. O total foi: {total} e o resultado foi {resultado}. "
    )
    print("_" * 80)

    if resultado == escolha_jogador:
        print("Você Venceu!")
        print("Vamos jogar novamente...")
        print("-=-" * 10)
        vezes_jogadas += 1
    else:
        print(f"Você Perdeu. Você acertou {vezes_jogadas} vezes seguidas.")
        print("\nPrograma finalizado!")
        break
