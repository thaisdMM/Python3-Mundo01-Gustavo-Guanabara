# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# FIZ O PALÍNDROMO, MAS SEM O LAÇO FOR.

print("VERIFICANDO SE É PALINDROMO")
frase = input(
    "Digite uma frase para verificarmos se ela é palindromo: ").strip().lower()
frase_sem_espaços = frase.replace(" ", "")
# print(frase)
# print(frase_sem_espaços)
# print(frase_sem_espaços[::-1])
if frase_sem_espaços == frase_sem_espaços[::-1]:
    print("PALINDROMO")

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

# CORREÇÃO PROFESSOR

frase = input("Digite uma frase: ").strip().upper()
palavras_frase = frase.split()
palavras_sem_espaco = "".join(palavras_frase)  # junta tudo sem espaço
# print(f"Você digitou a frase {frase}")
# print(palavras_frase)
# print(palavras_sem_espaco)
inverso = ""
# for começa da ultima letra da palavra_sem_espaco -1 > se len()=20 tem 19 letras, por isso o -1
#  vai ate a a ultima letra: -1(é a 0, mas o desconsidera a ultima) , pula de -1 em -1
for letra in range(len(palavras_sem_espaco) - 1, -1, -1):
    # print(palavras_sem_espaco[letra])
    inverso += palavras_sem_espaco[letra]
# print(palavras_sem_espaco, inverso)

# # No código do professor ele tira o for e faz o que eu tinha feito no código sem for:
# inverso = palavras_sem_espaco[::-1]

print(f"O inverso de {palavras_sem_espaco} é: {inverso}")
if inverso == palavras_sem_espaco:
    print("Temos um PALÍNDROMO!")
else:
    print("Não temos PALÍNDROMO.")
