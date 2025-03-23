# Melhora o DESAFIO 061, parguntando para o usuário so ale quar mostrar mois alguns termos. O programa encerra quando ala dissar que quar mostrar O tormos.

primeiro_termo_pa = int(input("1° termo da Progressão Aritmética: "))
razao_pa = int(input("Razão da Progressão Aritmética: "))
termos_pa = primeiro_termo_pa
# numero_termos_pa = int(input("Número de termos da Progressão Aritmética: "))
numero_termos_pa = 0
sequencia_pa = " "
#novos_termos_pa = -1
continuar_programa = True

# while continuar_programa == True:
#     if termos_pa <= 10:
while continuar_programa == True:
    novos_termos_pa = int(input("Quantos termos da Progressão Aritmética você quer mostrar? "))
    if novos_termos_pa == 0:
        continuar_programa = False
        print(termos_pa, end=", ")
        termos_pa += razao_pa
        numero_termos_pa += 1
        numero_termos_pa == novos_termos_pa
    else:
        print(novos_termos_pa)
        #print(termos_pa)
    # elif termos_pa <= 10:
    #     print(termos_pa, end=", ")
    #     termos_pa += razao_pa
    #     numero_termos_pa += 1
    # elif termos_pa == 10:
    #     novos_termos_pa = print(int(input("Quantos termos da PA ainda quer mostrar? ")))

# elif novos_termos_pa == 0:
#     continuar_programa = False
print("\nPrograma finalizado.")
