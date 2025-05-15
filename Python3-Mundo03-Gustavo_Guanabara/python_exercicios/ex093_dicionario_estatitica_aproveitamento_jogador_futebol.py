aproveitamento_jogador = {}
gols_por_partida = []
total_gols = 0
aproveitamento_jogador["nome"] = input("Nome do jogador: ").strip().capitalize()
partidas = int(input("Quantas partidas ele jogou? "))
# print(f"dicionário aproveitamento_jogador {aproveitamento_jogador}")
for gols in range(1, partidas + 1):
    gols_marcados = int(input(f"Quantos gols na partida  {gols}? "))
    total_gols += gols_marcados
    gols_por_partida.append(gols_marcados)
    # print(f"lista: {gols_por_partida}")
# print(f"lista de gols por partida: {gols_por_partida}")
# print(f"total de gols marcados {total_gols}")
aproveitamento_jogador["gols"] = gols_por_partida
# print(f"lista {aproveitamento_jogador}")
aproveitamento_jogador["total"] = total_gols
print("=-" * 30)
print(f"{aproveitamento_jogador}")
print("=-" * 30)
for key, value in aproveitamento_jogador.items():
    print(f"O campo {key} tem o valor: {value}.")
print("=-" * 30)
print(f"O jogador {aproveitamento_jogador['nome']} jogou {partidas} partidas.")
for partida, valor in enumerate(gols_por_partida):
    print(f"=> Na partida {partida+1}, fez {valor} gols.")
print(f"Foi um total de {aproveitamento_jogador['total']} gols.")
# for i in range(1, partidas+1):
#     for valor in gols_por_partida:
#         print(f"=> Na partida {i}, fez {valor} gols.")
# for value in aproveitamento_jogador["gols"].values():
#     print(f"{i} aproveitamento_jogador[gols] {aproveitamento_jogador['gols']}")
#     print(value)
