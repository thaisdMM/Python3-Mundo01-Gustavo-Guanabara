alunos = []
dados = [[], [], []]



dados[0].append(input("Nome: ").strip())
nota1 = (float(input("Nota 1: ")))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2) / 2
dados[1].append(nota1)
dados[1].append(nota2)
dados[2].append(media)
# dados[1].append(float(input("Nota 1: ")))
# dados[1].append(float(input("Nota 2:")))

print(f"Dados: {dados}")