quantidade_km_carro = float(input("Quantos km seu carro alugado percorreu? "))
quantidade_dias_carro = int(input("Quantos dias seu carro foi alugado? "))
preco_carro = (quantidade_dias_carro * 60) + (quantidade_km_carro * 0.15)
print(f"O preço a pagar pelo aluguel do carro é {preco_carro:.2f}")