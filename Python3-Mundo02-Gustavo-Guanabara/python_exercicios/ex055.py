#Faça um programa que laig o paso de cinco passoas. No final, mostra qual foi o maior a o menor paso lidos.

maior_peso = 0

for i in range(0):
   peso = float(input("Digite o seu peso: "))
   #print(peso)
   maior_peso = peso
for i in range (0,4):
   peso = float(input("Digite o seu peso: "))
   if peso > maior_peso:
      maior_peso = peso
   else:
      maior_peso = maior_peso
print(maior_peso)