from time import sleep


def maior(*numero):
    print("=-" * 30)
    print(f"Analizando os valores passados...")
    tamanho = len(numero)
    # essa função retorna uma tupla
    # se a tupla for vazia entao o tamanho dela é == 0 significa que não tem nada nela
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
