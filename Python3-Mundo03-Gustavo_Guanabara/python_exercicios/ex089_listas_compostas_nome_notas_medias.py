alunos = []
# dados = [[], [], []]
contador = 0

while True:
    dados = [[], [], []]
    dados[0].append(input("Nome: ").strip())
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    dados[1].append(nota1)
    dados[1].append(nota2)
    dados[2].append(media)
    alunos.append(dados[:])
    dados.clear()
    contador += 1
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if continuar == "N":
        break
    print(f"contador {contador}")
print(f"Dados: {dados}")
print(f"alunos {alunos}")
print("=-" * 40)
print(f'{"Nº":<4} {"NOME":<15} {"MÉDIA":>6}')
print("-" * 40)

for posicao, dados_aluno in enumerate(alunos):
    # print(f"{posicao} {dados_aluno[0]} {dados_aluno[2]}")
    nome = dados_aluno[0][0]
    media = dados_aluno[2][0]
    print(f"{posicao:<4} {nome:<15} {media:<8}")
print("-" * 40)