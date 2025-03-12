#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = int(input("Digite o número inteiro de cumprimento da reta 1: "))
reta2 = int(input("Digite o número inteiro de cumprimento da reta 2: "))
reta3 = int(input("Digite o número inteira de cumprimento da reta 3: "))
# print(reta1, reta2, reta3) # teste

if reta2 + reta3 > reta1:
   print(f"A reta 1 {reta1} pode formar uma das retas do triângulo.")
   if reta1 +reta3 > reta2:
      print(f"A reta 2 {reta2} também pode formar uma das retas do triângulo.")
      if reta1 + reta2 > reta3:
         print(f"TEMOS UM TRIÂNGULO!!! A reta 3 {reta3} também pode formar uma das retas de um triângulo.")
      else:
         print("Não é possível formar o triângulo!")