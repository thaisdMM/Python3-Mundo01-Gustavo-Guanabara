# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input("Digite o preco: R$"))
print(f"O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}")
print(f"A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}")
print(
    f"Aumentando de {moeda.moeda(preco)} 15%, temos {moeda.aumentar(preco, 15, True)}"
)
print(f"Reduzindo de {moeda.moeda(preco)} 20%, temos {moeda.diminuir(preco, 20, True)}")
