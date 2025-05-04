# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
for i in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {i}: ")))
print(f"O valores digitados foram: {valores}")
print(
    f"O valor máximo {max(valores)} é aparece na posição: {valores.index(max(valores))}"
)
print(
    f"O valor minimo {min(valores)} é aparece na posição: {valores.index(min(valores))}"
)
posicao_maior_valor = []
posicao_menor_valor = []
for posicao, valor in enumerate(valores):
    print(f"posição {posicao}")
    print(f"valor: {valor}")
    #     print(maximo[valores])
    if valor == max(valores):
        posicao_maior_valor += [
            posicao,
        ]
        print(f"Possicao maior valor {posicao_maior_valor}")
    if valor == min(valores):
        posicao_menor_valor += [
            posicao,
        ]
        print(f"Possicao menor valor {posicao_menor_valor}")
print(f"O valor máximo {max(valores)} aparece na posição: {posicao_maior_valor}")
print(f"O menor valor digitado foi {min(valores)} na posição {posicao_menor_valor}")
# maior = menor = 0
# for posicao, valor in enumerate(valores):
#     # if posicao == 0:
#     #     maior = valor
#     #     menor = valor
#     print(f"posição {posicao}", end=" ")
#     print(f"valor: {valor}")
# if (max(valores)) in enumerate(valores):
#     print(f"O maior valor digitado foi {max(valores)} na posiçao {posicao}")
# print(f"O menor valor digitado foi {min(valores)} na posição {posicao}")
