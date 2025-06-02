# # Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários

from pacote_utilidades.subpacote_dado import dado
from pacote_utilidades.subpacote_moeda import moeda

preco = dado.leiaDinheiro("Digite o preco: R$")
moeda.resumo(preco, 35, 22)
#moeda.resumo(preco, 80, 35)
# moeda.resumo(preco, 12, 20)
# moeda.resumo(preco)
