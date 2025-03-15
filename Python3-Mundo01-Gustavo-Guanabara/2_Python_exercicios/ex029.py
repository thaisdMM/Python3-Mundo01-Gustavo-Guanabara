# Escreva um programa que leia a velocidade de um carro.
# Se velocidade ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

velocidade_carro = float(input("Digite a velocidade do carro: "))
multa = (velocidade_carro - 80) * 7
if velocidade_carro > 80:
   print(f"Sua velocidade é {velocidade_carro}Km/h. O máximo permitito é 80Km/h e você foi multado!")
   print(f"O valor da multa é: R${multa:.2f}")
print("Tenha um bom dia, dirija com segurança!") #essa parte do código sempre executa
# Eu coloquei o else, mas o prof nao colocou, eu sabia que nao precisava, mas quis ser mais completa
# else:
#    print(f"Sua velocidade é {velocidade_carro}Km/ e você está dentro do limite da velocidade.")