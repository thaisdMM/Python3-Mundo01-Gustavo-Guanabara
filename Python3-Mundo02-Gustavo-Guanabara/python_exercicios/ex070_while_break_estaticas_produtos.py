# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# MEU CÓDIGO:

#  print("-" * 20)
# print("LOJAS SUPER PREÇO")
# print("-" * 20)
# total_compra = produto_mais_1000 = total_produtos = menor_preco = 0
# produto_mais_barato = False
# nome_produto_mais_barato = " "

# while True:
#     nome_produto = input("Nome do Produto: ").strip()
#     preco = float(input("Preço: R$"))

#     total_compra += preco
#     if preco > 1000:
#         produto_mais_1000 += 1
#     total_produtos += 1

#     if not produto_mais_barato:
#         produto_mais_barato = True
#         nome_produto_mais_barato = nome_produto
#         menor_preco = preco
#     else:
#         if menor_preco > preco:
#             nome_produto_mais_barato = nome_produto
#             menor_preco = preco

#     continuar = " "
#     while continuar not in "SN":
#         continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
#     if continuar == "N":
#         break
# print(f"O total de produtos comprado foi: {total_produtos}")
# print(f"O valor total da compra foi: R${total_compra:.2f}")
# print(f"A quantidade de produtos acima de R$1000,00 é: {produto_mais_1000}")
# print(
#     f"O nome do produto mais barato é {nome_produto_mais_barato} e o preço desse produto é {menor_preco:.2f}."
# )
# print("\n{:-^40}".format(" PROGRAMA FINALIZADO! "))

# correção PROFESSOR

print("-" * 20)
print("LOJAS SUPER PREÇO")
print("-" * 20)
total_compra = produto_mais_1000 = total_produtos = menor_preco = 0
nome_produto_mais_barato = " "

while True:
    nome_produto = input("Nome do Produto: ").strip()
    preco = float(input("Preço: R$"))
    total_produtos += 1

    total_compra += preco
    if preco > 1000:
        produto_mais_1000 += 1

    if total_produtos == 1 or preco < menor_preco:
        menor_preco = preco
        nome_produto_mais_barato = nome_produto
    # dá para eliminar o codigo abaixo colocando um or no codigo de cima
    #  else:
    #     if preco < menor_preco:
    #         menor_preco = preco
    #         nome_produto_mais_barato = nome_produto

    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print(f"O total de produtos comprado foi: {total_produtos}")
print(f"O valor total da compra foi: R${total_compra:.2f}")
print(f"A quantidade de produtos acima de R$1000,00 é: {produto_mais_1000}")
print(
    f"O nome do produto mais barato é {nome_produto_mais_barato} e o preço desse produto é {menor_preco:.2f}."
)
print("\n{:-^40}".format(" PROGRAMA FINALIZADO! "))
