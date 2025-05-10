# matriz_lista = [[], [], []]
# for valor in range(0, 9):
#     if valor < 3:
#         matriz_lista[0].append(int(input(f"Digite um valor para {matriz_lista[0]} ")))
#     elif valor < 6:
#         matriz_lista[1].append(int(input(f"Digite um valor para {valor} ")))
#     else:
#         matriz_lista[2].append(int(input(f"Digite um valor para {valor} ")))
# # print(f"Matriz: {matriz_lista}")
# for posicao, valor in enumerate(matriz_lista):
#     print(f"Posicao: {posicao}")
# print("=-" * 30)
# for valor in matriz_lista:
#     print(valor)


for contador in range(0, 9):
    matriz_lista = [[], [], []]
    if contador < 3:
       
        for linha in matriz_lista:
            matriz_lista[0].append(int(input(f"Digite um valor para {matriz_lista[linha]} ")))
#         elif valor < 6:
#             matriz_lista[1].append(int(input(f"Digite um valor para {valor} ")))
#         else:
#             matriz_lista[2].append(int(input(f"Digite um valor para {valor} ")))
# # print(f"Matriz: {matriz_lista}")
for posicao, valor in enumerate(matriz_lista):
    print(f"Posicao: {posicao}")
print("=-" * 30)
for valor in matriz_lista:
    print(valor)
