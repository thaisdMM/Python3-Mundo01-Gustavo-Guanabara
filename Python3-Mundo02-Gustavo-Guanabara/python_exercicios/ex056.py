# Desanvolva um programa que laig o nome, idade o sexo da 4 passoas. No final do programa, mostra:
# A média da idade do grupo.
# › Qual é o nome do homem mais valho.
# › Quantas mulheras têm manos de 20 anOs.
soma_idades = 0
mulher_menor_20 = 0
maior_idade_homem = 0
homem_mais_velho_range = False
nome_homem_mais_velho = " "

for i in range(0, 4):
    nome = input("Digite o seu nome: ").strip().upper()
    idade = int(input("Qual a sua idade? "))
    print("Informe qual é o seu SEXO?")
    sexo = int(input("""
   [ 1 ] MASCULINO 
   [ 2 ] FEMININO \n"""))
    soma_idades += idade

    if sexo == 2 and idade < 20:
        mulher_menor_20 += 1

    if sexo == 1:
      # PRIMEIRO homem encontrado
        if homem_mais_velho_range == False:  # checar o primeiro e salvar os dados do primeiro
            homem_mais_velho_range = True
            maior_idade_homem = idade
            nome_homem_mais_velho = nome
        else:
            # JÁ encontramos outro homem antes
            if maior_idade_homem < idade:
                maior_idade_homem = idade
                nome_homem_mais_velho = nome

media_idade = soma_idades // 4
print(f"\nMÉDIA DAS IDADES = {media_idade}")
print(f"IDADE DO HOMEM MAIS VELHO = {maior_idade_homem}")
print(f"NOME DO HOMEM MAIS VELHO: {nome_homem_mais_velho}")
print(f"NÚMERO DE MULHERES COM MENOS DE 20 ANOS = {mulher_menor_20}")
print("\nPrograma finalizado.")
