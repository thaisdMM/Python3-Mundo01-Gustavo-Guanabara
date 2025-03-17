# Escrava um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai parguntar o valor da casa, o salário do comprador o em quantos anos ala vai pagar-
# Calcula o valor da prostação mensal. sabando que ala não poda exceder 30% do salário ou então o emprestimo sarÁ negado

print("\nEMPRÉSTIMO BANCÁRIO para compra de imóvel.")
valor_casa = float(input("\nQual o valor da casa? R$"))
#print(f"{valor_casa:.2f}")
salario_comprador = float(input("Qual o valor do seu salário? R$"))
#print(f"{salario_comprador:.2f}")
anos_pagamento = int(input("Quantos anos você deseja pagar a casa?"))
converter_anos_meses = anos_pagamento * 12
#print(converter_anos_meses)
prestacao_mensal = valor_casa / converter_anos_meses
#print(prestacao_mensal)
limite_30_salario = salario_comprador * 30 / 100
#print(limite_30_salario)

if prestacao_mensal > limite_30_salario:
   print(f"\nNEGADO. O valor mensal da prestação é: R${prestacao_mensal:.2f} e excede 30% do seu salario: {limite_30_salario:.2f}")
else:
   print(f"APROVADO! O valor mensal da prestação é: R${prestacao_mensal:.2f} e não excede a 30% do seu salário: {limite_30_salario:.2f}")
                       