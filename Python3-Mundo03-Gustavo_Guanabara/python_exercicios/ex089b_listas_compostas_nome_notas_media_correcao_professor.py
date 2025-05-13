alunos = []
while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = input("Quer continuar? [S/N]").strip().upper()[0]
    if continuar in "N":
        break
print("=-" * 30)
print(f"{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}")
print("-" * 30)
for posicao, valor in enumerate(alunos):
    print(f"{posicao:<4}{valor[0]:<10}{valor[2]:>8.1f}")
while True:
    print("-" * 35)
    mostrar_notas = int(input("Mostar notas de qual aluno? (999 interrompe) "))
    if mostrar_notas == 999:
        print("FINALIZANDO...")
        break
    if mostrar_notas <= len(alunos) - 1:
        print(f"Notas de {alunos[mostrar_notas][0]} são {alunos[mostrar_notas][1]}")
print("<<< VOLTE SEMPRE >>>")
