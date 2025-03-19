#Faça um programa que laig o paso de cinco passoas. No final, mostra qual foi o maior a o menor paso lidos.

maior_peso = 0
menor_peso = 0

for i in range (0,4):
   peso = float(input("Digite o seu peso: "))
   if i == 0:
      maior_peso = peso
      menor_peso = peso
   if peso > maior_peso:
      maior_peso = peso
   if peso < menor_peso:
      menor_peso = peso
   else:
      maior_peso = maior_peso
      menor_peso = menor_peso
print(maior_peso)
print(menor_peso)