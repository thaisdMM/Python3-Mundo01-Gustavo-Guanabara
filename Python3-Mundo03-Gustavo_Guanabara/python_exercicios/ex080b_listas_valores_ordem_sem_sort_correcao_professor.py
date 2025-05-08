valores = []
for i in range(0, 5):
    numero = int(input("Digite um valor: "))
    if i == 0 or numero > valores[-1]:
        valores.append(numero)
        print("Adicionado ao final da lista...")
    else:
        posicao = 0
        while posicao < len(valores):
            # print(posicao)
            if numero <= valores[posicao]:
                valores.insert(posicao, numero)
                print(f"Adicionado na posicação {posicao} da lista...")
                break
            posicao += 1
print("=-" * 30)
print(f"Os valores digitados em ordem foram: {valores}")
