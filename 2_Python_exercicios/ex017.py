from math import hypot

cateto_oposto_triangulo = float(input("Digite o cumprimento do cateto oposto do triâgulo = "))
cateto_adjacente_triangulo = float(input("Digite o cumprimento do cateto adjacente do triâncgulo= "))
hipotenusa_triangulo = hypot(cateto_oposto_triangulo, cateto_adjacente_triangulo)

print(f"O cumprimento da hipotenusa do triangulo com {cateto_oposto_triangulo} e {cateto_adjacente_triangulo} é = {hipotenusa_triangulo:.2f}")