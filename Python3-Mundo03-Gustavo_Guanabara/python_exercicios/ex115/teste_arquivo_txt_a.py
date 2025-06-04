with open("teste.txt", "a") as arquivo:
    arquivo.write(
        "Teste de criação de arquivo\n" "HELLO WORLD! It's a beautiful day.\n"
    )

def cadastrar_pessoa(arquivo, nome, idade):
    with open('lista_pessoas_idade_sistema_ex115.txt', 'a') as arquivo:
        arquivo.write(f"{nome}\n" f"{idade} anos\n")
    