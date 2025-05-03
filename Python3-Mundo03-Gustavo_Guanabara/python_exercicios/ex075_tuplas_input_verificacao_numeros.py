contador = 0
valores = ()
# print(type(valores))
for i in range(1, 5):
    numero = int(input("Digite um valor: "))
    valores += (numero,)
    # print(type(valores))
print(f"Você digitou os valores: {valores}")
# print(type(valores))
print(f"O valor 9 apareceu: {valores.count(9)} vezes.")
if 3 in valores:
    print(f"O valor 3 apareceu: {valores.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
# par = ()
print(f"Os valores pares digitados foram: ", end=" ")
for verifica_par in valores:
    if verifica_par % 2 == 0:
        print(verifica_par, end=" ")
        # par += (verifica_par,)
# print(f"Os numeros pares digitados foram: {par}")

# CORREÇÃO PROFESSOR:

numero = (
    int(input("\nDigite um número: ")),
    int(input("Digite outro número: ")),
    int(input("Digite mais um número: ")),
    int(input("Digite o último número: ")),
)
print(f"Você digitou os valores: {numero}")
print(f"O valor 9 apareceu {numero.count(9)} vezes.")
if 3 in numero:
    print(f"O valor 3 apareceu na {numero.index(3)+1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print(f"Os valores pares digitados foram: ", end=" ")
for verifica_par in numero:
    if verifica_par % 2 == 0:
        print(verifica_par, end=" ")
