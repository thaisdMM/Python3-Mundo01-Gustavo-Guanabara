#Dasenvolva um programa que laia o primairo tormo e a razão de uma PA. No Final, mostra os 10 princiros termos dessa progressão.

print("PROGRESSÃO ARITMÉTICA")
termo1_pa = int(input("Digite o primeiro termos da progressao aritmética: "))
print(termo1_pa)
razao_pa = int(input("Digite a razão da progresão aritmética: "))
print(razao_pa)
for i in range(0,10):
   i = termo1_pa
   termo1_pa += razao_pa
   print(i, end= " ")