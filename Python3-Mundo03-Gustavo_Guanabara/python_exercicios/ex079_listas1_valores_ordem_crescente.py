
valores = []
contador = 0
while True:
    if contador == 0:
        valor = int(input("Digite um valor: "))
        valores += [valor, ]
        print(f"Valore: {valores}")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        contador += 1
    else:    
        while continuar not in "NS":
            print("Resposta inválida. Digite [S/N]")
            continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        if continuar == "N":
            break
        if continuar == "S":
            valor = int(input("Digite um valor: "))
            # valores += [valor, ]
            #for i in valores:
                # print(f"i: {i}")
                # print(valores)
            if valor not in valores:
                valores += [valor, ]
                print(f"Valor {valor} adicionado com sucesso!")
                contador += 1
            elif valor in valores:
                print("Valor duplicado. Não vou adicionar.")
        # contador += 1
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        #     if valor in valores:
        #         print(f"Valor {valor} duplicado. Não vou adicionar.")        
        # else:
        #     valores += [valor, ]        
        #     print(f"Valor {valor} adicionado com sucesso!")
print(f"Você digitou {contador} valores. São: {valores}")