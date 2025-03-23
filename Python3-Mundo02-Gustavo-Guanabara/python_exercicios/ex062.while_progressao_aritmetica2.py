# Melhora o DESAFIO 061, parguntando para o usuário so ale quar mostrar mois alguns termos. O programa encerra quando ala dissar que quar mostrar O tormos.

primeiro_termo_pa = int(input("1° termo da Progressão Aritmética: "))
razao_pa = int(input("Razão da Progressão Aritmética: "))
termos_pa = primeiro_termo_pa
# numero_termos_pa = int(input("Número de termos da Progressão Aritmética: "))
numero_termos_pa = 0
sequencia_pa = " "
novos_termos_pa = -1
continuar_programa = True

# while continuar_programa == True:
#     if termos_pa <= 10:
while continuar_programa == True:
    if novos_termos_pa == 0:
        continuar_programa = False
    elif termos_pa <= 10:
        print(termos_pa, end=", ")
        termos_pa += razao_pa
        numero_termos_pa += 1
    elif termos_pa == 10:
        novos_termos_pa = print(int(input("Quantos termos da PA ainda quer mostrar? ")))

# elif novos_termos_pa == 0:
#     continuar_programa = False
print("\nPrograma finalizado.")
