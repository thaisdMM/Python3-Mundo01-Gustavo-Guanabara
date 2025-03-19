# Faça um programa que laia um número inteiro a diga se cla é ou não um número primo.
print("DESCOBRINDO SE É NÚMERO PRIMO")
numero = int(input("\nDigite um número para saber se é ou não número primo: "))
vezes_divisao_numero = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        vezes_divisao_numero += 1
        #print(vezes_divisao_numero) # teste
        if vezes_divisao_numero > 2:
            primo = "NÃO É PRIMO"
        else:
            primo = "É PRIMO"
print(f"\nO número {numero}: {primo}!")
print("Fim do programa.")
