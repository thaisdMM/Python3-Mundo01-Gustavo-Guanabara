# Faça um programa que leia três números a mostra qual é o maior e qual é o menor.
# eu pus >= e <= para ter sempre uma resposta pq se for igual nao print

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print("\nMaior de 3 números:")
if n1 >= n2 and n1 >= n3:
   print(f"O número {n1} é maior ou igual a {n2} e {n3}")
elif n2 >= n1 and n2 >= n3:
   print(f"O número {n2} é maior ou igual a {n1} e {n3}")
else:
   print(f"O número {n3} é maior ou igual a {n1} e n{n2}")

print("\nMenor de 3 números:")
if n1 <= n2 and n1 <= n3:
   print(f"O número {n1} é menor ou igual a {n1} e {n3}")
elif n2 <= n1 and n2 <= n3:
   print(f"O número {n2} é menor ou igual a {n1} e {n3}")
else:
   print(f"O número {n3} é menor ou igual a {n1} e {n2}")