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
