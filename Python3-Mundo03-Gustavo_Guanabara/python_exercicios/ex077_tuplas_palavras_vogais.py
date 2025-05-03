palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)
for i in palavras:
    print(f"Na palavra: {(i).upper()}", end="")
    # contador += 1
    # print(contador)
    # if contador == 1:
    vogais = ""
    total_vogais = 0
    for letter in i:
        if letter in "aeiou":
            vogais += letter
            total_vogais += 1
    print(f" temos {total_vogais} vogais que são: {vogais}")

# correção professor nao usou uma variavel para guardar as vogais, exibiu elas diretamente

for i in palavras:
    print(f"\nNa palavras {i.upper()} temos ", end="")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
