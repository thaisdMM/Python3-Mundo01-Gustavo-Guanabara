# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
contador = 0
while True:
    if contador == 0:
        valor = int(input("Digite um valor: "))
        valores.append(valor)
        print(f"Valor {valor} adicionado com sucesso!")
        # print(f"Valore: {valores}")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        contador += 1
    else:
        while continuar not in "NS":
            print("Resposta inválida. Digite [S/N]")
            continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
        if continuar == "N":
            break
        if continuar == "S":
            valor = int(input("Digite um valor: "))
            if valor not in valores:
                valores.append(valor)
                print(f"Valor {valor} adicionado com sucesso!")
                contador += 1
            elif valor in valores:
                print("Valor duplicado. Não vou adicionar.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
print("=-" * 30)
# print(valores)

# sem mudar a lista:
#  print(sorted(valores))
# mudando a lista:
valores.sort()

print(f"\nVocê digitou {contador} valores. São: {valores}")
