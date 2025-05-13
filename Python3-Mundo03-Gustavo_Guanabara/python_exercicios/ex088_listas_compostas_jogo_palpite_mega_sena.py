from random import randint
from time import sleep

# palpite_mega_sena = randint(0,60)
# print(palpite_mega_sena)
numeros_mega_sena = []
lista_mega_sena = []

print("-" * 40)
print("{:^30}".format("JOGOS NA MEGA SENA"))
print("-" * 40)
jogos_gerados = int(input("Quantos jogos quer que eu sorteie? "))
sleep(1)
print(f"=-" * 20)
print(f" SORTEANDO {jogos_gerados} JOGOS ")
print("=-" * 20)

while jogos_gerados > 0:
    for lista in range(0, 6):
        palpite_mega_sena = randint(0, 60)
        numeros_mega_sena.append(palpite_mega_sena)
    numeros_mega_sena.sort()
    lista_mega_sena.append(numeros_mega_sena[:])
    numeros_mega_sena.clear()
    jogos_gerados -= 1
    # print(f"Lista da mega-sena {lista_mega_sena}")

for posicao, valor in enumerate(lista_mega_sena):
    sleep(1)
    print(f"Jogo {posicao+1}: {valor} ")

print(f"BOA SORTE!!!")
