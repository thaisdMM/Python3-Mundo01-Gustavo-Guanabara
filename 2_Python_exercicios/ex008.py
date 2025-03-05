# programa ler um valor em metros e o exibe convertido em centimetros e milimetros
# centímetro: 100 centímetros corresponde a 1 metro. milímetro: 1000 milímetros corresponde a 1 metro.

metros = float(input("Digite o valor em metros para fazermos a conversão em centímetros e milímetros: "))
print(f"{metros} metros convertidos para centímetros são: {metros * 100}. \nJá {metros} metros convertidos em milímetros são: {metros * 1000}")
