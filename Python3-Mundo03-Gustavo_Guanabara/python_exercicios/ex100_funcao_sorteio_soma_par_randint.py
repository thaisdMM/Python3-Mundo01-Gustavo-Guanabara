from random import randint
from time import sleep

numeros_lista = []


def sorteio():
    print(f"Sorteadon 5 valores da lista: ", end="")
    for i in range(0, 5):
        numeros = randint(1, 10)
        numeros_lista.append(numeros)
        print(numeros, end=" ", flush=True)
        sleep(0.6)
    print("PRONTO!")
    print()


def somaPar():
    soma_pares = 0
    for valor in numeros_lista:
        if valor % 2 == 0:
            soma_pares += valor

    print(f"Somando os valores pares de {numeros_lista}, temos: {soma_pares}")


sorteio()
somaPar()
