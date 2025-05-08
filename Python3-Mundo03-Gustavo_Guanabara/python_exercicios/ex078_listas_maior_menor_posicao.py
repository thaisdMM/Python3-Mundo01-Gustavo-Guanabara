# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))
print(f"O valores digitados foram: {valores}")
# print(f"O valor máximo {max(valores)} é aparece na posição: {valores.index(max(valores))}")
# print(f"O valor minimo {min(valores)} é aparece na posição: {valores.index(min(valores))}")

# # usei uma variável para salvar a posição do maior e do menor valor, mas depois acabai exibindo esses valores com o print no for, entao nao foi necessário manter essa variável
# posicao_maior_valor = []
# posicao_menor_valor = []

print(f"O valor máximo {max(valores)} aparece na posição: ", end="")
for posicao, valor in enumerate(valores):
    # print(f"posição {posicao}")
    # print(f"valor: {valor}")
    if valor == max(valores):
        print(f"{posicao}... ", end="")
        # posicao_maior_valor += [posicao,]
        # print(f"Possicao maior valor {posicao_maior_valor}")
print(f"\nO menor valor digitado foi {min(valores)} na posição: ", end="")
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print(f"{posicao}... ", end="")
        # posicao_menor_valor += [posicao,]
        # print(f"Possicao menor valor {posicao_menor_valor}")
# print(f"O valor máximo {max(valores)} aparece na posição: {posicao_maior_valor}")
# print(f"O menor valor digitado foi {min(valores)} na posição {posicao_menor_valor}")

# CORREÇÃO PROFESSOR:

lista_numero = []
maior = 0
menor = 0
for posicao in range(0, 5):
    lista_numero.append(int(input(f"Digite um valor para a posição {posicao} ")))
    if posicao == 0:
        maior = menor = lista_numero[posicao]
    else:
        if lista_numero[posicao] > maior:
            maior = lista_numero[posicao]
        if lista_numero[posicao] < menor:
            menor = lista_numero[posicao]

print("=-" * 30)
print(f"Você digitou os valores {lista_numero}")
print(f"O maior valor digitado foi {maior} nas posições ", end="")
for indice, valor in enumerate(lista_numero):
    if valor == maior:
        print(f"{indice}... ", end="")
print()  # para quebrar de linha
print(f"O menor valor digitado foi {menor} nas posições ", end="")
for indice, valor in enumerate(lista_numero):
    if valor == menor:
        print(f"{indice}...", end="")
print()
