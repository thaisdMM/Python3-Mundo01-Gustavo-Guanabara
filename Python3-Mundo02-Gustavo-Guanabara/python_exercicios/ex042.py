# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("\nVERIFICANDO SE 3 SEGMENTOS FORMAM UM TRIÂGULO")

segmento1 = float(input("\nPrimeiro segmento: "))
segmento2 = float(input("Segundo segmento: "))
segmento3 = float(input("Terceiro segmento: "))
# print(segmento1, segmento2, segmento3)

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print("\nPODE formar triâgulo.")
#   if segmento1 == segmento2 and segmento2 == segmento3: # meu código, mas python aceita fazer a comparação direta:
    if segmento1 == segmento2 == segmento3:  # 1 == 2 e 2==3, então 1, 2, 3 são iguais
        print(
            f"TRIÂNGULO EQUILÁTERO! Os três segmentos são todos iguais: {segmento1}, {segmento2} e {segmento3}.")
#   elif segmento1 != segmento2 and segmento1 != segmento3 and segmento2 != segmento3:
    # 1!=2 e 2!=3, mas 1 pode ser == 3 entao tem que colar 1!=3, senão pode ler como escaleno um triângulo isósceles
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print(
            f"TRIÂNGULO ESCALENO! O três segmentos são diferentes: {segmento1}, {segmento2} e {segmento3}")
    else:
        print(
            f"TRIÂGULO ISÓSCELES! Dois dos segmentos são iguais: {segmento1}, {segmento2} e {segmento3}")
else:
    print("\nNÃO pode formar triângulo.")
