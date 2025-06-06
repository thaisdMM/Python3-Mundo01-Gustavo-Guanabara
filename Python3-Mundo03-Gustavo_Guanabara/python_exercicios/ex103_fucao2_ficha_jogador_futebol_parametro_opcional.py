# # Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome="<desconhecido>", gols=0):
    print(f"O jogador {nome} fez {gols} gol(s) no Campeonato.")
    # print(type(gols))


print("-" * 30)
nome = input("Nome do jogador: ").strip().title()
gols = input("Número de gols: ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == "":
    ficha(gols=gols)
    # > Não pega nome do input, vai pegar o nome definido na função(desconhecido) e o gol que foi passado aqui no input
else:
    ficha(nome, gols)
