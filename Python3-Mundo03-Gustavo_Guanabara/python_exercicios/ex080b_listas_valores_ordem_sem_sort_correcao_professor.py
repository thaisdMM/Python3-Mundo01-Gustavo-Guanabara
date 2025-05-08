valores = []
for posicao in range (0,5):
    numero = int(input("Digite um valor: "))
    if posicao == 0 or numero > valores[-1]:
        valores.append(numero)
    