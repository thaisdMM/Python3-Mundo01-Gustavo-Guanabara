dados_pessoas = list()
pessoa = dict()
mulheres_cadastradas = []
total_idade = 0
while True:
    pessoa["nome"] = input("Nome: ").strip().capitalize()
    pessoa["idade"] = int(input("Idade: "))
    total_idade += pessoa["idade"]
    print(f"total idade {total_idade}")
    pessoa["sexo"] = input("Sexo: [M/F]").strip().upper()[0]
    # if pessoa["sexo"] == "F":
    #     mulheres_cadastradas.append(pessoa["nome"])
    #     print(f"mulheres_cadastradas {mulheres_cadastradas}")
    dados_pessoas.append(pessoa.copy())
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
print(f"A lista de dados de pessoas é: {dados_pessoas}")
print(f"Ao todo foram cadastradas {len(dados_pessoas)} pessoas.")
media_idade = total_idade / len(dados_pessoas)
print(f"A média de idade das pessoas cadastradas foi: {media_idade:.2f}")
print(f"As mulheres cadastradas foram: ", end="")
# abaixo nao serve, pois apenas mostra a ultima pessoa cadastrada
# print(f"dicionario final: {pessoa}")
# for key, valor in pessoa.items():
#     print(f"dicinario for key {key} {valor}")

for valor in dados_pessoas:
    if valor["sexo"] == "F":
        print(valor["nome"], end=" ")
    # print(f"valor da lista no for: {valor}")
    # for key, value in valor.items():
    #     print(key)
    #     print(value)
    #     if key == "sexo" and value == "F":
    #         print("sexo femino")
    #         print(f"{}")
    # # print(f"valor[0][5] {valor[0][5]}")
    # if valor["sexo"] == "F":
    #     print("mulher")




#print(f"dados_pessoas['sexo] {dados_pessoas['sexo']}")
# for valor in dados_pessoas:
#     print(valor)