# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

numero_final_fibonacci = int(input("1° número: "))
primeiro_numero_fibonacci = 0
segundo_numero_fibonacci = 1
fibonacci = 0
sequencia_fibonacci = 0
soma = 0

elementos_sequencia = 0
while numero_final_fibonacci > 0:
    #fibonacci =  primeiro_numero_fibonacci, segundo_numero_fibonacci
    sequencia_fibonacci = primeiro_numero_fibonacci, segundo_numero_fibonacci
    primeiro_numero_fibonacci = segundo_numero_fibonacci
    segundo_numero_fibonacci = primeiro_numero_fibonacci + segundo_numero_fibonacci
    #soma = segundo_numero_fibonacci
    print(f"SEQUENCIA: {sequencia_fibonacci}")
    #print(soma)
    print(f"1: {primeiro_numero_fibonacci}", end=" ")
    print(segundo_numero_fibonacci, end=" ")
    numero_final_fibonacci -= 1

# print(sequencia_fibonacci)
