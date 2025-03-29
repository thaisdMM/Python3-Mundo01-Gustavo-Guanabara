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
terceiro_termo = primeiro_termo + segundo_termo
print(f"→ {terceiro_termo}", end="")

# numero_termos_fibonacci = int(input("Quantos termos terão a sequencia fibonacci? "))
# primeiro_termo = 0
# segundo_termo = 1
# contador_termos = 0
# novos_termos = 0
# sequencia_fibonacci = primeiro_termo, segundo_termo

# while numero_termos_fibonacci > 0:
#     print(f"Primeiro termo: {primeiro_termo}")
#     numero_termos_fibonacci -= 1
#     print(f"\nSegundo termo: {segundo_termo}")
#     numero_termos_fibonacci -=1
# #    print(f"\nSequência fibonacci: {sequencia_fibonacci}", end="")
#     #novos_termos = primeiro_termo, segundo_termo
    
#     novo_primeiro_termo = segundo_termo

# #    numero_termos_fibonacci -= 1
#     novo_segundo_termo = primeiro_termo + segundo_termo

# #    numero_termos_fibonacci -= 1
#     sequencia_fibonacci = primeiro_termo, segundo_termo
    
#     #print(f"Novos termos: {novos_termos}")
#     contador_termos += 1
#     numero_termos_fibonacci -= 1
# print(contador_termos)