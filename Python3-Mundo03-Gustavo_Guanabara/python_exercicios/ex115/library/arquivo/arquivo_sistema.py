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
        for linha in conteudo:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n", "")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")


def cadastrar_arquivo(file_path, nome="desconhecido", idade=0):
    try:
        with open(file_path, "at") as arquivo:
            try:
                arquivo.write(f"{nome};{idade}\n")
            except:
                print("Houve algum ERRO ao adicionar dados no arquivo.")
            else:
                print(f"Novo resgistro de {nome} adicionado com sucesso!")
    except PermissionError:
        print("Você não tem permissão para editar esse arquivo.")
    except:
        print("Houve ERRO genérico na abertura do arquivo.")
