from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -(passo)
    # utilizando a função abs() para printar o valor absoluto do número no passo, sem positivo ou negativo, mas no range vai continuar o passo correto, seja ele negativo ou positivo
    print("=-" * 30)
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}")
    for i in range(inicio, fim + passo, passo):
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
