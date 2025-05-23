# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(msg):
    while True:
        print(msg, end="")
        entrada_usuario = input().strip()
        if entrada_usuario.isnumeric():
            break
        if entrada_usuario[0] == "-" and entrada_usuario[1:].isnumeric():
            break
        print("ERRO! Digite um número inteiro válido.")
    entrada_usuario = int(entrada_usuario)
    return entrada_usuario


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")
