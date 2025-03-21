numero1 = int(input("1° número: "))
numero2 = int(input("2° número: "))
# print(numero1, numero2)
sair_do_programa = False
soma = numero1 + numero2
multiplicacao = numero1 * numero2
maior = 0

while sair_do_programa == False:
    print("""
    MENU DO PROGRAMA:
          
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
""")
    escolha_usuario = int(input("Digite a sua escolha: "))

    if escolha_usuario not in (1,2,3,4,5):
        print("Escolha inválida. Tente novamente!")

    elif escolha_usuario == 1:
        print(f"SOMA: {numero1} + {numero2} = {soma}")
    elif escolha_usuario == 2:
        print(f"MULTIPLICAÇÃO: {numero1} x {numero2} = {multiplicacao}")
    elif escolha_usuario == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f"MAIOR: entre {numero1} e {numero2} o maior é: {maior}")
    elif escolha_usuario == 4:
        numero1 = int(input("Novo 1° número: "))
        numero2 = int(input("Novo 2° número: "))
    
    elif escolha_usuario == 5:
        sair_do_programa = True
        print(f"Escolheu {escolha_usuario}: Sair do programa.")

print("Programa finalizado.")