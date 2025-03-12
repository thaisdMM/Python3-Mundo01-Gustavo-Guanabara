# Escreva um programa que pargunte o salário de um Funcionário e calcula o valor do seu aumento.
#Para salários suparioras a R$1.250.00, calcule um aumento de 10%
#Para os inferioras ou iguais, o aumento é de 15%

salario = float(input("Qual o seu salário? "))
aumento1 = salario + (salario * 10/100)
#print(aumento1) # testar a variável
aumento2 = salario + (salario * 15/100)
#print(aumento2) # testando se variável está funcionando corretamente antes de implentar todo código

if salario > 1250:
   print(f"Seu salário é R$ {salario} e vai aumentar para {aumento1:.2f}")
else:
   print(f"Seu salário é R$ {salario} e vai aumentar para {aumento2:.2f}")