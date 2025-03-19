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

# PALINDROMO COM O LAÇO FOR melhorando eficiência, palindromo como espelho, verificar até a metadade já é o suficiente
frase = input(
    "Digite uma frase para verificar se a frase é PALÍNDROMO: ").strip().lower()
frase_sem_espaços = frase.replace(" ", "")
metade_frase = len(frase_sem_espaços) // 2
palindromo = True
for i in range(0, metade_frase):
    if frase_sem_espaços[i] != frase_sem_espaços[-i-1]:
        palindromo = False
if palindromo:
    print(f"\nA frase: {frase} É PALÍNDROMO.")
else:
    print(f"\nA frase: {frase} NÃO É PALÍNDROMO")
print("\nPrograma finalizado.")
