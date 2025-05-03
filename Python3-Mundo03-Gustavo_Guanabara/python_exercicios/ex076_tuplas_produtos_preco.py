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
    4.20,
    "Compasso",
    9.99,
    "Mochila",
    120.32,
    "Canetas",
    22.30,
    "Livro",
    34.90,
)

print("-" * 30)
print("LISTAGEM DE PREÇOS".center(30))
print("-" * 30)
estilo = "." * 25
print(f"Tupla normal: {produtos_precos}")

tupla_strings = tupla_float =()

for indice in range (0, len(produtos_precos)):
    if indice % 2 == 0:
        print(produtos_precos[indice])
        tupla_strings += (produtos_precos[indice], )
    else:
        print(produtos_precos[indice])
        tupla_float += (produtos_precos[indice], )
print(f"Tupla de produtos: {tupla_strings}")
print(f"Tupla de preços: {tupla_float}")
ordem_preco = sorted(tupla_float)
print(f"Ordem de preço: {ordem_preco}")
print(len(produtos_precos))
# for produtos in range(len(tupla_strings, len(tupla_float))):
#     print(f"{produtos} {estilo} R${produtos}")

# ERRO LEN
# for produtos in range(len(tupla_strings, len(tupla_float))):
#    print(f"{produtos} {estilo} R${produtos}")
# TypeError: len() takes exactly one argument (2 given)
# 
#  ERRO SPLIT
# tupla_separada = (produtos_precos.split())
# print(tupla_separada)
# AttributeError: 'tuple' object has no attribute 'split'


# ERRO SORTED COM STRING E FLOAT
# print(f"Tupla ordenada: {sorted(produtos_precos)}")
# TypeError: '<' not supported between instances of 'float' and 'str'

# for produtos in range(0, len(produtos_precos)):
#     print(f"{produtos_precos[produtos]} {estilo}", end="")
#     print(f"R${produtos_precos[produtos]}")
