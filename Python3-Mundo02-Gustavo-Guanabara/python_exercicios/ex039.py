# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print("\nAlistamento Militar:")

sexo = input("Digite: M para masculino ou F para feminino: ").strip().upper()
if sexo == "F":
    print("Você é mulher e não precisa fazer o alistamento militar obrigatório.")

elif sexo == "M":
   ano_nascimento = int(input("\nDigite o ano do seu nascimento: "))
   # print(ano_nascimento)
   ano_atual = date.today().year
   # print(ano_atual)
   idade = ano_atual - ano_nascimento
   # print(idade)

   if idade == 18:
      print(f"\nVocê tem {idade} anos. É HORA DE SE ALISTAR!")
   elif idade > 18:
      tempo = idade - 18
      print(
         f"\nVocê tem {idade} anos. JÁ PASSOU DO TEMPO DE SE ALISTAR {tempo} anos.")
      print(f"Você deveria ter se alistado em {ano_nascimento + 18}")  # eu
   else:
      tempo = 18 - idade
      print(
         f"\nVocê tem {idade} anos. VOCÊ AINDA VAI SE ALISTAR daqui há {tempo} anos.")
      print(f"Você vai se alistar em: {ano_atual + tempo}")  # professor
else:
   print(f"Opção inválida. Tente novamente!")
print("\nPrograma finalizado.")
