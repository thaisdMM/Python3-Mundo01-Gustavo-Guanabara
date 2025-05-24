# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
import builtins
from time import sleep

cores = {
    "limpa": "\033[m",
    "verde": "\033[0;32m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "pretoebranco": "\033[7;37m",
    "textovermelhofundoamarelo": "\033[31;43m",
    "sublinhadovermelhofundoazul": "\033[4;31;44m",
    "letraazulfundoamarelo": "\033[1;7;33;44m",
    "fundoamareloateofinal": "\033[1;31;43m",
}


def titulo(txt, cor=cores["fundoamareloateofinal"]):

    tamanho = len(txt) + 4
    print(cor, end="")
    print("~" * tamanho)
    print(f"  {txt}")
    print("~" * tamanho)
    print(cores["limpa"], end="")
    sleep(1)


def biblioteca(comando):
    titulo(
        f"Acessando o doc do comando: '{comando}'", cores["sublinhadovermelhofundoazul"]
    )
    print(cores["pretoebranco"], end="")
    funcao = getattr(builtins, comando)
    print(f"{funcao.__doc__}")
    print(cores["limpa"], end="")
    sleep(1)


while True:
    titulo("SISTEMA DE AJUDA Py.__DOC__")
    resposta = input("Função > ").strip().lower()
    if resposta == "fim":
        break
    else:
        biblioteca(resposta)
titulo(f"Programa finalizado!", cores["verde"])
