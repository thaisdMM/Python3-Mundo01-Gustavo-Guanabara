#Dasenvolva um programa que laia o primairo tormo e a razão de uma PA. No Final, mostra os 10 princiros termos dessa progressão.

print("PROGRESSÃO ARITMÉTICA")
termo1_pa = int(input("\nDigite o primeiro termos da progressao aritmética: "))
razao_pa = int(input("Digite a razão da progresão aritmética: "))
for i in range(0,10):
   print(f"{termo1_pa}", end = ", ")
   termo1_pa += razao_pa
print("\nFim do programa.")