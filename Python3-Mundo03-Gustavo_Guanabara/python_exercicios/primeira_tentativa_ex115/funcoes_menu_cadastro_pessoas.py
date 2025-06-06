import function_leia_int_leia_float


def linha():
    print("-" * 50)




def menu():

    titulo("MENU PRINCIPAL")
    print(
        """
        1 - Ver pessoas Cadastradas
        2 - Cadastrar nova pessoa
        3 - Sair do sistema
        """
    )


def cadastrar_pessoa(nome, idade):
    file_path = "lista_pessoas_idade_sistema_ex115.txt"
    with open(file_path, "a") as arquivo:
        arquivo.write(f"{nome};{idade} anos\n")


def ver_pessoas_cadastradas():
    file_path = "lista_pessoas_idade_sistema_ex115.txt"
    try:
        with open(file_path, "r") as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        print("O arquivo não foi encontrado. Verifique se o arquivo existe.")
    except PermissionError:
        print("Você não tem permissão para ler esse arquivo.")
    else:
        junta_conteudo = conteudo.strip()
        separa_conteudo = junta_conteudo.split(";")
        
        # for contador, valor in range(1, len(separa_conteudo) +1):
        #     if contador % 2 != 0:
        #         print(f"{valor.ljust(30)}", end=" ")
        #     if contador % 2 == 0:
        #         print(f"{valor.rjust(10)}\n")
            
        # print(f"{separa_conteudo}", end=" ")
        # print()
        # # for line in conteudo:

        # for line in conteudo:
        #     print(line, end="")
        # print(conteudo)
        # for line in conteudo:
        #     line.strip()
        #     line.split(';')
        #     print(f'{line}', end="")

    # for pessoa in lista:
    #     print(f"\t{pessoa}", end="")
    # print()


lista_pessoas = []
arquivo = "lista_pessoas_idade_sistema_ex115.txt"

while True:
    menu()
    while True:
        opcao = function_leia_int_leia_float.leiaInt("Sua opção: ")
        if 0 < opcao <= 3:
            break
        print(f"ERRO! Opção {opcao} inexistente no menu.")

    if opcao == 1:
        titulo("LISTA DE PESOAS CADASTRADAS")
        ver_pessoas_cadastradas()

    if opcao == 2:
        titulo("NOVO CADASTRO")
        nome = input("Nome: ").strip().title()
        idade = input("Idade: ").strip()
        cadastrar_pessoa(nome, idade)

    if opcao == 3:
        print("Programa finalizado!")
        break


print(lista_pessoas)
