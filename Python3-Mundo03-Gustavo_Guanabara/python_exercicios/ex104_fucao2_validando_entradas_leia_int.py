# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


def leiaInt(msg):
    print("-" * 30)
    while True:
        print(msg, end="")
        entrada_usuario = input().strip()
        if entrada_usuario.isnumeric():
            break
        if len(entrada_usuario) > 0: # tem pelo menos 2 caracteres, pois o len é >0
            if entrada_usuario[0] == "-" and entrada_usuario[1:].isnumeric():
                break
        print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
    entrada_usuario = int(entrada_usuario)
    return entrada_usuario


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")

# CORREÇÃO DO PROFESSOR:


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        numero = input(msg)
        if numero.isnumeric():
            valor = int(numero)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido\033[m")
        if ok:
            break
    return valor


numero = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {numero}")
