# #ESTÁ CORRETO, MAS ABAIXO TEM UMA OPÇAO QUE GASTA MENOS MEMÓRIA, POIS ITERA DE 2 EM 2
# print("Números PARES entre 1 e 50:")
# for i in range(1, 51):
#     if i % 2 == 0:
#         #print(".") # aqui mosta a iteraçao de 1 em 1, desnecessária
#         print(i)
# print("Fim do programa.")

for i in range(2, 51, 2):
   print(f"{i}", end=", ")
print("Fim do programa.")
