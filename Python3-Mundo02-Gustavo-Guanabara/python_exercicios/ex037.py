# Escrava um programa que laia um número intairo qualquar e peça para o usuário escolhar qual sará a base de convarsão:
# - 1 para binário
# - 2 parg octal
# - 3 para hexadecimal

print("\nCONVERSAO DE NUMERO PARA BINÁRIO, OCTAL ou HEXADECIMAL")
numero = int(input("\nDigite um número inteiro: "))
#print(numero)
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
   print(f"\nINTEIRO = {numero}, convertido para HEXADECIMAL = {hex(numero)[2:]}")
else:
   print("\nOpção inválida. Tente novamente.")