# numero = int(input("Digite um número: "))

n = cont = 0

# 999 flag no while
# while n != 999:
#     n = int(input("Digite um número: "))
#     cont += 1

# while cont < 5:
#     n = int(input("Digite um número: "))
#     cont += 1

# # Aqui a soma conta o 999
# n = s = 0
# while n != 999:
#     n = int(input("Digite um número: "))
#     s += n
# print(f"A soma vale {s}")

# # Aqui TEM UM LOOPING INFINITO
# n = s = 0
# while True:
#     n = int(input("Digite um número: "))
#     s += n
# print(f"A soma vale {s}")

# Aqui a soma NÃO conta o 999 porque tem um BREAK
n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print(f"A soma vale {s}")

# f'string
nome = "José"
idade = 33
print(f"o {nome} tem {idade} anos.")
