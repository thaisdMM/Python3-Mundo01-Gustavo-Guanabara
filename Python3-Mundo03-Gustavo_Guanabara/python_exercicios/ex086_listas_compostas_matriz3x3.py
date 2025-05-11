matriz_lista = []
linha_matriz = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        linha_matriz.append(int(input(f"Dogite um valor para [{linha}, {coluna}] ")))
        print(f"Linha_matriz: {linha_matriz}")
    matriz_lista.append(linha_matriz[:])
    linha_matriz.clear()
    print(f"Matriz no range: {matriz_lista}")
print("=-" * 30)
print(f"Matriz: {matriz_lista}")
for valor in matriz_lista:
    print(valor)
