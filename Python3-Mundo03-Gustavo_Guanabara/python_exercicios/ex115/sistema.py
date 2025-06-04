from library.interface import interface_sistema
from time import sleep


while True:
    resposta = interface_sistema.menu(["Ver Pessoas Cadastradas", "Cadastrar Nova Pessoa", "Sair do Sistema"])
    if resposta == 1:
        interface_sistema.titulo("LISTA DE PESOAS CADASTRADAS")
    elif resposta == 2:
        interface_sistema.titulo("NOVO CADASTRO")

    elif resposta == 3:
        interface_sistema.titulo("Saindo do Sistema... Até logo!")
        break
    else:
        print(f"\033[31mERRO! Opção '{resposta}' inexistente no menu.\033[m")
    sleep(1)