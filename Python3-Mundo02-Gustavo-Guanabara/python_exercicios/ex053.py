# Crie um programa que laig uma frase qualquer a diga se ala é um polindromo.
# desconsiderando os aspaços.
# Ен:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

# # FIZ O PALÍNDROMO, MAS SEM O LAÇO FOR.
# print("VERIFICANDO SE É PALINDROMO")
# frase = input("Digite uma frase para verificarmos se ela é palindromo: ").strip().lower()
# frase_sem_espaços = frase.replace(" ", "" )
# print(frase)
# print(frase_sem_espaços)
# print(frase_sem_espaços[::-1])
# if frase_sem_espaços == frase_sem_espaços[::-1]:
#    print("PALINDROMO")

#PALINDROMO COM O LAÇO FOR
frase = input("Digite uma frase para verificar se a frase é PALÍNDROMO: ").strip().lower()
frase_sem_espaços = frase.replace(" ", "")
for i in range(len(frase_sem_espaços)):
   if frase_sem_espaços == frase_sem_espaços[::-1]:
      palindromo = "É PALÍNDROMO"
   else:
      palindromo = "NÃO É PALÍNDROMO"
print(palindromo)