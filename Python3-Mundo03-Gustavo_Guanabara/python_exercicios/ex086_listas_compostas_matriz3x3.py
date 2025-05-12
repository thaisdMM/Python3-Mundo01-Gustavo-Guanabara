# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz_lista = []
numeros_matriz = []
for linha in range(0, 3):
    for coluna in range(0, 3):
        numeros_matriz.append(int(input(f"Digite um valor para [{linha}, {coluna}] ")))
        # print(f"Linha_matriz: {linha_matriz}")
    matriz_lista.append(numeros_matriz[:])
    numeros_matriz.clear()
    # print(f"Matriz no range: {matriz_lista}")
print("=-" * 30)
# print(f"Matriz: {matriz_lista}")
# # aqui não imprime com a formatação do professor, por isso o código abaixo para imprimir 1 a 1 [] formatado
# for valor in matriz_lista:
#     print(f"[{valor}]")
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_lista[linha][coluna]:^5}]", end="")
    print()

# Correção do PROFESSOR

matriz_lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz_lista[linha][coluna] = int(
            input(f"\nDigite um valor para a [{linha}, {coluna}] ")
        )
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz_lista[linha] [coluna]:^5}]", end="")
    print()
