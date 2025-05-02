estilo = "-=-"
times_serie_b = (
    "Avaí",
    "Cuiabá",
    "Vila Nova",
    "Coritiba",
    "Goiás",
    "CRB",
    "Athletico-PR",
    "América-MG",
    "Remo",
    "Novorizontino",
    "Chapecoense",
    "Ferroviária",
    "Atlético Goianiense",
    "Criciúma",
    "Operário-PR",
    "Athletic Club",
    "Botafogo-SP",
    "Paysandu",
    "Amazonas",
    "Volta Redonda",
)

print(estilo * 20)
print(
    f"""Lista de times do Brasileirão serie B 2025: 

{times_serie_b}"""
)
print(estilo * 20)
print(f"\nO 5 primeiros colocados são: {times_serie_b[:5]}")
print(estilo * 20)
print(f"\nOs 4 últimos colocados são: {times_serie_b[-4:]}")
print(estilo * 20)
chapecoense = 0
for contador in range(0, len(times_serie_b)):
    if times_serie_b[contador] == "Chapecoense":
        chapecoense = contador + 1
print(f"\nO time da Chapecoense está na {chapecoense}ª classificação.")
print(estilo * 20)
