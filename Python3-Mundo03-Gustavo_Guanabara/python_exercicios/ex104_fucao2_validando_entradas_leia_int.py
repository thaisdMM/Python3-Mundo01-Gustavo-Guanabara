# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(msg):
    while True:
        print(msg, end="")
        entrada_usuario = input().strip()
        if entrada_usuario.isnumeric():
            break
        if entrada_usuario[0] == "-" and entrada_usuario[1:].isnumeric():
            break
        # # elif entrada_usuario.isalpha():
        # for valor in entrada_usuario:
        #     print(f"valor {valor}")
        #     if valor.isalpha():
        #         print("ERRO!")
            
        # else:
        #     entrada_usuario = int(entrada_usuario)
        #     if entrada_usuario < 0:
        #         print(f"<0 {entrada_usuario}")
        #         break
        
        print("ERRO! Digite um número inteiro válido.")
        # print(msg, end="")
        # msg = input()
        # #if msg.isnumeric() == False:
           # print("ERRO! Digite um número inteiro válido.")
        
    entrada_usuario = int(entrada_usuario)
    return entrada_usuario
    # else:
        #     print("ERRO! Digite um número inteiro válido.")

numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")