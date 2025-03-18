numero = int(input("Digite um número para saber sua tabuada: "))

print(f"\nTabuada de {numero}")
print("-=-" * 5)
for i in range(1, 11):
    print(f"{numero} x {i:2} = {i * numero}")

print("-=-" * 5)
print("\nFim do programa.")
