#preco produto, desconto 15% a vista, juros 8% a prazo

preco_produto = float(input("Qual o preço do produto? R$: "))
pagamento_a_vista = preco_produto - (preco_produto*15/100)
pagamento_a_prazo = preco_produto + (preco_produto*8/100)
print(f"O produto custa R$ {preco_produto}\nSe pagar à vista tem desconto de 15% e o preço do produto fica R$ {pagamento_a_vista:.2f}\nSe pagar a prazo temos um juros de 8% e o preço do produto fica R$ {pagamento_a_prazo:.2f}")