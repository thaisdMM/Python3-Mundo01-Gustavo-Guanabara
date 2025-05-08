valores = []
for posicao in range (0,5):
    numero = int(input("Digite um valor: "))
    if posicao == 0:
        valores.append(numero)
    
    elif numero > valores[-1]:
        valores.append(numero)