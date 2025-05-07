# num2 = [7, 5, 0, 3, 2, 1]
# num2.insert(3,2)
# print(num2)

# num = int(input("Numero: "))
# num2.insert(2, num)
# print(num2)

valores = []
numero_comparado = posicao_lista = 0
# Nao dá para ser enumerates
# for posicao, valor in enumerate(0,5):
for posicao in range(0, 5):
    numero = int(input("Digite um valor de 0 a 10: "))
    print(f"Numero digitado: {numero}")
    print(f"Posição no range: {posicao}")
    if posicao == 0:
        if numero > 5:
            print(f"O valor {numero} foi adicionado no final da lista...")
            valores.append(numero)
            print(valores)
        elif numero <= 5:
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            valores.append(numero)
            print(f"Lista de valores: {valores}")
    # posicao_lista += 1
    # print(f"Posicao_Lista: {posicao_lista}")
    if posicao == 1:
        for valor in valores:
            print(f"VALOR: {valor}")
            # if posicao_lista == 1:
            #     print(f"Posicao_Lista: {posicao_lista}")
            #     print(f"Posição no range: {posicao}")
            #     for valor in valores:
            #         print(f"VALOR: {valor}")
            if numero <= valor:
                valores.insert(0, numero)
                print(f"O valor {numero} foi adicionado na posição 0 da lista...")
                print(f"Lista de valores: {valores}")
            elif numero >= valor:
                valores.append(numero)
                print(f"O valor {numero} foi adicionado no final da lista...")
                print(f"Lista de valores: {valores}")
            # posicao_lista += 1
            break
    if posicao == 2:
        # for position, valor in enumerate(valores):
        #     print(f"POSITION: {posicao}")
        #     print(f"VALOR: {valores}")
        if numero <= valores[0]:
            valores.insert(0, numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            print(f"Lista de valores: {valores}")
        elif numero >= valores[1]:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            print(f"Lista de valores: {valores}")
        else:
            valores.insert(1,numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
            print(f"Lista de valores: {valores}")
    if posicao == 3:
        # for position, valor in enumerate(valores):
        #     print(f"POSITION: {posicao}")
        #     print(f"VALOR: {valores}")
        if numero <= valores[0]:
            valores.insert(0, numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            print(f"Lista de valores: {valores}")
        elif numero >= valores[2]:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            print(f"Lista de valores: {valores}")
        elif numero > valores[0] and numero <= valores[1]:
            valores.insert(1,numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
            print(f"Lista de valores: {valores}")
        else:
            valores.insert(2,numero)
            print(f"O valor {numero} foi adicionado na posição 2 da lista.")
            print(f"Lista de valores: {valores}")
    if posicao == 4:
        if numero <= valores[0]:
            valores.insert(0,numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            print(f"Lista de valores: {valores}")          
        elif numero <= valores[1]:
            valores.insert(1, numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
            print(f"Lista de valores: {valores}")
        elif numero <= valores[2]:
            valores.insert(2,numero)
            print(f"O valor {numero} foi adicionado na posição 2 da lista.")
            print(f"Lista de valores: {valores}")
        elif numero <= valores[3]:
            valores.insert(3,numero)
            print(f"O valor {numero} foi adicionado na posição 3 da lista.")
            print(f"Lista de valores: {valores}")       
        else:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            print(f"Lista de valores: {valores}")


# numero_comparado = numero
# valores += [numero, ]
# posicao_lista += 1
# if posicao == 1:
#     print(f"Posição no range: {posicao}")
#     for valor in valores:
#         print(f"VALOR: {valor}")
#         if numero < valor:
#              valores.insert(0,numero)
#              print(f"Lista de valores: {valores}")
#         elif numero > valor:
#              valores.append(numero)
#              print(f"Lista de valores: {valores}")

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
