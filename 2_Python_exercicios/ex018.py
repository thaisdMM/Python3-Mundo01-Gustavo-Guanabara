from math import radians, sin, cos, tan

angulo_graus = float(input("Para calcular o seno, cosseno e a tangente diginte o valor do ângulo: "))
convertendo_angulo_radianos = radians (angulo_graus)
seno = sin(convertendo_angulo_radianos)
cosseno = cos(convertendo_angulo_radianos)
tangente = tan(convertendo_angulo_radianos)

print(f"O ângulo {angulo_graus} em graus convertido para radianos é: {convertendo_angulo_radianos}")
print(f"seno = {seno:.3f}")
print(f"cosseno = {cosseno:.3f}")
print(f"tangente = {tangente:.3f}")
