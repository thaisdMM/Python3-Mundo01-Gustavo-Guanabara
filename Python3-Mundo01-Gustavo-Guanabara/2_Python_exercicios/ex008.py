# programa ler um valor em metros e o exibe convertido em centimetros e milimetros
# centímetro: 100 centímetros corresponde a 1 metro. milímetro: 1000 milímetros corresponde a 1 metro.

# metros = float(input("Digite o valor em metros para fazermos a conversão em centímetros e milímetros: "))
# print(f"{metros} metros convertidos para centímetros são: {metros * 100}. \nJá {metros} metros convertidos em milímetros são: {metros * 1000}")

medida_metros = float(input("Digite a medida em metros: "))
decimetro = medida_metros * 10
centimetros = medida_metros * 100
milimetros = medida_metros * 1000
decametros = medida_metros * 0.10
hectometros = medida_metros * 0.001
kilometros = medida_metros * 0.0001

print(f"{medida_metros} metros coresponde a: \ndm: {decimetro} \ncm: {centimetros} \nmm: {milimetros} \ndam: {decametros} \nhm: {hectometros:.2f} \nkm: {kilometros:.3f}")
