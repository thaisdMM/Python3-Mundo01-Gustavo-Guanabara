# Fasa um programa qua laia o ano da nascimento de um jovem a informa. de acordo com sua idade:
# - Se ala ainda vai se alistar ao sarviço militar.
# - Sa é a hora de sa alistar.
# - Sejá passou do tampo do alistamanto.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("\nAlistamento Militar:")
ano_nascimento = int(input("\nDigite o ano do seu nascimento: "))
#print(ano_nascimento)
ano_atual = date.today().year
#print(ano_atual)
idade = ano_atual - ano_nascimento
#print(idade)

if idade == 18:
   print(f"\nVocê tem {idade} anos. É HORA DE SE ALISTAR!")
elif idade > 18:
   tempo = idade -18
   print(f"\nVocê tem {idade} anos. JÁ PASSOU DO TEMPOS DE SE ALISTAR {tempo} anos.")
else:
   tempo = 18 - idade
   print(f"\nVocê tem {idade} anos. VOCÊ AINDA VAI SE ALISTAR daqui há {tempo} anos.")