# CORREÇÃO PROFESSOR

numeros_extenso = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove",
    "vinte",
)
contador_numeros_extenso = 0
while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {numeros_extenso[numero]}")
        contador_numeros_extenso += 1
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        #continuar = " "
        while continuar not in "SN":
            print("Comando inválido. Tente novamente.")
            continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        
        if continuar == "N":
            break
        if continuar == "S":
            print("Voce escolheu continuar.")
    else:
        print("Tente novamente. ", end="")
print(f"Você exibiu {contador_numeros_extenso} números por extenso.")
print("Programa finalizado.")
