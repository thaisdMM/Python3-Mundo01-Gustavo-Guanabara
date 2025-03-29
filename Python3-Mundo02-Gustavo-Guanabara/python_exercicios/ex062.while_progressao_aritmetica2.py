# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo_pa = int(input("1° termo da Progressão Aritmética: "))
razao_pa = int(input("Razão da Progressão Aritmética: "))
termos_pa = primeiro_termo_pa
# numero_termos_pa = int(input("Número de termos da Progressão Aritmética: "))
numero_termos_pa = 0
primeira_sequencia_termos = 10
sequencia_pa = ""
novos_termos_pa = 0
continuar_programa = True
contador_termos_mostrados = 0


# while continuar_programa == True:
#     if termos_pa <= 10:
while continuar_programa:
    print(termos_pa, end=", ")
    sequencia_pa += f"{termos_pa}, "
    termos_pa += razao_pa
    contador_termos_mostrados += 1

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
print(f"\nForam exibidos {contador_termos_mostrados} termos da PA.")
print(f"\nA SEQUENCIA FINAL DA PA foi: {sequencia_pa[:-2]}")
print("\nPrograma finalizado.")
