# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from pacote_utilidades.subpacote_moeda import moeda

preco = float(input("Digite o preco: R$"))
moeda.resumo(preco, 80, 35)
moeda.resumo(preco, 12, 20)
moeda.resumo(preco)
