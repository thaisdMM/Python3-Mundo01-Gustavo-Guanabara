# Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários


def leiaDinheiro(msg):
    while True:
        eh_monetario = False
        valor = 0
        numero = input(msg)
        if numero.isnumeric():
            valor = int(numero)
            eh_monetario = True
        else:
            encontrou_numero = 0
            encontrou_caractere = 0
            if numero[0].isdigit() == False:
                eh_monetario = False
                print(f"ERRO! Caractere primeira entrada não é numérica")
                continue
            for caractere in numero:
                # if caractere[0]:
                #     if caractere.isnumeric():
                #         encontrou_numero +=1
                #     else:
                #         eh_monetario = False
                #         print(f"ERRO! Caractere primeira entrada não é numérica")
                #         break
                # else:
                if caractere.isnumeric():
                    continue
                if caractere not in ",.":
                    eh_monetario = False
                    print(f"ERRO! Caractere diferente de ., .")
                    break
                else:
                    if caractere in ".":
                        print(caractere)
                        encontrou_caractere += 1
                    if caractere in ',':
                        encontrou_caractere += 1
                if encontrou_caractere > 1:
                    print(f"ERRO! Mais caracteres.")
                    eh_monetario = False
                    break
                if encontrou_caractere == 1:

                    valor = numero
                    eh_monetario = True
            
                

                # if caractere != "," and caractere != ".":
                #     eh_monetario = False
                #     print(f"ERRO! Caractereo diferente.")
                #     break
                # if caractere == ',' or caractere == '.':
                
                #     encontrou_caractere += 1
                # if encontrou_caractere > 1:
                #     print(f"ERRO! Mais caractereos.")
                #     eh_monetario = False
                #     break
                # if encontrou_caractere == 1:

                #     valor = numero
                #     eh_monetario = True
                # else:
                #     not eh_monetario
                #     break


        if eh_monetario:
            break
    return valor


numero = leiaDinheiro("digite um valor monetário: ")
print(f"O valor digitado foi {numero}")
