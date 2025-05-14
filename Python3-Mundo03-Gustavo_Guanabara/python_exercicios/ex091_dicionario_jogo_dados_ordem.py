from random import randint
from time import sleep
from operator import itemgetter

lista_jogos = []
jogo_dados = {
    "jogador1": randint(1, 6),
    "jogador2": randint(1, 6),
    "jogador3": randint(1, 6),
    "jogador4": randint(1, 6),
}
ranking = list()
print(">" * 7, f"{' JOGO DE DADOS ':^10}", "<" * 7)
# print(f"jogo_dados: {jogo_dados}")
# print(f"key: {jogo_dados.keys()}")
# print(f"value: {jogo_dados.values()}")
print("=-" * 15)
print(f"{'Valores sorteados':^30}")
print("=-" * 15)
sleep(1)
for key, value in jogo_dados.items():
    sleep(1)
    print(f"O {key} tirou: {value}")
print("=-" * 15)
print(f"{'RANKING DOS JOGADORES:':^30}")
print("=-" * 15)
ranking = sorted(jogo_dados.items(), key=itemgetter(1), reverse=True)
# print(ranking)
for posicao, valor in enumerate(ranking):
    print(f"{posicao+1}° lugar: {valor[0]} com {valor[1]}")
    sleep(1)
