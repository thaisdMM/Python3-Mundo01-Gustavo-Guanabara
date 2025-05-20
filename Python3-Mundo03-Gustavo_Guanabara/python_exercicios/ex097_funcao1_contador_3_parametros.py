from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
        print("=-" * 30)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if passo < 0 and inicio > fim:
        print("=-" * 30)
        print(f"Contagem de {inicio} até {fim} de {-passo} em {-passo}")
    elif inicio > fim:
        passo = -(passo)
        print("=-" * 30)
        print(f"Contagem de {inicio} até {fim} de {-passo} em {-passo}")

    else:
        print("=-" * 30)
        print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    for i in range(inicio, fim + passo, passo):
        # sleep(0.5)
        print(f"{i}", end=" ", flush=True)
        sleep(0.5)
    print("FIM!")
    print()


contador(1, 10, 1)
contador(10, 0, 2)

print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
