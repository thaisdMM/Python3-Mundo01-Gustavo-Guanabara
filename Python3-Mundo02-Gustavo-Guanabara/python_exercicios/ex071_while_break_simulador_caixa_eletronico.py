print("-" * 15)
print("BANCO MOREIRA")
print("-" * 15)
cedulas_50 = cedulas_20 = cedulas_10 = 0
while True:
    valor = int(input("Qual o valor você quer sacar? R$ "))

    
    for i in range(valor):
        if valor / 50:
            cedulas_50 = valor // 50
        if (valor % 50 != 0) / 20:
            cedulas_20 = (valor % 50) // 20
        if (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) / 10:
            cedulas_10 = (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) // 10
        #if valor % 20 != 0: # and (valor % 20) / 10:
        #    cedulas_10 = (valor % 20) // 10
        #print(valor / 50)

    # if valor % 50 == 0:
    #     cedulas_50 = valor / 50

    # elif valor % 20 == 0:
    #     cedulas_20 = valor / 20
    break
    # if valor % 50 == 0:
    #     cedulas_50 +=1

        #for i in range(0,valor + 1):
        
            
    # if valor - 0 == 0:
    #     break
print(f"Total de {cedulas_50} cedulas de R$50")
print(f"Total de {cedulas_20} cédulas de R$20")
print(f"Total de {cedulas_10} cédulas de R$10")

print("\nFim do Programa.")
