# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz_lista = []
numeros_matriz = []
numero = par = soma_par = soma_terceira_coluna = 0
for linha in range(0, 3):
    for coluna in range(0, 3):

        # #PARES PODERIA SER ASSIM TAMBÉM:
        # numero = (int(input(f"Digite um valor para [{linha}, {coluna}] ")))
        # if numero % 2 == 0:
        #     soma_par += numero
        #     par += 1
        # numeros_matriz.append(numero)

        numeros_matriz.append(int(input(f"Digite um valor para [{linha}, {coluna}] ")))
    matriz_lista.append(numeros_matriz[:])
    numeros_matriz.clear()
for linha in range(0, 3):
    for coluna in range(0, 3):
        # if matriz_lista[linha] % 2 == 0 or matriz_lista[coluna] % 2 == 0:
        #     par += 1
        #     print(par)
        print(f"[{matriz_lista[linha][coluna]:^5}]", end="")
    print()

for valor in matriz_lista:
    print(f"Linha: {valor}")
    for linha in valor:
        print(f"linha_valor {linha}")
        if linha % 2 == 0:
            soma_par += linha
            par += 1
            print(par)
    if valor == 1:
        for linha in valor:
            print(f"Maximo {max(linha)}")
for valor in matriz_lista:
    print(valor[2])
    soma_terceira_coluna += valor[2]

# for valor in matriz_lista:
#     for coluna in valor:
#         print(coluna)
#         soma_terceira_coluna += coluna

# for valor in matriz_lista:
#     for coluna in valor:
#         if valor == 2:
#             print(coluna)
#             soma_terceira_coluna += coluna


print(f"O total de números pares da matriz é {par} e a soma deles é {soma_par}")
print(f"A soma da terceira coluna é {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é {max(matriz_lista[1])}")
