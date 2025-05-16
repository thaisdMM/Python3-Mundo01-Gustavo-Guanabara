# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date, datetime

pessoa = {}
pessoa["nome"] = input("Nome: ").strip().title()
ano_nascimento = int(input("Ano de Nascimento: "))
ano_atual = date.today().year
# # EXISTE TAMBÉM A FORMA ABAIXO, MAS COMO É APENAS PARA ANO A DE CIMA É MAIS LIMPA
# # datetime.now().year> Inclui data e hora (ano, mês, dia, hora, minuto, segundo, etc).
# ano_atual2 = datetime.now().year
# print(f"Ano com date {ano_atual} e ano com datetime {ano_atual2}")
idade = ano_atual - ano_nascimento
pessoa["idade"] = idade
pessoa["ctps"] = int(input("Carteira de Trabalho (0 = não tem) "))
if pessoa["ctps"] != 0:
    pessoa["contratação"] = int(input("Ano de contratação: "))
    pessoa["salário"] = float(input("Salário: R$ "))
    tempo_contribuicao = ano_atual - pessoa["contratação"]
    pessoa["apossentadoria"] = (35 - tempo_contribuicao) + idade
# #print(f"tempo de contribuição: {tempo_contribuicao}")
# #print(f"aposentadoria: {pessoa["aposentadoria"]}")
# print(f"Dados da pessoa: {pessoa}")
print("=-" * 5, f" DADOS DA PESSOA ", "=-" * 5)
for key, value in pessoa.items():
    print(f"{key} tem o valor: {value}")
