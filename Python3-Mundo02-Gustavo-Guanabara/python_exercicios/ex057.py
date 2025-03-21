sexo_invalido = True
while sexo_invalido == True:
    print(
        """Sexo da pessoa:
[M] Masculino
[F] Feminino"""
    )
    sexo = input("sexo = ").strip().upper()
    if sexo != "M" and sexo != "F":
        sexo_invalido = True
        print(f"\nOpção é inválida. Tente novamente!")
    else:
        sexo_invalido = False
if sexo == "M":
    print(f"\nO sexo digitado foi: {sexo}: MASCULINO")
else:
    print(f"\nO sexo digitado foi: {sexo}: FEMININO")
print("\nFim do programa.")
