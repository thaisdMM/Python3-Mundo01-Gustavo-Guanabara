from random import randint
from time import sleep

lista_jogos = []
jogo_dados = {"jogador1": randint(1,6), "jogador2": randint(1,6), "jogador3": randint(1,6), "jogador4": randint(1,6)}
print(f"jogo_dados: {jogo_dados}")
# print(f"key: {jogo_dados.keys()}")
# print(f"value: {jogo_dados.values()}")
print("=-" * 15)
print(f"{'JOGO DE DADOS':^30}")
print("=-" * 15)
sleep(1)
for key, value in jogo_dados.items():
    sleep(1)
    print(f"O {key} tirou: {value}")
print("=-" * 15)
print(f"{'RANKING DOS JOGADORES:':^30}")
print("=-" * 15)
for valor in jogo_dados.items():
    print(valor)
    lista_jogos.append(valor)
    # print(lista_jogos)
print(f"Lista de jogos {lista_jogos}")
for posicao, valor in enumerate(lista_jogos):
    print(f"posicao {posicao}")
    print(f"valor {valor}")
    print(sorted(valor[2]))

# ordenada = sorted(lista_jogos)
# #lista_jogos[1].sort()
# #print(f"Lista de jogos {lista_jogos}")
# print(ordenada)

# lista_jogos.append(jogo_dados.copy())
# # for key, value in jogo_dados:
# #     lista_jogos.append(key)
# #     lista_jogos.append(value)
# # print(lista_jogos)
# lista_jogos.sort()
# print(f"lista ordenada {lista_jogos}")
# for valor in lista_jogos:
    
# print(sorted(jogo_dados.values()))
# ordenacao_valores = sorted(jogo_dados.values())
# # if ordenacao_valores == jogo_dados
# for key, value in jogo_dados.items():
#     ordenacao_valores = sorted(jogo_dados.values())
#     print(f"{ordenacao_valores}")
#     print(value)
#     for valor in ordenacao_valores:
#         #if valor == value:
#         lista_jogos.append(key, value)
# print(lista_jogos)
            #print(f"{key} = {value}")
# for key, value in jogo_dados.items():
#     sorted(value)
#     print(f"{key} = {value}")
# print(f"dicionario com sorted {jogo_dados}")
#dado = randint(1,6)
