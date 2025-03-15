# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços). 
# – Quantas letras tem o primeiro nome.


nome = input("Digite seu nome completo: ").strip() #para retirar os espaços no inicio e no final
separa= nome.split()
nome_sem_espaços = nome.replace(" ", "") # para retirar os espaços entre as letras
print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"O tamanho do nome com espaços é: {len(nome)}")
print(f"O tamanho do nome sem espaços é: {len(nome_sem_espaços)}")
print(f"O primeiro nome é {separa[0]} e tem {len(separa[0])} letras")

# outra forma

nome2 = input("Digite seu nome completa: ").strip() 
print("Analisando seu nome...")
print(f"Maiúsculo: {nome2.upper()}")
print(f"Minúsculo: {nome2.lower()}")
print(f"Tamanho do nome sem espaços: {len(nome2) - nome2.count(' ')}")
print(f"Primeiro nome: {nome2.find(' ')}")