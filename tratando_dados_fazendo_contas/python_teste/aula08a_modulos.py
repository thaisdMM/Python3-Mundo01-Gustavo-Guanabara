#BIBLIOTECA PADRÃO https://docs.python.org/3.11/library/random.html

# # utilizando a biblioteca importanto tudo
# import math

# num = int(input("Digite um número: "))
# raiz = math.sqrt(num)
# print(f"A raiz quadradade de {num} é = a {math.floor(raiz)}") # math.ceil(raiz) arrendondar para cima; math.floor(raiz) arredonda para baixo

# #importando só raiz quadrada
# from math import sqrt, ceil
# num = int(input("Digite um número: "))
# raiz = sqrt(num)
# print(f"A raiz quadrada de {num} = {ceil(raiz)}")


# import random
# # num = random.random() # numero aleatório entre 0 e 1
# num = random.randint(1,10) # número inteiro de 1 até 10
# print(num)

# BIBLIOTECAS EXTERNAS 
import emoji
print(emoji.emojize("Olá, Mundo :thumbs_up: 🌍"))