import function_leia_int_leia_float


def linha():
    print("-" * 50)


def titulo(msg):
    linha()
    print(msg.center(50))
    linha()


def menu():

    titulo("MENU PRINCIPAL")
    print(
        """
        1 - Ver pessoas Cadastradas
        2 - Cadastrar nova pessoa
        3 - Sair do sistema
        """
    )


def cadastrar_pessoa(lista, nome, idade):
    lista.append([nome, idade])


def ver_pessoas_cadastradas(lista):
    for pessoa in lista:
        print(f"\t{pessoa}", end="")
    print()


lista_pessoas = []


while True:
    menu()
    while True:
        opcao = function_leia_int_leia_float.leiaInt("Sua opção: ")
        if 0 < opcao <= 3:
            break
        print(f"ERRO! Opção {opcao} inexistente no menu.")

    if opcao == 1:
        titulo("LISTA DE PESOAS CADASTRADAS")
        ver_pessoas_cadastradas(lista_pessoas)

    if opcao == 2:
        titulo("NOVO CADASTRO")
        nome = input("Nome: ")
        idade = input("Idade: ")
        cadastrar_pessoa(lista_pessoas, nome, idade)

    if opcao == 3:
        print("Programa finalizado!")
        break


print(lista_pessoas)
