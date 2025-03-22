print("FATORIAL DE UM NÚMERO COM O FOR:")
numero = int(input("\nDigite um número pra saber o fatorial: "))
fatorial = 1
sequencia_fatorial = " "

for i in range(numero, 0, -1):
    # print(i)
    fatorial = fatorial * i
    if i == 1:
        sequencia_fatorial += f"{i} "
    else:
        sequencia_fatorial += f"{i} x "
#    print(fatorial)
#    print(sequencia_fatorial)

print(f"FATORIAL de {numero}: {sequencia_fatorial} = {fatorial}")

print("\nFATORIAL DE UM NÚMERO COM WHILE:")
numero = int(input("\nDigite um número pra saber o fatorial: "))
fatorial = 1
sequencia_fatorial = " "
numero_fatorial = numero

while numero > 0:
    # print(numero)
    fatorial = fatorial * numero
    sequencia_fatorial += f"{numero}"
    numero -= 1
    if numero == 0:
        sequencia_fatorial += f" "
    else:
        sequencia_fatorial += f" x "
    # print(fatorial)

print(f"Fatorial de {numero_fatorial}: {sequencia_fatorial} = {fatorial}")
