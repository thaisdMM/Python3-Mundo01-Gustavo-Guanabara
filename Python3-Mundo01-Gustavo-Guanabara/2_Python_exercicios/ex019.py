#import random

from random import choice

# alunos = ["Maria", "José", "Madalena", "Pedro"]
# print(f"Os possíveis alunos para apagar o quadro são {alunos}")
# print(f"O aluno escolhido é: {random.choice(alunos)}")

aluno1 = input("Digite o nome do 1° aluno: ")
aluno2 = input("Digite o nome do 2° aluno: ")
aluno3 = input("Digite o nome do 3 aluno: ")
aluno4 = input("Digite o nome do 4 aluno: ")
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
print(f"O aluno escolhido para apagar o quadro é: {choice(lista_alunos)}")