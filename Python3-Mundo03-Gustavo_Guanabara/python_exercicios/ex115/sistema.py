import os
from library.interface import interface_sistema
from library.arquivo import arquivo_sistema
from time import sleep

# Caminho absoluto da pasta onde está o sistema.py
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto até o arquivo .txt
CAMINHO_ARQUIVO = os.path.join(PASTA_BASE, "lista_pessoas_idade_sistema_ex115.txt")


arquivo = CAMINHO_ARQUIVO

if not arquivo_sistema.arquivo_existe(arquivo):
    arquivo_sistema.criar_arquivo(arquivo)


while True:
    resposta = interface_sistema.menu(
        ["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair do Sistema"]
    )
    if resposta == 1:
        # interface_sistema.titulo("LISTA DE PESOAS CADASTRADAS")
        arquivo_sistema.ler_arquivo(arquivo)
    elif resposta == 2:
        interface_sistema.titulo("NOVO CADASTRO")
        nome = input("Nome: ").strip().title()
        idade = interface_sistema.leiaInt("Idade: ")
        arquivo_sistema.cadastrar_arquivo(arquivo, nome, idade)

    elif resposta == 3:
        interface_sistema.titulo("Saindo do Sistema... Até logo!")
        break
    else:
        print(f"\033[31mERRO! Opção '{resposta}' inexistente no menu.\033[m")
    sleep(1)
