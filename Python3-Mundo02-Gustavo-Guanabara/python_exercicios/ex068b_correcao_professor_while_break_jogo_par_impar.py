from random import randint

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,10)
    total = jogador + computador
    tipo = input("Par ou Ímpar?")

    print(f"Você jogou {jogador} e o computador {computador}. O total foi {total}")