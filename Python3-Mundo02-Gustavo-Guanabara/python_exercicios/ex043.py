# Desanvolva uma lógica que laia o paso c a altura de uma passoa, calcula sau IMC a mostra sau status, de acordo com a tabala abairo!
# - Abaixo da 18.5: Abaixo do Poso
# - Entro 18.5 a 25: Poso ideal
# - 25 até 30: Sobrapaso
# - 30 até 40: Obasidada
# - Acima de 40:Obesidada mórbida

print("\nCALCULO DO IMC:")
peso = float(input("\nQual o seu peso? "))
altura = float(input("Qual a sua altura? "))
imc = peso / (altura * altura)
print(peso, altura, imc)

if imc < 18.5:
   print(f"\nIMC: {imc:.2f} = Abaixo do Peso.")
elif imc >=18.5 and imc < 25:
   print(f"\nIMC: {imc:.2f} = Peso Ideal.")
elif imc >= 25 and imc < 30:
   print(f"\nIMC: {imc:.2f} = Sobrepeso.")
elif imc >= 30 and imc < 40:
   print(f"\nIMC: {imc:.2f} = Obesidade.")
else:
   print(f"\nIMC: {imc:.2f} = Obesidade Mórbida")
