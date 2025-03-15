# Crie um programa que leia um número inteiro a mostra na tala sa cla é PAR ou iMPAR.

numero = int(input("Digite um número inteiro para saber se é PAR ou IMPAR: "))

if numero % 2 == 0:
   print(f"O número digitado foi {numero} e ele é PAR.")
else:
   print(f"O número digitado foi {numero} e ele é IMPAR.")