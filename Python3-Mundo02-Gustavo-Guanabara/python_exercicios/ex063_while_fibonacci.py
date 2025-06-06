# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# CORREÇÃO PROFESSOR

print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)
numero_termos_fibonacci = int(input("Quantos termos você quer mostrar? "))
primeiro_termo = 0
segundo_termo = 1
print("~" * 30)
print(f"{primeiro_termo} → {segundo_termo}", end="")
contador_termos = 3  # começa do 3 pois, já tem 1° e 2° termo definidos
while contador_termos <= numero_termos_fibonacci:
    terceiro_termo = primeiro_termo + segundo_termo
    print(f" → {terceiro_termo}", end="")
    primeiro_termo = segundo_termo
    segundo_termo = terceiro_termo
    contador_termos += 1
print(" → FIM")
print("~" * 30)


# OUTRA FORMA DE FAZER:

numero_termos_fibonacci = int(input("Quantos termos terão a sequência Fibonacci? "))

primeiro_termo = 0
segundo_termo = 1
contador_termos = 0

while contador_termos < numero_termos_fibonacci:
    print(primeiro_termo, end=" ")  # Mostra o termo atual da sequência

    proximo_termo = (
        primeiro_termo + segundo_termo
    )  # Calcula o próximo termo da sequência
    primeiro_termo = segundo_termo  # Atualiza o primeiro termo
    segundo_termo = proximo_termo  # Atualiza o segundo termo

    contador_termos += 1  # Conta mais um termo gerado
