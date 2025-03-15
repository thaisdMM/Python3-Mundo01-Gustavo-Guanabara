nome = input("Digite o seu nome completo: ").strip()
nome_separado = nome.split()
print(f"O nome digitato foi {nome}")
print(f"Primeiro nome: {nome_separado[0]}")
print(f"Último nome: {nome_separado[-1]}")
# print(f"Último nome: {nome_separado[len(nome_separado)-1]}") #codigo do professor