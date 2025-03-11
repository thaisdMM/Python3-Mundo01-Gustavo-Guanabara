# Escrava um programa que laia a velocidade de um carro.
# Se cie ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
# A multa vai custar
# R$7.00 por cada Km acima do limita.

velocidade_carro = int(input("Digite a velocidade do carro: "))
multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
   print(f"Sua velocidade é {velocidade_carro}Km/h e você foi multado!")
   print(f"O valor da multa é: R${multa:.2f}")
else:
   print(f"Sua velocidade {velocidade_carro}Km/ foi e você está dentro do limite da velocidade.")