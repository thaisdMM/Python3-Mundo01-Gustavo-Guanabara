# # Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

numeros_mega_sena = []
lista_mega_sena = []

print("-" * 40)
print(f'{" JOGOS NA MEGA SENA ":^40}')
print("-" * 40)
jogos_gerados = int(input("Quantos jogos quer que eu sorteie? "))
total_jogos = 1 # começou com 1 para não dar um jogo a mais
while total_jogos <= jogos_gerados:
    contador = 0
    while True:
        palpite_mega_sena = randint(1,60)
        if palpite_mega_sena not in numeros_mega_sena:
            numeros_mega_sena.append(palpite_mega_sena)
            contador += 1
        if contador >= 6:
            break
    numeros_mega_sena.sort()
    lista_mega_sena.append(numeros_mega_sena[:])
    numeros_mega_sena.clear()
    total_jogos += 1   
#print(f"Os números sorteados foram: {lista_mega_sena}")

sleep(1)
print(f"=-" * 20)
print(f" {'SORTEANDO':>15} {jogos_gerados} {'JOGOS'} ")
print("=-" * 20)
for posicao, valor in enumerate(lista_mega_sena):
    sleep(1)
    print(f"Jogo {posicao+1}: {valor} ")

print(f"\n{' BOA SORTE!!! ':=^30}")

# Meu código Estava com um erro no FOR pois podia repetir número, o resto estava correto.

# numeros_mega_sena = []
# lista_mega_sena = []

# print("-" * 40)
# print(f'{" JOGOS NA MEGA SENA ":^40}')
# print("-" * 40)
# jogos_gerados = int(input("Quantos jogos quer que eu sorteie? "))
# sleep(1)
# print(f"=-" * 20)
# print(f" {'SORTEANDO':>15} {jogos_gerados} {'JOGOS'} ")
# print("=-" * 20)

# while jogos_gerados > 0:
#     # O FOR ESTÁ ERRADO, POIS PODE SORTEAR NÚMERO REPETIDO
#     # for lista in range(0, 6):
#     #     palpite_mega_sena = randint(0, 60)
#     #     numeros_mega_sena.append(palpite_mega_sena)
#     numeros_mega_sena.sort()
#     lista_mega_sena.append(numeros_mega_sena[:])
#     numeros_mega_sena.clear()
#     jogos_gerados -= 1
#     # print(f"Lista da mega-sena {lista_mega_sena}")

# for posicao, valor in enumerate(lista_mega_sena):
#     sleep(1)
#     print(f"Jogo {posicao+1}: {valor} ")

# print(f"\n{' BOA SORTE!!! ':=^30}")
