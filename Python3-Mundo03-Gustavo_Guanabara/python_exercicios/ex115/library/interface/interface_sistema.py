def linha(tamanho = 50):
    print("-" * 50)

def titulo(msg):
    linha()
    print(msg.center(50))
    linha()

def menu(lista):
    titulo("MENU PRINCIPAL")
    contador = 1
    for item in lista:
        print(f"{contador} - {item}")
        contador += 1
    print(linha)