from random import randint

vitoria = 0
while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = input("Par ou Ímpar? [P/I] ").strip().upper()[0]

    print(
        f"Você jogou {jogador} e o computador {computador}. O total foi {total}. ",
        end="",
    )
    print("Deu PAR" if total % 2 == 0 else "Deu ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
    if tipo == "I":
        if total % 2 == 1:
            print("Você VENCEU!")
            vitoria += 1
        else:
            print("Você PERDEU!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vitoria} vezes.")
