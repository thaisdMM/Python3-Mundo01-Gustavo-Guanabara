# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

print("\nCalculando a média de notas.")
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2
# print(media)
if media >= 7:
    print(f"\nAPROVADO!!! Suas notas foram {nota1} e {nota2} e a méda foi: {media:.2f}.")
elif media >= 5:
    print(f"\nRECUPERAÇÃO. Suas notas foram {nota1} e {nota2} e a média foi: {media:.2f}")
else:
    print(f"\nREPROVADO. Suas notas foram {nota1} e {nota2} e a média foi {media}")
