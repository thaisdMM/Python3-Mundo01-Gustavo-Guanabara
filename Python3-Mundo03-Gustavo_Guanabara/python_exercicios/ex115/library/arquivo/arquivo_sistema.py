from library.interface import interface_sistema


def arquivo_existe(nome):
    try:
        file = open(nome, "rt")
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        with open(nome, "wt+") as arquivo:
            pass
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f"Arquivo {nome} criado com sucesso!")


def ler_arquivo(nome):
    try:
        with open(nome, "rt") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print("O arquivo não foi encontrado. Verifique se o arquivo existe.")
    except PermissionError:
        print("Você não tem permissão para ler esse arquivo.")
    else:
        interface_sistema.titulo("LISTA DE PESOAS CADASTRADAS")
        print(conteudo)
