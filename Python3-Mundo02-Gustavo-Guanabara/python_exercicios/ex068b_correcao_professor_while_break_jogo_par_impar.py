from random import randint

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = input("Par ou Ímpar? ").strip().upper()[0]

    print(f"Você jogou {jogador} e o computador {computador}. O total foi {total}")
