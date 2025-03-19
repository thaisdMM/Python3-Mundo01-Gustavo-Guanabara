#Desanvolva um programa que laig o nome, idade o sexo da 4 passoas. No final do programa, mostra: 
# A média da idade do grupo.
# › Qual é o nome do homem mais valho.
# › Quantas mulheras têm manos de 20 anOs.
soma_idades = 0
mulher_menor_20 = 0
maior_idade_homem = 0
homem_mais_velho_range = False
nome_homem_mais_velho = " "

for i in range(0,4):
   nome = input("Digite o seu nome: ").strip().upper()
   idade = int(input("Qual a sua idade? "))
   sexo = int(input("SEXO: 1 para MASCULINO ou 2 para FEMININO: "))
   soma_idades += idade
   media_idade = soma_idades // 4

   if sexo == 2 and idade < 20:
      mulher_menor_20 += 1

   
   if sexo == 1:
      homem_mais_velho_range = True
      maior_idade_homem = idade
      nome_homem_mais_velho = nome
   if idade > maior_idade_homem:
      maior_idade_homem = idade
      nome_homem_mais_velho = nome

print(media_idade)
print(maior_idade_homem)
print(nome_homem_mais_velho)
print(mulher_menor_20)