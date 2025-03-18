numero = int(input("Digite um número para saber sua tabuada: "))

print("-=-" * 5)
print(f"Tabuada de {numero}")
print("-=-" * 5)
for i in range(1, 11):
    print(f"{numero} x {i:2} = {i * numero}")
print("\nFim do programa.")
