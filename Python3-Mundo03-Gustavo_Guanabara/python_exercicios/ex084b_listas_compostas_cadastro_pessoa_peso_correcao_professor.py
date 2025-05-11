lista_pessoas = []
dados = []
maior_peso = menor_peso = 0

while True:
    dados.append(input("Nome: "))
    dados.append(float(input("Peso: ")))
    if len(lista_pessoas) == 0:  # não cadastrou ninguém ainda
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    lista_pessoas.append(dados[:])
    dados.clear()
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar in "N":
        break

print("-=" * 30)
print(f"O dados foram {lista_pessoas}")
print(f"Ao todo, você cadastrou {len(lista_pessoas)} pessoas.")
print(f"O maior peso foi de {maior_peso}Kg. Peso de ", end="")
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        print(f"[{pessoa[0]}]", end="")
print()
print(f"O menor peso foi de {menor_peso}Kg. Peso de ", end="")
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f"[{pessoa[0]}]", end="")
print()
