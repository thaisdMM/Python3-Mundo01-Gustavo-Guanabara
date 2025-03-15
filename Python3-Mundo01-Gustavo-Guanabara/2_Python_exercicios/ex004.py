#testando o type
# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

#str
informacao = input('Digite alguma informação para testarmos qual é o type: ')
print(type(informacao))
print(f"{informacao} é numérico(isnumeric)? {informacao.isnumeric()}")
print(f"{informacao} é alfabeto(isalpha)? {informacao.isalpha()}")
print(f"{informacao} é letra ou número(isalnum)? {informacao.isalnum()}")
print(f"{informacao} é letra minúscula(islower)? {informacao.islower()}")
print(f"{informacao} é letra maiúscula(isupper)? {informacao.isupper()}")
print(f"{informacao} é espaço vazio(isspace)? {informacao.isspace()}")
print(f"{informacao} é um título(istitle) {informacao.istitle()}")