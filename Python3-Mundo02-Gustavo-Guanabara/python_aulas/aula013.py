# Faz o laço 5 vezes, pois nao considera o ultimo número
for i in range(1,6):
   print("Oi")
print("FIM.")

# aqui faz 6
for i in range(0,6):
   print("Olá")
   print("Fim.") # se o fim ficar na identação também entra na repetição for

# printa o contador i de 0 a 5
for i in range(0, 6):
   print(i)
print("FIM")

for i in range(1, 7):
   print(i)
print("Finalizou")

# contar de trás pra frente - o final do laço é a iteração, no caso abaixo vai tirando 1 (-1)
for i in range(6, 0, -1):
   print(i)

# Iteração contanto de 2 em 2
for i in range(0, 7, 2):
   print(i)
print("FIM")

# Lendo um valor e usando no for
# esse código conta até antes do número digitado
numero = int(input("Digite um número: "))
for i in range (0, numero):
   print(i)
print("Fim")

# esse código com o numero + 1 conta até o número digitado
numero = int(input("Digite um número: "))
for i in range (0, numero +1):
   print(i)
print("Fim")

# você digita o inicio da contage, o fim e quantos passos ele dá
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for i in range(inicio, fim + 1, passo):
   print(i)
print("FIM")

# Fica repetindo a identação pela contagem do range
for i in range(0,3):
   numero = int(input("Digite um valor: "))
print("FIM")

# somando os valores digitados
soma = 0
for i in range(0,4):
   numero = int(input("Digite um valor: "))
   soma += numero # mesmo que soma = soma + numero
print(f"O somatório de todos os valores foi {soma}")