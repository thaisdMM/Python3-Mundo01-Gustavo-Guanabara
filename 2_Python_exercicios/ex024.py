nome_cidade = input("Digite o nome da cidade: ")
primeiro_nome = nome_cidade.split()
comeca_santo = primeiro_nome[0]
print(f"O nome {nome_cidade} começa com SANTO/santo?:")
print("SANTO" in comeca_santo.upper())
print(f"\nO nome {nome_cidade} começa com SANTA/santa?")
print("SANTA" in comeca_santo.upper())
print(f"\nO nome {nome_cidade} começa com SÃO/são?")
print("SÃO" in comeca_santo.upper())