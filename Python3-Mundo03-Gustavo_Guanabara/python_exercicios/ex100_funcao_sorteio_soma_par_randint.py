# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep


def sorteio(lista):
    print(f"Sorteadon 5 valores da lista: ", end="")
    for i in range(0, 5):
        numeros = randint(1, 10)
        lista.append(numeros)
        print(numeros, end=" ", flush=True)
        sleep(0.6)
    print("PRONTO!")
    print()


def somaPar(lista):
    soma_pares = 0
    for valor in lista:
        if valor % 2 == 0:
            soma_pares += valor
    print(f"Somando os valores pares de {lista}, temos: {soma_pares}")


numeros_lista = []

sorteio(numeros_lista)
somaPar(numeros_lista)
