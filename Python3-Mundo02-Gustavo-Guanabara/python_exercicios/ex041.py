# A ConfadoraSão Nacional de NataÇão precisa de um programa que laig o ano de nascimento de um atlata a mostra sua categoria. da acordo com a idada:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

print("\nCATEGORIA DE NATAÇÂO DA CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
ano_atual = date.today().year
ano_nascimento = int(input("\nDigite o ano que você nasceu: "))
idade = ano_atual - ano_nascimento
#print(idade)
if idade <= 9:
   print(f"\n{idade} anos: categoria MIRIM.")
elif idade > 9 and idade <= 14:
   print(f"\n{idade} anos: categoria INFANTIL.")
elif idade > 14 and idade <= 19:
   print(f"\n{idade} anos: categoria JUNIOR.")
elif idade > 19 and idade <= 20:
   print(f"\n{idade} anos: categoria SÊNIOR.")
else:
   print(f"\n{idade} anos: categoria MASTER.")