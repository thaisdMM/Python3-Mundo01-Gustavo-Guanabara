# Exercício Python 108: Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

preco = float(input("Digite o preco: R$"))
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
# dá pra trocar a moeda passada como parametro:
print(
    f"Moeda tem 2 parâmetros, então dá para trocar o parâmetro R$ na função moeda para dolar {moeda.moeda(preco, 'US$')}, mas não dentro de dobro, pois dobro() só tem um parâmetro."
)
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(
    f"Aumentando de {moeda.moeda(preco)} 15%, temos {moeda.moeda(moeda.aumentar(preco, 15))}"
)
print(
    f"Reduzindo de {moeda.moeda(preco)} 20%, temos {moeda.moeda(moeda.diminuir(preco, 20))}"
)
