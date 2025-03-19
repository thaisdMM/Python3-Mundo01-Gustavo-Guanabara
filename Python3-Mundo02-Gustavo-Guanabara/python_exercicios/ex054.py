# Crie um programa que laia o ano de nascimanto de sata passoas. No final. mostra quantas passoas ainda não atingiram a maioridade e quantasjf sio maioras.

from datetime import date

ano_atual = date.today().year
#print(ano_atual)
#ano_nascimento = int(input("Qual ano você nasceu? "))
#idade = ano_atual - ano_nascimento
#print(idade)
maioridade = 0
salvar_idade = " "

for i in range(0,7):
   ano_nascimento = int(input("Qual ano você nasceu? "))
   idade = ano_atual - ano_nascimento
#   print(idade)
   salvar_idade += f"{idade}, "
   if idade >= 21:
      maioridade += 1
print(f"A idade de todos são: {salvar_idade}")
print(f"Considerando 21 anos maioridade. Das 7 pessoas, {maioridade} são maiores de idade.")
