# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

print("\nCALCULO DO IMC:")
peso = float(input("\nQual o seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso / (altura ** 2)
# print(peso, altura, imc)

if imc < 18.5:
    print(f"\nIMC: {imc:.1f} = Abaixo do Peso.")
# CODIGO PROFESSOR:
# elif imc < 25: # esse foi eu que pensando na correção de outra aula, e funciona perfeitamente
elif 18.5 <= imc < 25:
    print(f"\nIMC: {imc:.1f} = Peso Ideal.")
# elif imc < 30:
elif 25 <= imc < 30:
    print(f"\nIMC: {imc:.1f} = Sobrepeso.")
# elif imc < 40:
elif 30 <= imc < 40:
    print(f"\nIMC: {imc:.1f} = Obesidade.")
else:
    print(f"\nIMC: {imc:.1f} = Obesidade Mórbida")
