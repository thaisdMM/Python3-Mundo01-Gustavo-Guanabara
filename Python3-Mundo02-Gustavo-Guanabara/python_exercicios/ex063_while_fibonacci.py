# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

numero_termos_fibonacci = int(input("Quantos termos terão a sequencia fibonacci? "))
primeiro_termo = 0
segundo_termo = 1
contador_termos = 0
novos_termos = 0

while numero_termos_fibonacci > 0:
    print(f"Primeiro termo: {primeiro_termo}")
    print(f"Segundo termo: {segundo_termo}")
    novos_termos = primeiro_termo, segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = primeiro_termo + segundo_termo
    
    print(f"Novos termos: {novos_termos}")
    contador_termos += 1
    numero_termos_fibonacci -= 1
print(contador_termos)