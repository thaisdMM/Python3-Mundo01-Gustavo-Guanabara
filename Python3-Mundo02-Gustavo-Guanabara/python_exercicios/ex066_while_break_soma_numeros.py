contador = soma = 0
while True:
    numero = int(input("Digite um valor ou 999 para parar o programa: "))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f"Foram digitados {contador} numeros e a soma entre eles foi: {soma}")
