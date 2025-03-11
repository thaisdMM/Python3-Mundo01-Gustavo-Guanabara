# Desenvolva um programa que pargunte a distância da uma viagem em Km. Calcula o preço da passagem, cobrando R50.50 por Km para viagens de ate 200km a R$0.45 para viagens mais longas.

distancia_viagem = int(input("Quantos kilometros tem a viagem? "))
passagem1 = distancia_viagem * 0.50
passagem2 = distancia_viagem * 0.45
if distancia_viagem <= 200:
   print(f"A viagem tem {distancia_viagem}Km.\nO preço da passagem é R$: {passagem1:.2f}")
else:
   print(f"A viagem tem {distancia_viagem}Km.\nO preço da passagem é R$: {passagem2:.2f}")