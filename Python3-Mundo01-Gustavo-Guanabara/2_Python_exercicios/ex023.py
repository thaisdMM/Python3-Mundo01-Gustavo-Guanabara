# Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = input("Digite um numero de 0 a 9999: ")
numero = numero.zfill(4) # Garante que a string tenha exatamente 4 caracteres  
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f""" unidade = {unidade}
dezena = {dezena}
centena = {centena}
milhar = {milhar} """)

# CORREÇÃO PROFESSOR

num = int(input("\nInforme um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"unidade = {u}")
print(f"dezena = {d}")
print(f"centena = {c}")
print(f"milhar = {m}")