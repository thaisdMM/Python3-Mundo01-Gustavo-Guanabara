produtos_precos = (
    "Lápis",
    1.75,
    "Boracha",
    2.00,
    "Caderno",
    15.90,
    "Estojo",
    25.00,
    "Transferidor",
    4,
    20,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Canetas",
    22.30,
    "Livro",
    34,
    90,
)

print("-" * 30)
print("LISTAGEM DE PREÇOS".center(30))
print("-" * 30)
estilo = "." * 25
print(f"Tupla normal: {produtos_precos}")

# ERRO SPLIT
# tupla_separada = (produtos_precos.split())
# print(tupla_separada)
# AttributeError: 'tuple' object has no attribute 'split'


# ERRO SORTED COM STRING E FLOAT
# print(f"Tupla ordenada: {sorted(produtos_precos)}")
# TypeError: '<' not supported between instances of 'float' and 'str'

# for produtos in range(0, len(produtos_precos)):
#     print(f"{produtos_precos[produtos]} {estilo}", end="")
#     print(f"R${produtos_precos[produtos]}")
