from random import sample, shuffle

# sample(lista, k): Retorna uma nova lista aleatória com k elementos da lista original, sem modificá-la.
alunos_apresentação = ["Thaís", "Carol", "Guilherme", "André"]
print(f"Os alunos são: {alunos_apresentação}") 
print(f"A ordem de apresentação dos trabalhos é: {sample(alunos_apresentação, k=len(alunos_apresentação))}")

#também dá para fazer shuffle:
#> shuffle(lista): Embaralha a própria lista e retorna None. Por isso tem que chamar a lista sem o shoffle para ver o resultado

alunos_apresentação2 = ["Daniel", "Rafael", "Mariana", "Miguel"]
print(f"\nOs alunos que apresentaram o trabalho hoje são: {alunos_apresentação2}")

shuffle(alunos_apresentação2) # Modifica a lista original
print(f"A ordem de apresentação é: {alunos_apresentação2}")
