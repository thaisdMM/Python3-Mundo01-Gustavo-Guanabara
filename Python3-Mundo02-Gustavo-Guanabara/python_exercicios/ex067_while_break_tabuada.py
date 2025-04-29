print(f"=-=" * 10, "TABUADA", "=-=" * 10)
print("\nNúmeros negativos param o programa.")
# contador = 1
while True:
    print("-" * 40)
    numero = int(input("\nDigite um número para ver sua tabuada: "))
    print("-" * 40)
    contador = 1
    if numero < 0:
        break
    while contador <= 10:
        print(f"{numero} x {contador:2} = {numero * contador}")
        contador += 1

print(f"Fim do Programa.")

# programa com WHILE AND FOR

while True:
    print("-" * 40)
    numero = int(input("\nDigite um número para ver sua tabuada: "))
    print("-" * 40)
    if numero < 0:
        break
    for i in range(1, 11):
        print(f"{numero} x {i:2} = {numero * i}")

print(f"Fim do Programa.")
