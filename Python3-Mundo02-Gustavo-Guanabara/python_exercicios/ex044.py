# Elabore um programa que calcula o valor a ser pago por um produto. considerando o sau preço normal a condição de pagamento:
# - à vista dinhairot chaque: 10 da desconto
# - à vista no cartão: 5% de desconto
# - am até 2u no cartão: prafo normal
# - 3н ou mais no cartão:
# 20z da juros

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


