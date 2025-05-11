# matriz_lista = []
# linha_matriz = []
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         linha_matriz.append(int(input(f"Dogite um valor para [{linha}, {coluna}] ")))
#         print(f"Linha_matriz: {linha_matriz}")
#     matriz_lista.append(linha_matriz[:])
#     linha_matriz.clear()
#     print(f"Matriz no range: {matriz_lista}")
# print("=-" * 30)
# print(f"Matriz: {matriz_lista}")
# for valor in matriz_lista:
#     print(valor)

# TENTATIVA DE FAZER IGUAL O DO PROFESSOR, POIS A EXIBIÇÃO DO RESULTADO DO MEU ESTAVA ERRADA.
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
for posicao, valor in enumerate(matriz_lista):
    if posicao < 3:
        print(valor, end=" ")
    if posicao < 6:
        print(f"{valor}", end=" ")
        print()
    else:
        print(valor, end=" ")
