aluno = {}
aluno["Nome"] = input("Nome: ").strip().capitalize()
aluno["Média"] = float(input("Média: "))
if aluno["Média"] >= 6:
    aluno["Situacao"] = "Aprovado"
else:
    aluno["Situacao"] = "Reprovado"
for key, value in aluno.items():
    print(f"{key} é igual a {value}")
