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
valor_atual = valor_restante = quantia_entregue = troca_cedula = numero_cedulas = 0
cedula = 50
while True:

    valor_atual = valor
    numero_cedulas = valor_atual // cedula
    quantia_entregue = numero_cedulas * cedula
    valor_restante = valor_atual - quantia_entregue
    valor = valor_restante
    # print(f"VALOR ATUAL: {valor_atual}")
    # print(f"NUMERO DE CEDULAS: {numero_cedulas}")
    # print(f"QUANTIA ENTREGUE: {quantia_entregue}")
    # print(f"VALOR RESTANTE: {valor_restante}")
    print(f"Total de {numero_cedulas} cedulas de R${cedula}")
    # print(f"VALOR ATUALIZADO {valor}")
    troca_cedula += 1
    if valor_restante == 0:
        break
    elif cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1

# print(f"TROCA DE CEDULA: {troca_cedula}")

print("\nPrograma finalizado.")
