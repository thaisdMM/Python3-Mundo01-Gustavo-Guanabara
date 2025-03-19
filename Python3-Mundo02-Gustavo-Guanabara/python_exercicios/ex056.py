#Desanvolva um programa que laig o nome, idade o sexo da 4 passoas. No final do programa, mostra: 
# A média da idade do grupo.
# › Qual é o nome do homem mais valho.
# › Quantas mulheras têm manos de 20 anOs.
soma_idades = 0

for i in range(0,4):
   nome = input("Digite o seu nome: ").strip().upper()
   idade = int(input("Qual a sua idade? "))
   sexo = int(input("SEXO: 1 para MASCULINO ou 2 para FEMININO: "))
   soma_idades += idade
   media_idade = soma_idades // 4

print(media_idade)
print(nome, idade, sexo)