# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep


def maior(*numero):
    print("=-" * 30)
    print(f"Analizando os valores passados...")
    tamanho = len(numero)
    # essa função retorna uma tupla
    # se a tupla for vazia entao o tamanho dela é == 0 significa que não tem nada nela
    ## tem que adicionar o if abaixo pois utilizando a função max() dá erro para a função maior() sem parâmetro
    if tamanho == 0:
        print(f"Foram informados 0 números.")
        print(f"O maior valor informado foi 0.")
    else:
        maior_numero = max(numero)
        for valor in numero:
            print(valor, end=" ", flush=True)
            sleep(0.6)
        print()
        print(f"Foram informados {tamanho} números.")
        print(f"O maior valor informado foi {maior_numero}.")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

# RESPOSTA DO PROFESSOR:
# a resposta dele não dá erro no vazio que tive que resolver com o len(numero) == 0


def maior(*numero):
    contador = maior = 0
    print("=-" * 25)
    print("Analizando os valores passados...")
    for valor in numero:
        print(f"{valor} ", end="", flush=True)
        sleep(0.3)
        if contador == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
    print(f"Foram informados {contador} números ao todo.")
    print(f"O maior valor informado foi {maior}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
