sexo = "x"
while sexo != "M" or sexo != "F":
    sexo = input("Digite o sexo da pessoa [M] Masculino ou [F] Feminino ").strip().upper()
    if sexo == "M" or sexo == "F":
        print(f"O sexo digitado foi: {sexo}")
    else:
        print("Opção inválida. Tente novamente.")

print("\nFim do programa.")