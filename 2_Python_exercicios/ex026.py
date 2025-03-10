frase = input("Digite uma frase: ").strip()
print(f"Na frase {frase} a letra 'a' minúscula aparece: {frase.count('a')}")
print(f"Na frase {frase} a letra 'A' maiúscula aparece: {frase.count('A')}")
print(f"Na frase {frase} o total de letra a é: {frase.upper().count('A')}")
print(f"Na frase {frase} a letra 'a' aparece pela primeira vez: {frase.lower().find('a') +1}") # pq começa do 0
print(f"Na frase {frase} a letra 'a' aparece pela última vez: {frase.lower().rfind('a') +1}")# preciso conferir essa parte