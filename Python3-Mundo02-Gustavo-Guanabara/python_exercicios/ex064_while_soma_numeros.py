# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

numero_eh_999 = False
contador = soma = 0

while numero_eh_999 == False:
    numero = int(input("Digite um número ou 999 para parar o programa: "))
    if numero == 999:
        numero_eh_999 = True
        print(f"Digitou o número {numero} para sair do programa.")
    else:
        soma += numero
        contador += 1

print(f"Você digitou {contador} números e a soma entre eles é {soma}")

# Correção do professor:

numero = contador = soma = 0
numero = int(input("Digite um número [999 para parar]: "))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {contador} números e a soma entre eles foi {soma}")
