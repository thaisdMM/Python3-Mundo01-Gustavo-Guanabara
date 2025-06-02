def leiaDinheiro(msg):
    while True:
        eh_monetario = False
        valor = 0
        numero = input(msg).strip().replace(",",".")
        if not numero:
            print(f"\033[0;31mERRO!'{numero}' Não foi digitado nada ou apenas espaços vazios.\033[m")
            continue
        if numero.isnumeric():
            valor = float(numero)
            eh_monetario = True
        else:
            encontrou_caractere = 0
            #virgula_caractere = ""
            if numero[0].isdigit() == False:
                eh_monetario = False
                print(
                    f"\033[0;31mERRO! Caractere '{numero[0]}' da primeira entrada não é monetária.\033[m"
                )
                continue
            for caractere in numero:
                if caractere.isnumeric():
                    continue
                if caractere not in ".":
                    eh_monetario = False
                    print(
                        f"\033[0;31mERRO! Caractere '{caractere}' diferente dos separadores monetários [.,]\033[m"
                    )
                    break
                else:
                    if caractere in ".":
                        encontrou_caractere += 1
                    # if caractere in ",":
                    #     encontrou_caractere += 1
                    #     virgula_caractere += caractere
                if encontrou_caractere > 1:
                    print(
                        f"\033[0;31mERRO!'{numero}' Mais separadores decimais do que permitido.\033[m"
                    )
                    eh_monetario = False
                    break
            if encontrou_caractere == 1:
                eh_monetario = True
                # if len(virgula_caractere) == 1:
                #     troca_virgula = numero.replace(",", ".")
                #     valor = float(troca_virgula)
                # else:
                valor = float(numero)
        if eh_monetario:
            break
    return valor

# # CORREÇÃO DO PROFESSOR:


# def leiaDinheiro(msg):
#     valido = False
#     while not valido:
#         entrada = input(msg).replace(",", ".").strip()

#         if entrada.isalpha() or entrada == "":
#             print(f"\033[0;31mERRO: \'{entrada}\' é um preço inválido!\033[m")
#         else:
#             valido = True
#             return float(entrada)