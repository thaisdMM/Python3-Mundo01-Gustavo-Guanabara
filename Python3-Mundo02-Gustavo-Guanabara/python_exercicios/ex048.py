# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

# MEU CÓDIGO
# print("NÚMEROS IMPARES MULTIPLOS DE 3 DE 1 A 500: \n")

# soma = 0
# for i in range(1,501):
#    if i % 2 == 1 and i % 3 == 0:
#       print(i)
#       soma += i
# print(f"\nA soma dos números ímpares multiplos de 3 de 1 a 500 é = {soma}")

# CÓDIGO PROFESSOR tem acumulador e contador
soma = 0
contador_numeros = 0
# fazendo com o pulo de 2 em 2 e começando com 1 já seleciona só ímpar
for i in range(1, 501, 2):
    if i % 3 == 0:
        contador_numeros += 1
        soma += i
#      print(i, end=" ")
print(f"Temos {contador_numeros} números ímpares multiplos de 3 do 1 a 500.\nA soma de todos os valores é {soma}")
