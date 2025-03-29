# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo_invalido = True
while sexo_invalido:
    print(
        """Sexo da pessoa:
[M] Masculino
[F] Feminino"""
    )
    sexo = input("sexo = ").strip().upper()
    if sexo != "M" and sexo != "F":
        print(f"\nOpção é inválida. Tente novamente!")
    else:
        sexo_invalido = False
if sexo == "M":
    print(f"\nO sexo digitado foi: {sexo}: MASCULINO")
else:
    print(f"\nO sexo digitado foi: {sexo}: FEMININO")
print("\nFim do programa.")

# CORREÇÃO PROFESSOR

# [0] só para pegar primeira letra
sexo = input("Informe seu sexo: [M/F] ").strip().upper()[0]
# print(sexo)
while sexo not in "MmFf":
    sexo = input("Dados inválidos. Por favor, informe seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")
