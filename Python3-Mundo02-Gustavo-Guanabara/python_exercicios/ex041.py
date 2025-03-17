# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

print("\nCATEGORIA DE NATAÇÂO DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
ano_atual = date.today().year
ano_nascimento = int(input("\nDigite o ano que você nasceu: "))
idade = ano_atual - ano_nascimento
#correção professor, as comparações anteriores(ex: idade >7 and idade <=14) eram desnecessárias, pois vai entrando de condição a condição
if idade <= 9:
   print(f"\n{idade} anos: categoria MIRIM.")
elif idade <= 14:
   print(f"\n{idade} anos: categoria INFANTIL.")
elif idade <= 19:
   print(f"\n{idade} anos: categoria JUNIOR.")
elif idade <= 25:
   print(f"\n{idade} anos: categoria SÊNIOR.")
else:
   print(f"\n{idade} anos: categoria MASTER.")