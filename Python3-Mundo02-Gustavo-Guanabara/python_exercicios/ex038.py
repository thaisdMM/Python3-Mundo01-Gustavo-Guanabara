# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

print("\nCOMPARAÇÃO ENTRE DOIS NÚMEROS INTEIROS:")
numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("Digite o segundo números: "))
# print(numero1, numero2)
if numero1 > numero2:
    print(
        f"O primeiro número: {numero1} é maior que o segundo número: {numero2}")
elif numero2 > numero1:
    print(
        f"O segundo número: {numero2} é maior que o primeiro número: {numero1}")
else:
    print(f"Os dois números são iguais: {numero1} = {numero2}")
