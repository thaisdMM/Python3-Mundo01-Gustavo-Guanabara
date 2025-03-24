# Melhora o DESAFIO 061, parguntando para o usuário so ale quar mostrar mois alguns termos. O programa encerra quando ala dissar que quar mostrar O tormos.

primeiro_termo_pa = int(input("1° termo da Progressão Aritmética: "))
razao_pa = int(input("Razão da Progressão Aritmética: "))
termos_pa = primeiro_termo_pa
# numero_termos_pa = int(input("Número de termos da Progressão Aritmética: "))
numero_termos_pa = 0
primeira_sequencia_termos = 10
sequencia_pa = ""
novos_termos_pa = 0
continuar_programa = True


# while continuar_programa == True:
#     if termos_pa <= 10:
while continuar_programa:
    print(termos_pa, end=", ")
    sequencia_pa += f"{termos_pa}, "
    termos_pa += razao_pa

    # print(sequencia_pa)
    # numero_termos_pa += 1
    primeira_sequencia_termos -= 1
    if primeira_sequencia_termos == 0:
        novos_termos_pa = int(
            input("\nQuantos termos da Progressão Aritmética você quer mostrar? ")
        )

        if novos_termos_pa == 0:
            continuar_programa = False
            print(
                f"\nVocê digitou {novos_termos_pa} e nao deseja mais adicionar números à Progressão Aritmética."
            )

        else:
            primeira_sequencia_termos = novos_termos_pa
print(f"\nA SEQUENCIA FINAL DA PA foi: {sequencia_pa[:-2]}")
print("\nPrograma finalizado.")
