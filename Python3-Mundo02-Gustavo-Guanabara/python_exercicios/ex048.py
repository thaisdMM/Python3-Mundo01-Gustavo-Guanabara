print("NÚMEROS IMPARES MULTIPLOS DE 3 DE 1 A 500: \n")

soma = 0
for i in range(1,501):
   if i % 2 == 1 and i % 3 == 0:
      print(i)
      soma += i
print(f"\nA soma dos números ímpares multiplos de 3 de 1 a 500 é = {soma}")