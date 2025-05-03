produtos_precos = (
    "Livro",
    34.90,
    "Lápis",
    1.75,
    "Canetas",
    22.30,
    "Caderno",
    15.90,
    "Mochila",
    120.32,
    "Boracha",
    2.00,
    "Compasso",
    9.99,
    "Estojo",
    25.00,
    "Transferidor",
    4.20,
)
# Não é o que queremos
# print(produtos_precos)
# for item in produtos_precos:
#     print(item)
print("-" * 40)
print(f"{'LISTAGEM DE PREÇOS':^40}")
print("-" * 40)

for posicao in range(0, len(produtos_precos)):
    if posicao % 2 == 0:  # aqui temos o nome do produto, sempre é par nessa tupla
        print(f"{produtos_precos[posicao]:.<30}", end="")
    # nesse else que são os números ímpares, temos os preços
    else:
        print(f"R${produtos_precos[posicao]:>7.2f}")
print("-" * 40)
