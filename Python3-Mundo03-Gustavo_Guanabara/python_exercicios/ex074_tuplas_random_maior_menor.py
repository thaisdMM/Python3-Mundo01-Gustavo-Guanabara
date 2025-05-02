from random import randint
maior = menor = contador = 0
numeros_aletorios_tupla = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(numeros_aletorios_tupla)
for maior_menor in numeros_aletorios_tupla:
    print(f"I: {maior_menor}")
    contador += 1
    #print(numeros_aletorios_tupla[0])
    if contador == 1:
        maior = maior_menor
        menor = maior_menor
    else:
        if maior < maior_menor:
            maior = maior_menor
        if menor > maior_menor:
            menor = maior_menor
    print(f"MAIOR: {maior}")
    print(f"MENOR: {menor}")
    print(contador)

#     # if numeros_aletorios_tupla[0]:
#     #      maior = menor = numeros_aletorios_tupla[0]
#     # else:
#     #      if maior < numeros_aletorios_tupla:
#     #           maior = numeros_aletorios_tupla
#     #      if menor > numeros_aletorios_tupla:
#     #           menor = numeros_aletorios_tupla
#     print(f"Maior número: {maior}")
#     print(f"Menor número: {menor}")
#     contador += 1
#     print(contador)

# # numeros_aletorios_tupla = int()
# # for numeros_aletorios in range (1,5):
# #     numeros_aletorios = randint(0,10)
# #     print(numeros_aletorios)
# #     numeros_aletorios_tupla += (numeros_aletorios)
# # print(numeros_aletorios_tupla)

# # numeros_tupla = (0,1,2,3,4,5,6,7,8,9,10)
# # print(sample(numeros_tupla), k=5)
# print(numeros_aletorios_tupla)
# print(type(numeros_aletorios_tupla))
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")