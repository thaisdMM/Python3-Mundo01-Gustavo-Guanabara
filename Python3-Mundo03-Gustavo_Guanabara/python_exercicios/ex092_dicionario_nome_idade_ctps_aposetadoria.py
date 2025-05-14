from datetime import date

pessoa = {}
pessoa["nome"] = input("Nome: ").strip().capitalize()
ano_nascimento = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
pessoa["idade"] = idade
while True:
    pessoa["ctps"] = int(input("Carteira de Trabalho (0 = não tem) "))
    if pessoa["ctps"] == 0:
        break
    else:
        pessoa["contratação"] = int(input("Ano de contratação: "))
        pessoa["salário"] = float(input("Salário: R$ "))
        tempo_contribuicao = ano_atual - pessoa["contratação"]
        pessoa["apossentadoria"] = (35 - tempo_contribuicao) + idade

        break
# tempo_contribuicao = ano_atual - pessoa["contratação"]
# #print(f"tempo de contribuição: {tempo_contribuicao}")
# aposentadoria = (35 - tempo_contribuicao) + idade
# #print(f"aposentadoria: {aposentadoria}")
# pessoa["aposentadoria"] = aposentadoria
# print(f"Dados da pessoa: {pessoa}")
print("=-" * 5, f" DADOS DA PESSOA ", "=-" * 5)
for key, value in pessoa.items():
    print(f"{key} tem o valor: {value}")
