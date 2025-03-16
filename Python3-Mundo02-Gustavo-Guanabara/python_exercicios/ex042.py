# Rafaça o DESAFIO035 dos triângulos. acroscantando o recurso de mostrar que tipo de triângulo sará formado:
# - Equilátero: todos os lados iguais
# - Isóscolas: dois lados iguais
# - Escalano: todos os lados difarantas

print("\nVERIFICANDO SE 3 SEGMENTOS FORMAM UM TRIÂGULO")

segmento1 = float(input("\nPrimeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))
#print(segmento1, segmento2, segmento3)

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3  and segmento3 < segmento1 + segmento2:
   print("\PODE formar triâgulo.")
   if segmento1 == segmento2 and segmento2 == segmento3:
      print(f"TRIÂNGULO EQUILÁTERO! Os três segmentos são todos iguais: {segmento1}, {segmento2} e {segmento3}.")
   elif segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3:
      print(f"TRIÂNGULO ESCALENO! O três segmentos são diferentes: {segmento1}, {segmento2} e {segmento3}")
   else:
      print(f"TRIÂGULO ISÓSCELES! Dois dos segmentos são iguais: {segmento1}, {segmento2} e {segmento3}")
else:
   print("\nNÃO pode formar triângulo.")