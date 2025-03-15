#Cria um programa que leia duas notas de um aluno e calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0:
# REPROVADO
# - Média entre 5.0 a 6.9:
# RECUPERAÇÃO
# - Média 7.0 ou suparior: aprovado
print("Calculando a média de notas.")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
#print(media)
if media >= 7:
   print(f"APROVADO!!! Sua méda foi: {media:.2f}.")
elif media >= 5:
   print(f"RECUPERAÇÃO. Sua média foi: {media:.2f}")
else:
   print(f"REPROVADO. Sua média foi {media}")