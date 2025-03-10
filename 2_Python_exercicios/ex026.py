frase = input("Digite uma frase: ")
print(f"Na frase {frase} a letra 'a' minúscula aparece: {frase.count('a')}")
print(f"Na frase {frase} a letra 'A' maiúscula aparece: {frase.count('A')}")
print(f"Na frase {frase} o total de letra a é: {frase.upper().count('A')}")
print(f"Na frase {frase} a letra 'a' aparece pela primeira vez: {frase.lower().find('a')}")
print(f"Na frase {frase} a letra 'a' aparece pela última vez: {frase[0:].lower().find('a')}")# preciso conferir essa parte