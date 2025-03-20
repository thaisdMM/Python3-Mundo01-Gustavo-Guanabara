# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print("-=-" * 20)
print("CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFÍCIO")
print("-=-" * 20)
sleep(1)
print("\nVai começar:")
sleep(1)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("🎉💥 FOGO!!! 💥🎊")
