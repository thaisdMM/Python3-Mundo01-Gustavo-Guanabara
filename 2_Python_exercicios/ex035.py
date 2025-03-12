#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# "Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo."


reta1 = int(input("Digite o número inteiro de cumprimento da reta 1: "))
reta2 = int(input("Digite o número inteiro de cumprimento da reta 2: "))
reta3 = int(input("Digite o número inteira de cumprimento da reta 3: "))
# print(reta1, reta2, reta3) # teste

# if reta2 + reta3 > reta1:
#    print(f"A reta 1 {reta1}cm pode formar uma das retas do triângulo.")
#    if reta1 +reta3 > reta2:
#       print(f"A reta 2 {reta2}cm também pode formar uma das retas do triângulo.")
#       if reta1 + reta2 > reta3:
#          print(f"TEMOS UM TRIÂNGULO!!! A reta 3 {reta3}cm também pode formar uma das retas de um triângulo.")
# else:
#    print("Não é possível formar o triângulo!") # o problema é que só entra aqui se a condição 1 nao for verdadeira, no resto nao entra

if reta2 + reta3 > reta1 and reta1 + reta3 > reta2 and reta2 + reta1 > reta3:
   print(f"\nTEMOS UM TRIÂNGULO! As medidas são {reta1}cm, {reta2}cm, {reta3}cm")
else:
   print(f"\nNão é possível formar um triângulo com as medidas {reta1}cm, {reta2}cm, {reta3}cm")