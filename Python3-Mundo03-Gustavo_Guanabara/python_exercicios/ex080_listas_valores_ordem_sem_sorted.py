valores = []

for posicao in range(0, 5):
    numero = int(input("Digite um valor: "))
    # print(f"Numero digitado: {numero}")
    # print(f"Posição no range: {posicao}")
    if posicao == 0:
        if numero > 5:
            print(f"O valor {numero} foi adicionado no final da lista...")
            valores.append(numero)
            # print(valores)
        elif numero <= 5:
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            valores.append(numero)
            # print(f"Lista de valores: {valores}")
    if posicao == 1:
        for valor in valores:
            # print(f"VALOR: {valor}")
            if numero <= valor:
                valores.insert(0, numero)
                print(f"O valor {numero} foi adicionado na posição 0 da lista...")
                # print(f"Lista de valores: {valores}")
            elif numero >= valor:
                valores.append(numero)
                print(f"O valor {numero} foi adicionado no final da lista...")
                # print(f"Lista de valores: {valores}")
            break
    if posicao == 2:
        if numero <= valores[0]:
            valores.insert(0, numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            # print(f"Lista de valores: {valores}")
        elif numero >= valores[1]:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            # print(f"Lista de valores: {valores}")
        else:
            valores.insert(1, numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
            # print(f"Lista de valores: {valores}")
    if posicao == 3:
        if numero <= valores[0]:
            valores.insert(0, numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            # print(f"Lista de valores: {valores}")
        elif numero >= valores[2]:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            # print(f"Lista de valores: {valores}")
        elif numero > valores[0] and numero <= valores[1]:
            valores.insert(1, numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
            # print(f"Lista de valores: {valores}")
        else:
            valores.insert(2, numero)
            print(f"O valor {numero} foi adicionado na posição 2 da lista.")
            # print(f"Lista de valores: {valores}")
    if posicao == 4:
        if numero <= valores[0]:
            valores.insert(0, numero)
            print(f"O valor {numero} foi adicionado na posição 0 da lista...")
            # print(f"Lista de valores: {valores}")
        elif numero <= valores[1]:
            valores.insert(1, numero)
            print(f"O valor {numero} foi adicionado na posição 1 da lista...")
        # print(f"Lista de valores: {valores}")
        elif numero <= valores[2]:
            valores.insert(2, numero)
            print(f"O valor {numero} foi adicionado na posição 2 da lista.")
            # print(f"Lista de valores: {valores}")
        elif numero <= valores[3]:
            valores.insert(3, numero)
            print(f"O valor {numero} foi adicionado na posição 3 da lista.")
            # print(f"Lista de valores: {valores}")
        else:
            valores.append(numero)
            print(f"O valor {numero} foi adicionado no final da lista...")
            # print(f"Lista de valores: {valores}")

print(f"O valores digitados foram: {valores}")
