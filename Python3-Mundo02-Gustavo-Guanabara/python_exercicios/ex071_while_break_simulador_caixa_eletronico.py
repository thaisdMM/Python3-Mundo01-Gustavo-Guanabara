# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# RESPOSTA MAS DE MANEIRA MATEMÁTICA
#  print("-" * 15)
# print("BANCO MOREIRA")
# print("-" * 15)
# cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
# while True:
#     valor = int(input("Qual o valor você quer sacar? R$ "))

#     for i in range(valor):
#         if valor / 50:
#             cedulas_50 = valor // 50
#         if (valor % 50 != 0) / 20:
#             cedulas_20 = (valor % 50) // 20
#         if (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) / 10:
#             cedulas_10 = (valor - ((cedulas_50 * 50) + (cedulas_20 * 20))) // 10
#         if (valor - ((cedulas_50 * 50) + (cedulas_20 * 20) + (cedulas_10 * 10))) / 1:
#             cedulas_1 = (
#                 valor - ((cedulas_50 * 50) + (cedulas_20 * 20) + (cedulas_10 * 10))
#             ) // 1
#     break

# print(f"Total de {cedulas_50} cedulas de R$50")
# print(f"Total de {cedulas_20} cédulas de R$20")
# print(f"Total de {cedulas_10} cédulas de R$10")
# print(f"Total de {cedulas_1} cédulas de R$1")

# print("\nFim do Programa.")

# TENTANDO DE OUTRA FORMA

print("-" * 15)
print("BANCO MOREIRA")
print("-" * 15)

valor = int(input("Qual valor você quer sacar? R$"))
valor_atual = valor_restante = quantia_entregue = troca_cedula = 0
cedula = 50
while valor != 0:
    valor_atual = valor // cedula
    quantia_entregue = valor_atual * cedula
    valor_restante = valor - quantia_entregue
    print(valor_atual)
    print(quantia_entregue)
    print(valor_restante)
    print(f"Total de {valor_atual} cedulas de R$50")
    troca_cedula +=1
    cedula = 20
    valor_atual = valor_restante // cedula
    print(valor_atual)
    print(quantia_entregue)
    print(valor_restante)
    print(f"Total de {valor_atual} cedulas de R$20")
    troca_cedula +=1
    cedula = 10
    print(valor_atual)
    print(quantia_entregue)
    print(valor_restante)
    print(f"Total de {valor_atual} cedulas de R$10")

    break


print("\nPrograma finalizado.")
