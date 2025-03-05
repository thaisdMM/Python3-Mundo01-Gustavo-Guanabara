# salário funcionário, novo salário com 15% aumento - porcentagem pode ser salario*15/100

salário = float(input("Digite o valor do seu salário R$: "))
print(f"O seu salário atual é:R$ {salário:.2f} e terá um aumento de 15% passando a ser R$: {salário + (salário * 0.15):.2f}")