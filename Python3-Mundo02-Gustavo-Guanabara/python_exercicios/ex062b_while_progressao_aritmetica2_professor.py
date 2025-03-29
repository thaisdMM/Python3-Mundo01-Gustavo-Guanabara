print("Gerador de PA")
print("-=" * 10)
primeiro_termo = int(input("Primeiro termo: "))
razao_pa = int(input("Razão da PA: "))
termo_pa = primeiro_termo
contador_pa = 1
total_termos_pa = 0
mais = 10 # como o programa começa com 10 ele tá simulando que primeiro foi digitado 10 em mais
while mais != 0:
    while contador_pa <= total_termos_pa:
        print(f"{termo_pa} → ", end="")
        termo_pa += razao_pa
        contador_pa += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print("FIM")