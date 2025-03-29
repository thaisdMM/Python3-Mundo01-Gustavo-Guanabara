print("Gerador de PA")
print("-=" * 10)
primeiro_termo = int(input("Primeiro termo: "))
razao_pa = int(input("Razão da PA: "))
termo_pa = primeiro_termo
contador_pa = 1

while contador_pa <= 10:
    print(f"{termo_pa} → ", end="")
    termo_pa += razao_pa
    contador_pa += 1
print("PAUSA")
mais = int(input("Quantos termos você quer mostrar a mais? "))