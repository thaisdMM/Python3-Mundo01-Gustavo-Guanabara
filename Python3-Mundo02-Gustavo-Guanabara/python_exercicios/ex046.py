# Fafa um programa que mostra na tala uma contagem regressiva parg o estouro da fogos de artificio, indo de 10 até O, com uma pausa de 1 segundo antra clas.

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