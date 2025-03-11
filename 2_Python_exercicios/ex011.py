#ler largura e altura parede em metros e cacular sua area. Depois caulcualr quantidade de tinta 1 litro pinta area de 2m2

largura_parede = float(input("Digite quantos metros tem a largura da parede: "))
altura_parede = float(input("Digite quantos metros tem a altura da parede: "))
area_parede = largura_parede * altura_parede
tinta_parede = area_parede / 2

print(f"A largura da parede é: {largura_parede} metros e a altura da parede é: {altura_parede} metros.\nDessa forma a área da parede é: {area_parede:.2f} metros quadrados.\nConsiderando que 1 litro de tinta pinta 2 metros quadrados, para pintar essa parede precisariámos de {tinta_parede:.2f} litros de tinta")