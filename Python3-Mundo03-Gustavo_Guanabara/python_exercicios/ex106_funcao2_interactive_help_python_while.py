# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
import builtins

cores = {
    "limpa": "\033[m",
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "pretoebranco": "\033[7;37m",
    "textovermelhofundoamarelo": "\033[31;43m",
    "sublinhadovermelhofundoazul": "\033[4;31;44m",
    "letraazulfundoamarelo": "\033[1;7;33;44m",
    "fundoamareloateofinal": "\033[1;31;43m",
}


def escreva(txt):

    tamaho_linha = len(txt) + 4
    print(f"{cores['fundoamareloateofinal']}~" * tamaho_linha)
    print(f"  {txt}")
    print(tamaho_linha * f"{cores['fundoamareloateofinal']}~{cores['limpa']}")


def biblioteca():
    while True:
        escreva("SISTEMA DE AJUDA PyHELP")
        resposta = input("Função ou Biblioteca > ").strip().lower()
        if resposta == "fim":
            print("Programa finalizado!")
            break
        else:
            print(
                f"{cores['sublinhadovermelhofundoazul']}Acessando o manual do comando: {resposta}{cores['limpa']}"
            )
            funcao = getattr(builtins, resposta)
            print(f"{cores['pretoebranco']}{funcao.__doc__}{cores['limpa']}")


biblioteca()
