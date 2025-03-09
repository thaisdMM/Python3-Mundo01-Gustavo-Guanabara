nome_cidade = input("Digite o nome da cidade: ")
primeiro_nome = nome_cidade.split()
comeca_santo = primeiro_nome[0]
print(f"O nome começa com SANTO?:")
print("SANTO" in comeca_santo.upper())
print(f"\nO nome começa com SANTA?")
print("SANTA" in comeca_santo.upper())
print(f"\nO nome começa com SÃO: ")
print("SÃO" in comeca_santo.upper())