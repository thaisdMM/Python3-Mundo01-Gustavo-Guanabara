dados_pessoas = list()
pessoa = dict()
total_idade = 0
while True:
    pessoa["nome"] = input("Nome: ").strip().capitalize()
    pessoa["sexo"] = input("Sexo: [M/F] ").strip().upper()[0]
    pessoa["idade"] = int(input("Idade: "))
    total_idade += pessoa["idade"]
    # print(f"total idade {total_idade}")
    dados_pessoas.append(pessoa.copy())
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
# print(f"A lista de dados de pessoas é: {dados_pessoas}")
print("-" * 30)
print(f"Ao todo foram cadastradas {len(dados_pessoas)} pessoas.")
media_idade = total_idade / len(dados_pessoas)
print(f"A média de idade das pessoas cadastradas foi: {media_idade:.2f}")
print(f"As mulheres cadastradas foram: ", end="")
for valor in dados_pessoas:
    if valor["sexo"] == "F":
        print(valor["nome"], end=" ")
print()
print(f"Lista de pessoas que estão acima da média da idade:")
for valor in dados_pessoas:
    for key, value in valor.items():
        if valor["idade"] > media_idade:
            print(f"{key} = {value}; ", end="")
    print()
print("<< ENCERRADO >>")
