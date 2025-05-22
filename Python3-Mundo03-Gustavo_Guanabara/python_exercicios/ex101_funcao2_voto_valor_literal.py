# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import date


def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 18:
        votar = "NÃO VOTA"
    elif idade >= 65:
        votar = "VOTO OPCIONAL"
    else:
        votar = "VOTO OBRIGATÓRIO"
    return idade, votar


print("-" * 30)
ano_nascimento = int(input("Em que ano você nasceu? "))
# print(voto(ano_nascimento))
# desempacotando uma tupla: o return idade, votar retorna uma tupla: (20, 'VOTO OBRIGATÓRIO')
# desempacotar é: você “abre” o pacote da tupla e guarda os itens em variáveis separadas de uma vez só.
# desempacotando abaixo:
idade, votar = voto(ano_nascimento)
## OBS: dava para chegar ao mesmo resultado acessando os indíces da tupla, como abaixo:
# print(f"Com {voto(ano_nascimento)[0]} anos: {voto(ano_nascimento)[1]}")
print(f"Com {idade} anos: {votar}")
