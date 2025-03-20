# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
# print(ano_atual)
# ano_nascimento = int(input("Qual ano você nasceu? "))
# idade = ano_atual - ano_nascimento
# print(idade)
maioridade = 0
salvar_idade = " "

for i in range(0, 7):
    ano_nascimento = int(input("Em que ano a pessoa nasceu? "))
    idade = ano_atual - ano_nascimento
#   print(idade)
    salvar_idade += f"{idade}, "
    if idade >= 21:
        maioridade += 1
print(f"A idade de todos são: {salvar_idade}")
print("Considerando 21 anos maioridade:")
print(f"{7 - maioridade} pessoas são MENORES  de idade e {maioridade} são MAIORES de idade.")
