numero1 = int(input("1° número: "))
numero2 = int(input("2° número: "))
# print(numero1, numero2)
sair_do_programa = False
soma = numero1 + numero2
multiplicacao = numero1 * numero2

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

    if escolha_usuario == 1:
        print(f"Soma: {numero1} + {numero2} = {soma}")

    
    if escolha_usuario == 5:
        sair_do_programa = True
        print(f"Escolheu {escolha_usuario}: Sair do programa.")

print("Programa finalizado.")