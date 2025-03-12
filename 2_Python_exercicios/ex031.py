# Desenvolva um programa que pergunte a distância da uma viagem em Km. Calcula o preço da passagem, cobrando R$0.50 por Km para viagens de ate 200km a R$0.45 para viagens mais longas.


# Meu código
#distancia_viagem = float(input("Quantos kilometros tem a viagem? "))
# passagem1 = distancia_viagem * 0.50
# passagem2 = distancia_viagem * 0.45
# if distancia_viagem <= 200:
#    print(f"A viagem tem {distancia_viagem}Km.\nO preço da passagem é R$: {passagem1:.2f}")
# else:
#    print(f"A viagem tem {distancia_viagem}Km.\nO preço da passagem é R$: {passagem2:.2f}")

# #código do professor 1

# distancia = float(input("Qual a distância da viagem? "))
# print(f"Você está prestes a começar uma viagem de {distancia} Km.")
# if distancia <= 200:
#    preço = distancia * 0.50
# else:
#    preço = distancia * 0.45
# print(f"E o preço da sua passagem será de {preço}")

#codigo 2 simplificado
distancia = float(input("Qual a distancia da viagem? "))
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f"O preço da sua passagem será {preco}")