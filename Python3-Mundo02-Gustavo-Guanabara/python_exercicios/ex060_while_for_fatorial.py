numero = int(input("Digite um número pra saber o fatorial: "))
fatorial = 1
sequencia_fatorial = " "
contador_fatorial = 0

# for i in range(numero, 0, -1):
#     #print(i)
#     fatorial = fatorial * i
#     if i == 1:
#         sequencia_fatorial += f"{i} "
#     else:
#         sequencia_fatorial += f"{i} x "
# #    acumulador += fatorial * fatorial
# #    print(fatorial)
# #    print(sequencia_fatorial)
# #    print (acumulador)

# print(f"FATORIAL de {numero}: {sequencia_fatorial} = {fatorial}")

while numero > 0:
    print(numero)
    fatorial = fatorial * numero
    sequencia_fatorial += f"{numero}"
    numero -= 1
    if numero == 0:
        sequencia_fatorial += f" "
    else:
        sequencia_fatorial += f" x "

    print(fatorial)

#    numero * numero -1

print(f"Fatorial de {numero}: {sequencia_fatorial} = {fatorial}")



# while numero > 0:
# #    print(numero)
#     fatorial = fatorial * numero
# #    sequencia_fatorial += f"{numero}"
#     contador_fatorial = numero -1
#     # if contador_fatorial == 1:
#     #     sequencia_fatorial += f"{numero}"
#     # else:
#     #     sequencia_fatorial += f" {numero} x "

#     #print(fatorial)

# #    numero * numero -1
#     print(fatorial)
#     print(contador_fatorial)
# print(f"Fatorial de {numero}: {sequencia_fatorial} = {fatorial}")