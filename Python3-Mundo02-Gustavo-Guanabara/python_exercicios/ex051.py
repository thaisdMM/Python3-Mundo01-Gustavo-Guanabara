# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

# MEU CÓDIGO:

print("PROGRESSÃO ARITMÉTICA")
termo1_pa = int(input("\nDigite o PRIMEIRO TERMO da progressao aritmética: "))
razao_pa = int(input("Digite a RAZÃO da progresão aritmética: "))
print(
    f"\nOs 10 primeiros termos da PROGRESSÃO ARITMÉTICA que começa com {termo1_pa} e tem razão: {razao_pa} são:")
for i in range(0, 10):
    print(f"{termo1_pa}", end=", ")
    termo1_pa += razao_pa
print("\nFim do programa.")

# CÓDIGO PROFESSOR:

termo1_pa = int(input("\nPrimeiro termo: "))
razao_pa = int(input("Razão: "))
decimo_termo_pa = termo1_pa + (10 - 1) * razao_pa

for i in range(termo1_pa, decimo_termo_pa + razao_pa, razao_pa):
    print(f"{i}", end=" → ")
print("ACABOU.")
