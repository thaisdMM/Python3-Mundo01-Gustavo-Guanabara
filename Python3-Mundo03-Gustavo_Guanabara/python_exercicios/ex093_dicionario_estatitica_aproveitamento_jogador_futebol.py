# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

aproveitamento_jogador = {}
gols_por_partida = []
# total_gols = 0
aproveitamento_jogador["nome"] = input("Nome do jogador: ").strip().title()
partidas = int(input(f"Quantas partidas {aproveitamento_jogador['nome']} jogou? "))
for gols in range(1, partidas + 1):
    gols_marcados = int(input(f"Quantos gols na partida  {gols}? "))
    gols_por_partida.append(gols_marcados)
    # print(f"lista: {gols_por_partida}")
# print(f"lista de gols por partida: {gols_por_partida}")
aproveitamento_jogador["gols"] = gols_por_partida[:]
# print(f"lista {aproveitamento_jogador}")
aproveitamento_jogador["total"] = sum(gols_por_partida)
print("=-" * 30)
print(f"{aproveitamento_jogador}")
print("=-" * 30)
for key, value in aproveitamento_jogador.items():
    print(f"O campo {key} tem o valor: {value}.")
print("=-" * 30)
print(f"O jogador {aproveitamento_jogador['nome']} jogou {partidas} partidas.")
for partida, valor in enumerate(gols_por_partida):
    print(f"    => Na partida {partida+1}, fez {valor} gols.")
print(f"Foi um total de {aproveitamento_jogador['total']} gols.")
