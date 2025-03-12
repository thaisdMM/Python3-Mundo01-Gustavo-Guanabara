# Faça um programa que leia três números a mostra qual é o maior e qual é o menor.

# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# n3 = int(input("Digite o terceiro número: "))

# print("\nMaior de 3 números:")
# if n1 > n2 and n1 > n3:
#    print(f"O número {n1} é maior que {n2} e {n3}")
# elif n2 > n1 and n2 > n3:
#    print(f"O número {n2} é maior que {n1} e {n3}")
# elif n3 > n1 and n3 > n2:
#    print(f"O número {n3} é maior que {n1} e n{n2}")
# else:
#    print(f"Alguns dos números digitados são iguais: {n1}, {n2}, {n3}")

# print("\nMenor de 3 números:")
# if n1 < n2 and n1 < n3:
#    print(f"O número {n1} é menor que a {n1} e {n3}")
# elif n2 < n1 and n2 < n3:
#    print(f"O número {n2} é menor que a {n1} e {n3}")
# elif n3 < n1 and n3 < n2:
#    print(f"O número {n3} é menor que a {n1} e {n2}")
# else:
#    print(f"Algum dos números são iguais: {n1}, {n2}, {n3}")

# explicação PROFESSOR

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

# para simplificar o código e eliminar linhas de código vai testar considerando um valor como menor ou maior
menor = a 
if b < a and b < c:
   menor = b
if c < a and c < b:
   menor = c
print(f"Os números são: {a}, {b}, {c}.\nO menor entre eles é: {menor}")

maior = a
if b > a and b > c:
   menor = b
if c > a and c > b:
   maior = c
print(f"\nOs números são: {a}, {b}, {c}.\nO maior entre eles é: {maior}")
