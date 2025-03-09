nome = input("Digite seu nome completo: ")
separa= nome.split()
nome_sem_espaços = nome.replace(" ", "") # para retirar os espaços entre as letras
print(f"Maiúsculo: {nome.upper()}")
print(f"Minúsculo: {nome.lower()}")
print(f"O tamanho do nome com espaços é: {len(nome)}")
print(f"O tamanho do nome sem espaços é: {len(nome_sem_espaços)}")
print(f"O primeiro nome tem {len(separa[0])} letras")