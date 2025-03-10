# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome_cidade = input("Digite o nome da cidade: ")
separa_nome = nome_cidade.split()
comeca_santo = separa_nome[0]
print(f"O nome {nome_cidade} começa com SANTO/santo?:")
print("SANTO" in comeca_santo.upper())
print(f"\nO nome {nome_cidade} começa com SANTA/santa?")
print("SANTA" in comeca_santo.upper())
print(f"\nO nome {nome_cidade} começa com SÃO/são?")
print("SÃO" in comeca_santo.upper())

# Resolução professor

cid = input("Digite a cidade em que você nasceu: ").strip()
print(cid[:5].upper() == "SANTO")