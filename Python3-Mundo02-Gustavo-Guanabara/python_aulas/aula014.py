# FOR - Sabe o limite

for i in range(1,10):
    print(i)
print("Fim do programa.")

# WHILE - sabe o limite e não sabe o limite

i = 1
while i < 10:
    print(i)
    i += 1
print("FIM")

for i in range(1, 5):
    n = int(input("Digite um valor: "))
print("FIM")

n = 1 # se nao começar o n dá erro: name 'n' is not defined
while n != 0:
    n = int(input("Digite um valor: "))
print("0 = Fim do programa.")

r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = input("Quer continuar? [S/N]").strip().upper()
print("Fim")

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    # para não contar o 0 como par
    if n != 0:
        if n % 2 == 0:
            par +=1
        else:
            impar += 1
print(f"Numeros pares: {par}")
print(f"Números ímpares: {impar}")
print("Acabou")