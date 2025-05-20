from time import sleep

# MEU CÓDIGO ESTÁ ERRADO, POIS RANGE NAO CONTA O FIM CORRETAMENTE, TEM QUE USAR O WHILE
# utilizando a função abs() para printar o valor absoluto do número no passo, sem positivo ou negativo, mas no range vai continuar o passo correto, seja ele negativo ou positivo


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print("=-" * 30)
    print(f"Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}")
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
fim = int(input("Fim:       "))
passo = int(input("Passo:   "))
contador(inicio, fim, passo)
