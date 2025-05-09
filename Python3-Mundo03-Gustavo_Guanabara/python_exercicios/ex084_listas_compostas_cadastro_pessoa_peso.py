# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista_pessoas = list()
dados = list()
lista_maior_peso = list()
lista_menor_peso = list()
maior_peso = 0
menor_peso = 0
while True:
    dados.append(input("Nome: ").strip())
    dados.append(float(input("Peso: ")))
    lista_pessoas.append(dados[:])
    dados.clear()
    # print(f"Lista de pessoas: {lista_pessoas}")
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break

print(f"Ao todo você cadastrou {len(lista_pessoas)} pessoas.")
print(f"A lista de pessoas cadastrada foi: {lista_pessoas}")

for posicao, peso in enumerate(lista_pessoas):
    # print(f"Posicao enumarates: {posicao}")
    # print(f"maior_peso: {maior_peso}")
    # print(f"menor_peso: {menor_peso}")
    if posicao == 0:
        # print(f"POSICAO[0] {posicao}")
        if peso[1]:
            maior_peso = peso[1]
            menor_peso = peso[1]
            # print(f"maior_peso: {maior_peso}")
            # print(f"menor_peso: {menor_peso}")
    else:
        if peso[1] >= maior_peso:
            # print(f"Peso 1 {peso[1]}")
            maior_peso = peso[1]
            # print(f"maior_peso: {maior_peso}")
        if peso[1] <= menor_peso:
            # print(f"Peso 1 {peso[1]}")
            menor_peso = peso[1]
            # print(f"menor_peso: {menor_peso}")
for pessoa in lista_pessoas:
    # print(pessoa)
    if pessoa[1] == maior_peso:
        lista_maior_peso.append(pessoa[0])
    if pessoa[1] == menor_peso:
        lista_menor_peso.append(pessoa[0])

print(f"O maior peso da lista foi {maior_peso} e as pessoas foram: {lista_maior_peso}")
print(
    f"\nO menor peso da lista foi {menor_peso} e as pessoas foram: {lista_menor_peso}"
)
print("Programa finalizado.")
