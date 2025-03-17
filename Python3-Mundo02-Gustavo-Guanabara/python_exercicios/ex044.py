# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

print("VALOR A SER PAGO POR UM PRODUTO")
valor_produto = float(input("Qual o valor do produto? R$"))
condicao_pagamento = input("Formas de pagamento: dinheiro, cheque, cartão. Digite a sua forma: ").strip().lower()
print(condicao_pagamento)
if condicao_pagamento == "dinheiro" or condicao_pagamento == "cheque":
   print(f"O preço para pagamento à vista no {condicao_pagamento} é: R${valor_produto - (valor_produto * 10 / 100):.2f}")
elif condicao_pagamento == "cartao" or condicao_pagamento == "cartão":
   forma_pagamento = input("Digite 1 para à vista ou 2 para à prazo: ")
   #print(forma_pagamento)
   if forma_pagamento == "1":
      print(f"O preço para pagamento no {condicao_pagamento} à vista é: R${valor_produto - (valor_produto * 5 / 100):.2f}")
   else:
      parcelamento = int(input("Em quantas vezes você deseja parcelar? "))
      if parcelamento <= 2:
         print(f"\nO preço para o pagamento parcelado no {condicao_pagamento} é R${valor_produto:.2f}.")
         print(f"Serão {parcelamento} parcelas. O valor da parcela será {valor_produto / parcelamento:.2f}")
      else:
         print(f"\nO preço para o pagamento parcelado no {condicao_pagamento} é R${valor_produto + (valor_produto * 20 / 100)}")
         print(f"Serão {parcelamento} parcelas. O valor da parcela será {valor_produto / parcelamento:.2f}")


