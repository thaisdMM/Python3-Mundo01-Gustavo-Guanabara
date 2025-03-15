#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# "Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo."


# reta1 = float(input("Digite o número floateiro de cumprimento da reta 1: "))
# reta2 = float(input("Digite o número floateiro de cumprimento da reta 2: "))
# reta3 = float(input("Digite o número floateira de cumprimento da reta 3: "))
# # print(reta1, reta2, reta3) # teste

# if reta2 + reta3 > reta1 and reta1 + reta3 > reta2 and reta2 + reta1 > reta3:
#    print(f"\nTEMOS UM TRIÂNGULO! As medidas são {reta1}cm, {reta2}cm, {reta3}cm")
# else:
#    print(f"\nNão é possível formar um triângulo com as medidas {reta1}cm, {reta2}cm, {reta3}cm")

# Correção professor

print("-=" * 20)
print("Analisador de Triângulos")
print("-=" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
#print(f"Os três seguimentos são: {r1} {r2} {r3}") # teste
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print("Os segmentos acima PODEM FORMAR triângulo!")
else:
   print("Os segmentos acima NÃO podem formar triângulo.")