print("PROGRESSÃO ARITMÉTICA")

primeiro_termo_pa = int(input("\nDigite o primeiro termo da PA: "))
razao_pa = int(input("Digite a razão da PA: "))
termos_pa = primeiro_termo_pa
numero_termos = 0

print(
    f"\nOs 10 primeiros termos da Progressão Aritmética que começa com: {termos_pa} e a razão é: {razao_pa} são: \n"
)
while numero_termos < 10:
    print(f"{termos_pa} → ", end="")
    termos_pa += razao_pa
    numero_termos += 1
    # print(numero_termos, end="")
print("FIM.")

# A RESOLUÇÃO ABAIXO NÃO ERA NECESSÁRIA, MAS FUNCIONA.
# Resolução com a fórmula do 10° termo da pa

print("\nPROGRESSÃO ARITMÉTICA")

primeiro_termo_pa = int(input("\nDigite o primeiro termo da PA: "))
razao_pa = int(input("Digite a razão da PA: "))
termos_pa = primeiro_termo_pa
numero_termos = 0
decimo_termo_pa = primeiro_termo_pa + (10 - 1) * razao_pa

print(
    f"\nOs 10 primeiros termos da Progressão Aritmética que começa com: {termos_pa} e a razão é: {razao_pa} são: \n"
)
while termos_pa <= decimo_termo_pa:
    print(f"{termos_pa} → ", end="")
    termos_pa += razao_pa
    numero_termos += 1
    # print(numero_termos, end="")
print("FIM.")
