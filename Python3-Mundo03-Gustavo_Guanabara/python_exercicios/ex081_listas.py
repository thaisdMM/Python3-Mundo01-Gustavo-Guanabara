# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#  A) Quantos números foram digitados.
#  B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "SN":
        print("Resposta inválida. Tente novamente.")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break

print("-=" * 30)
print(f"Você digitou {len(valores)} valores.")
valores.sort(reverse=True)
print(f"Os valores digitados em ordem decrescente são: {valores}")
if 5 in valores:
    print(
        f"O valor 5 faz parte da lista. Ele aparece a primeira vez na posição {(valores.index(5))+1}"
    )
else:
    print("O valor 5 não está na lista.")
