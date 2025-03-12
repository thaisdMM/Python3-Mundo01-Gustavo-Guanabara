#Faça um programa que leia um ano qualquar a mostra sa ele é BISSEXTO.

# ano bissexto acontece de 4 em 4 anos > ano 366 dias > 
# exceto: exceto anos múltiplos de 100 que não são múltiplos de 400

# #MEU CÓDIGO
# ano = int(input("Digite um ano para verificar se é bissexto: "))
# verifica_bissexto = ano % 4 == 0 and ano % 100 != 0
# verifica_bissexto_excecao = ano % 400 == 0

# if verifica_bissexto_excecao == True:
#    print(f"O ano {ano} é bissexto.")
# else:
#    if verifica_bissexto == True:
#       print(f"O ano {ano} é bissexto!")
#    else:
#       print(f"O ano {ano} não é bissexto.")

# CÓDIGO DO PROFESSOR
ano = int(input("Que ano quer analizar?"))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print(f"O ano {ano} É BISSEXTO.")
else:
   print(f"O ano {ano} NÃO É BISSEXTO.")