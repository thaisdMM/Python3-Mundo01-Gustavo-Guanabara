from math import ceil, floor, trunc


numero = float(input("Digite um número real: "))
numero_parte_inteira = print(f"Pegando a porção inteira do {numero} com trunc = {trunc(numero)}")
numero_arredondado_cima = print(f"\nArredondando o {numero} para cima com ceil = {ceil(numero)}")
numero_arredondado_baixo = print(f"Arredondando o {numero} para baixo com floor = {floor(numero)}")
