# ler preço produto, novo preço com 5% desconto - porcentagem pode ser assim preco_produto*5/100

preco_produto = float(input("Digite o preço do produto:R$ "))
print(f"O valor do produto era {preco_produto:.2f}.\nO novo preço do produto com o desconto de 5% é R$: {preco_produto - (preco_produto * 0.05):.2f}")
