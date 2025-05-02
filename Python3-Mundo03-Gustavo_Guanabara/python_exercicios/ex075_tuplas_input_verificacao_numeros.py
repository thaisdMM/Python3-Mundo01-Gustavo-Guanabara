contador = 0
valores = ()
# print(type(valores))
for i in range(1, 5):
    numero = int(input("Digite um valor: "))
    valores += (numero,)
    # print(type(valores))
print(f"Você digitou os valores: {valores}")
print(type(valores))
print(f"O valor 9 apareceu: {valores.count(9)} vezes.")
if 3 in valores:
    print(f"O valor 3 apareceu: {valores.index(3)+1}ª posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
par = ()
for verifica_par in valores:
    if verifica_par % 2 == 0:
        par += (verifica_par,)
print(f"Os numeros pares digitados foram: {par}")

# for numeros in valores:
#     if numeros

# valores = (int(input("valor: ")))
# print(type(valores))

# numero = int(input("Digite um valor: "))
# valor = ()
# valor = (numero)
# print(i)
# print(f"VALOR: {valor}")
# print(numero)
# contador += 1
# valor(numero, numero)
