# Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

import moeda

preco = float(input("Digite o preco: R$"))
moeda.resumo(preco, 80, 35)
moeda.resumo(preco, 12, 20)
moeda.resumo(preco)
