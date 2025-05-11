# Jeito de fazer, mas não exibia as posicões corretas da lista

matriz_lista = [[], [], []]
for valor in range(0, 9):
    if valor < 3:
        matriz_lista[0].append(int(input(f"Digite um valor para {valor} ")))
    elif valor < 6:
        matriz_lista[1].append(int(input(f"Digite um valor para {valor} ")))
    else:
        matriz_lista[2].append(int(input(f"Digite um valor para {valor} ")))
# print(f"Matriz: {matriz_lista}")
for posicao, valor in enumerate(matriz_lista):
    print(f"Posicao: {posicao}")
print("=-" * 30)
for valor in matriz_lista:
    print(valor)

# codigo correto: 

matriz_lista = []
linha_matriz = []
for contador in range(0,3):
    for coluna in range(0, 3):
        coluna_matriz = print(f"Digite um valor para: [{coluna},", end="")
        for linha in range(0,1):
            linha_matriz.append(int(input(f" {linha}] ")))
            print(f"Linha_matriz: {linha_matriz}")
    matriz_lista.append(linha_matriz[:])
    linha_matriz.clear()

    print(f"Matriz no range: {matriz_lista}")   
print("=-" * 30)
print(f"Matriz: {matriz_lista}")
for valor in matriz_lista:
    print(valor)
