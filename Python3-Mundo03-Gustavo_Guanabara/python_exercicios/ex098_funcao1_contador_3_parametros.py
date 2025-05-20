# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada

from time import sleep

# utilizando a função abs() para printar o valor absoluto do número no passo, sem positivo ou negativo, mas no range vai continuar o passo correto, seja ele negativo ou positivo


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print("=-" * 30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(1)
    if inicio < fim:
        contagem = inicio
        while contagem <= fim:
            print(f"{contagem}", end=" ", flush=True)
            sleep(0.6)
            contagem += passo
        print("FIM!")
    else:
        contagem = inicio
        while contagem >= fim:
            print(f"{contagem}", end=" ", flush=True)
            sleep(0.6)
            contagem -= passo
        print("FIM!")


contador(1, 10, 1)
contador(10, 0, 2)
print("=-" * 30)
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
