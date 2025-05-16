# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

aproveitamento_jogador = {}
lista_aproveitamento_jogadores = []

while True:
    # total_gols = 0
    lista_gols = []
    aproveitamento_jogador["nome"] = input("Nome do jogador: ").strip().title()
    partidas_jogadas = int(
        input(f"Quantas partidas {aproveitamento_jogador['nome']} jogou? ")
    )
    for jogos in range(1, partidas_jogadas + 1):
        gols = int(
            input(
                f"  Quantos gols {aproveitamento_jogador['nome']} marcou na partida {jogos}? "
            )
        )
        lista_gols.append(gols)
    aproveitamento_jogador["gols"] = lista_gols[:]
    aproveitamento_jogador["total"] = sum(lista_gols)
    lista_aproveitamento_jogadores.append(aproveitamento_jogador.copy())
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        print("=-" * 30)
        break
    print("-" * 50)
# print(f"lista: {lista_aproveitamento_jogadores}")
## CÓDIDO DO PROFESSOR PARA FORMATAÇÃO ABAIXO:
print("cod ", end="")
for key in aproveitamento_jogador.keys():
    print(f"{key:<15}", end="")
print()
print("-" * 40)
for posicao, value in enumerate(lista_aproveitamento_jogadores):
    print(f"{posicao +1:>3} ", end="")
    for dados in value.values():
        print(f"{str(dados):<15}", end="")
    print()
# meu CÓDIDO Da FORMATAÇÃO acima:
# print(f"{'COD':<5} {'NOME':<20} {'GOLS':<25} {'TOTAL':>5}")
# print("-" * 70)
# for posicao, valor in enumerate(lista_aproveitamento_jogadores):
#     print(
#         f"{posicao+1:<5} {valor['nome']:<20} {str(valor['gols']):<25} {valor['total']:>5}"
#     )
while True:
    resposta = int(
        input("Mostrar os dados de qual jogador? [999 para finalizar o programa] ")
    )
    if resposta == 999:
        print("Progama finalizado.")
        break
    if resposta == 0 or resposta > len(lista_aproveitamento_jogadores):
        print(
            f"Não existe jogador com o código {resposta}. Verifique o código do jogador."
        )
    else:
        jogador = lista_aproveitamento_jogadores[resposta - 1]
        print(f" -- LEVANTAMENTO DO JOGADOR {jogador['nome']}: ")
        for partida, gol in enumerate(jogador["gols"]):
            print(f"No jogo {partida+1} fez {gol}")

        # # CODIGO DO PROFESOR NO ELSE:
        # print(
        #     f" -- LEVANTAMENTO DO JOGADO {lista_aproveitamento_jogadores[resposta - 1]['nome']}"
        # )
        # for partida, gol in enumerate(
        #     lista_aproveitamento_jogadores[resposta - 1]["gols"]
        # ):
        #     print(f"        No jogo {partida + 1} fez {gol} gols.")
    print("-" * 40)
print("<< VOLTE SEMPRE >>")
