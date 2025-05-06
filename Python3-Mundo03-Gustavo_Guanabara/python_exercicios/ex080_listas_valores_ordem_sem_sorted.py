valores = []
numero_comparado = posicao_lista = 0
# Nao dá para ser enumerates
# for posicao, valor in enumerate(0,5):
for posicao in range(0, 5):
    numero = int(input("Digite um valor de 0 a 10: "))

    if numero >  5:
            print(f"O valor {numero} foi adicionado no final da lista...")
            valores.append(numero)
            print(valores)
    elif numero <= 5:
        print(f"O valor {numero} foi adicionado na posição 0 da lista...")
        valores.append(numero)
   # numero_comparado = numero
   # valores += [numero, ]
    posicao_lista += 1
    if posicao == 1:
        for valor in valores:
            if numero < valor:
                 valores.insert(0,numero)
                 print(valores)
                 break
           # posicao
        # if numero < numero[0]:
            # print("Valor menor")

    # if posicao == 0:
    #     valores += [
    #         numero,
    #     ]
    #     # valores.append(numero)
    #     # posicao += 1
    #     print(valores)
    #     print(posicao)
    # if posicao != 0:
    #     for valor in valores:
    #         if numero > valor:
    #             print(f"O valor {numero} foi adicionado no final da lista...")
    #             valores.append(numero)
    #         elif numero < valor:
    #             valores.insert(0, numero)
    #     # posicao += 1
    #     print(valores)
    #     print(posicao)


# valores += [numero, ]
#     if posicao == 0:
#         if numero > 5:
#             print(f"O valor {numero} foi adicionado no final da lista...")
#             valores.insert(5,numero)
#             print(valores)
#         elif numero <= 5:
#             print(f"O valor {numero} foi adicionado na posição 0 da lista...")
#         numero_comparado = numero
#    # valores += [numero, ]
#     if posicao == 1:
#         if numero < numero_comparado:
#             posicao
#         # if numero < numero[0]:
#             print("Valor menor")

print(f"O valores digitados foram: {valores}")
