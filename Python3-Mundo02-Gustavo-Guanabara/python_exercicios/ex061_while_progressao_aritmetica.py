print("Progressao Aritmética")

primeiro_termo_pa = int(input("Digite o primeiro termo da PA:"))
razao_pa = int(input("Digite a razão da PA: "))
termos_pa = 0
numero_termos = 0

while numero_termos <= 10:
    print(primeiro_termo_pa, end= ", ")
    primeiro_termo_pa += razao_pa
    numero_termos +=1
    #print(numero_termos)
    #print(termos_pa)
    

# while numero_termos < 10:
#     termos_pa = primeiro_termo_pa
#     termos_pa += razao_pa
#     #print(termos_pa, end= ", ")
#     numero_termos +=1
#     #print(numero_termos, end="")

# # print(primeiro_termo_pa, end=", ")
