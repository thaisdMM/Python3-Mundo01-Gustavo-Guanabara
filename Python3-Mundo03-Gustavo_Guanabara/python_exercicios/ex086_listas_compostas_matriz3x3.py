matriz_lista = []
linha_matriz = []
#for contador in range(0, 3):
for linha in range(0, 3):
    # coluna_matriz = print(f"Digite um valor para: [{coluna},", end="")    
    for coluna in range(0, 3):
        linha_matriz.append(int(input(f"Dogite um valor para [{linha}, {coluna}] ")))
        #print(f"Digite um valor para: [{coluna},", end="")
        #linha_matriz.append(int(input(f" {linha}] ")))
        print(f"Linha_matriz: {linha_matriz}")
    matriz_lista.append(linha_matriz[:])
    linha_matriz.clear()
    print(f"Matriz no range: {matriz_lista}")
# matriz_lista.append(linha_matriz[:])
# linha_matriz.clear()

print("=-" * 30)
print(f"Matriz: {matriz_lista}")
for valor in matriz_lista:
    print(valor)
