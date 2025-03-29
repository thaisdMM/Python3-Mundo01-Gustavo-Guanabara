print(f"=-=" * 10, "TABUADA", "=-=" * 10)
print("\n0 e números negativos param o programa.")
contador = 0
while True:
    print("-" * 40)
    numero = int(input("\nDigite um número para ver sua tabuada: "))
    print("-" * 40)
    if numero < 0:
        break
    for i in range(1, 11):
        print(f"{numero} x {i:2} = {numero * i}")
print(f"Fim do Programa.")
