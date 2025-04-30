print("=" * 30)
print("{:^30}".format("BANCO MOREIRA"))
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$"))
total = valor
cedula_atual = 50
total_cedulas = 0
while True:
    if total >= cedula_atual:
        total -= cedula_atual
        total_cedulas += 1
    else:
        # aqui nao escreve as cedulas que sao 0
        if total_cedulas > 0:
            print(f"Total de {total_cedulas} de R${cedula_atual}")
        if cedula_atual == 50:
            cedula_atual = 20
        elif cedula_atual == 20:
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        total_cedulas = 0
        if total == 0:
            break
print("=" * 30)
print("Volte sempre ao BANCO MOREIRA! Tenha um bom dia!")
