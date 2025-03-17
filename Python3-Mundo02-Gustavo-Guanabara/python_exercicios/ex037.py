# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print("\nCONVERSAO DE NUMERO PARA BINÁRIO, OCTAL ou HEXADECIMAL")
numero = int(input("\nDigite um número inteiro: "))
# print(numero)
print("""Escolha a forma de conversão:
[ 1 ] binário
[ 2 ] octal
[ 3 ] hexadecimal""")
escolha = int(input("Digite sua opção: "))
if escolha == 1:
    print(f"\nINTEIRO = {numero}, convertido para BINÁRIO = {bin(numero)[2:]}")
elif escolha == 2:
    print(f"\nINTEIRO = {numero}, convertido para OCTAL = {oct(numero)[2:]}")

elif escolha == 3:
    print(
        f"\nINTEIRO = {numero}, convertido para HEXADECIMAL = {hex(numero)[2:]}")
else:
    print("\nOpção inválida. Tente novamente.")
