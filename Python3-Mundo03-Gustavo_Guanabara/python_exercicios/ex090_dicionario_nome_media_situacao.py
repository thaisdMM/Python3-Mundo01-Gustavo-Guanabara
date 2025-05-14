aluno = {}
aluno["Nome"] = input("Nome: ").strip().capitalize()
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))
if aluno["Média"] >= 7:
    aluno["Situacao"] = "Aprovado"
elif 5 <= aluno["Média"] < 7:
    aluno["Situacao"] = "Recuperação"
else:
    aluno["Situacao"] = "Reprovado"
print("=-" * 20)
for key, value in aluno.items():
    print(f"{key} é igual a {value}")
