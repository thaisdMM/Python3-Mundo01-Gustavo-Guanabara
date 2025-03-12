# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero_random = randint(0,5)
#print(numero_random) # pus o print para testar se funcionava corretamente
print("Tente advinhar o número. Você pode escolher do número 0 a 5.")
numero_usuario = int(input("Digite um numero: "))
if numero_usuario == numero_random:
   print(f"Você ACERTOU!")
else:
   print(f"Você ERROU! O numero era: {numero_random}")