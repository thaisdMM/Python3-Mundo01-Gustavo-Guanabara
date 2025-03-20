# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input("Digite um número para saber sua tabuada: "))

print(f"\nTabuada de {numero}")
print("-=-" * 5)
for i in range(1, 11):
    print(f"{numero} x {i:2} = {i * numero}")

print("-=-" * 5)
print("\nFim do programa.")
