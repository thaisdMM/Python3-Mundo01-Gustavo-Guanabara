alunos = []
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
    # contador += 1
    continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    while continuar not in "NS":
        print("Resposta inválida. Digite [S/N]")
        continuar = input("Quer continuar? [S/N] ").strip().upper()[0]
    if continuar == "N":
        break
# print(f"Dados: {dados}")
# print(f"alunos {alunos}")
print("=-" * 30)
print(f'{"Nº":<4} {"NOME":<15} {"MÉDIA":>6}')
print("-" * 40)

for posicao, dados_aluno in enumerate(alunos):
    # print(f"{posicao} {dados_aluno[0]} {dados_aluno[2]}")
    nome = dados_aluno[0][0]
    media = dados_aluno[2][0]
    print(f"{posicao:<4} {nome:<15} {media:<8.1f}")
print("-" * 40)

while True:
    mostrar_notas = int(input("Mostrar notas de qual aluno? [999 interrompe] "))
    if mostrar_notas == 999:
        break
    else:
        if mostrar_notas < 0 or mostrar_notas >= len(alunos):
            print("Número de aluno incorreto. Tente novamente.")
        else:
            print(
                f"As notas de {alunos[mostrar_notas][0][0]} são {alunos[mostrar_notas][1]}"
            )
            # for posicao, dados_aluno in enumerate(alunos):
            #     if mostrar_notas == posicao:
            #         print(f"As notas de {dados_aluno[0][0]} são {dados_aluno[1]}")

print("Programa de notas finalizado.")
