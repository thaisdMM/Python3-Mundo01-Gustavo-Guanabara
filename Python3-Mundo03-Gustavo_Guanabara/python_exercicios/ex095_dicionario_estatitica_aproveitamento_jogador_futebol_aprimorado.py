aproveitamento_jogador = {}
lista_aproveitamento_jogadores = []

while True:
    total_gols = 0
    lista_gols = []
    aproveitamento_jogador["nome"] = input("Nome do jogador: ").strip().title()
    partidas_jogadas = int(
        input(f"Quantas partidas {aproveitamento_jogador['nome']} jogou? ")
    )
    for jogos in range(1, partidas_jogadas + 1):
         gols = int(
            input(
                f"Quantos gols {aproveitamento_jogador['nome']} marcou na partida {jogos}? "
            )
        )
         lista_gols.append(gols)
         total_gols += gols

    aproveitamento_jogador["gols"] = lista_gols
    aproveitamento_jogador["total"] = total_gols
    lista_aproveitamento_jogadores.append(aproveitamento_jogador.copy())
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if continuar == "N":
        print("=-" * 30)
        break
    print("-" * 50)
print(f"lista: {lista_aproveitamento_jogadores}")
print(f"{'COD':<5} {'NOME':<20} {'GOLS':<25} {'TOTAL':>5}")
print("-" * 70)
for posicao, valor in enumerate(lista_aproveitamento_jogadores):
    print(f"{posicao+1:<5} {valor['nome']:<20} {str(valor['gols']):<25} {valor['total']:>5}")
while True:
    resposta = int(input("Mostrar os dados de qual jogador? [999 para finalizar o programa] "))
    if resposta == 999:
        print("Progama finalizado.")
        break
    else:
        for posicao, valor in enumerate(lista_aproveitamento_jogadores):
            if resposta -1 == posicao:
            #if resposta <= len(lista_aproveitamento_jogadores) -1:
                print(f"-- LEVANTAMENTO DO JOGADOR {valor['nome']}: ")
                for gol in valor["gols"]:
                    print(f"No jogo {posicao+1} fez {gol}") 
                # for jogo, gol in enumerate(lista_gols):
                #     print(f"No jogo {jogo +1} fez {gol} gols.")