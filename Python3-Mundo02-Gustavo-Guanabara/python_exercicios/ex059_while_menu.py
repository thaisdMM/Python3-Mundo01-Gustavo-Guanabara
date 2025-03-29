# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

numero1 = int(input("1° número: "))
numero2 = int(input("2° número: "))
sair_do_programa = False
maior = 0

while sair_do_programa == False:
    print(
        """
    MENU DO PROGRAMA:
          
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
"""
    )
    escolha_usuario = int(input("Digite a sua escolha: "))

    # if escolha_usuario not in (1, 2, 3, 4, 5):
    #     print("Escolha inválida. Tente novamente!")

    if escolha_usuario == 1:
        soma = numero1 + numero2
        print(f"SOMA: {numero1} + {numero2} = {soma}")
    elif escolha_usuario == 2:
        multiplicacao = numero1 * numero2
        print(f"MULTIPLICAÇÃO: {numero1} x {numero2} = {multiplicacao}")
    elif escolha_usuario == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f"MAIOR: entre {numero1} e {numero2} o maior é: {maior}")
    elif escolha_usuario == 4:
        print("Digite os novos números:")
        numero1 = int(input("Novo 1° número: "))
        numero2 = int(input("Novo 2° número: "))

    elif escolha_usuario == 5:
        sair_do_programa = True
        print(f"Escolheu {escolha_usuario}: Sair do programa.")
    # Dava para colocar um else para opção invalida e nao precisava de fazer o primeiro if
    else:
        print("Opção invalida. Tente novamente.")
    print("=-=" * 10)
    sleep(1)

print("Programa finalizado.")
