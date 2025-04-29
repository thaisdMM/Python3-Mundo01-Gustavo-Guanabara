# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print("-" * 20)
print("LOJAS SUPER PREÇO")
print("-" * 20)
total_compra = produto_mais_1000 = total_produtos = 0

while True:
    nome_produto = input("Nome do Produto: ").strip()
    preco = float(input("Preço: R$"))

    total_compra += preco
    if preco > 1000:
        produto_mais_1000 += 1
    total_produtos += 1
    continuar = " "
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print(f"O total de produtos comprado foi: {total_produtos}")
print(f"O valor total da compra foi: R${total_compra}")
print(f"A quantidade de produtos acima de R$1000,00 é: {produto_mais_1000}")
print("\nPROGRAMA FINALIZADO!")
