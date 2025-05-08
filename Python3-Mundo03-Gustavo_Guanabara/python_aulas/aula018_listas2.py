teste = list()
teste.append("Thais")
teste.append(30)
galera = list()
# galera.append(teste)> nesse caso fez uma ligação entre as duas listas
galera.append(teste)
print(f"Lista teste: {teste}")
print(f"Lista galera tem lista(teste) dentro de lista {galera}")
teste[0] = "Maria"
teste[1] = "22"
# galera.append(teste)> nesse caso fez uma ligação entre as duas listas
galera.append(teste)
print(f"Lista teste: {teste}")
print(f"Lista galera tem lista(teste) dentro de lista(galera) {galera}")

# RESULTADO DO TERMINAL:
# Lista teste: ['Thais', 30]
# Lista galera tem lista(teste) dentro de lista [['Thais', 30]]
# Lista teste: ['Maria', '22']
# Lista galera tem lista(teste) dentro de lista(galera) [['Maria', '22'], ['Maria', '22']]

galera.append(teste[:])> #Agora é diferente faz uma cópia da lista teste
teste = list()
teste.append("Thais")
teste.append(30)
galera = list()

galera.append(teste[:]) # copia
print(f"Lista teste: {teste}")
print(f"Lista galera tem lista(teste) dentro de lista {galera}")
teste[0] = "Maria"
teste[1] = "22"
galera.append(teste[:]) # copia
print(f"Lista teste: {teste}")
print(f"Lista galera tem lista(teste) dentro de lista(galera) {galera}")

# # RESULTADO DO TERMINAL:
# Lista teste: ['Thais', 30]
# Lista galera tem lista(teste) dentro de lista [['Thais', 30]]
# Lista teste: ['Maria', '22']
# Lista galera tem lista(teste) dentro de lista(galera) [['Thais', 30], ['Maria', '22']]

galera2 = [["João", 19], ["Ana", 33], ["Joaquim", 13], ["Maria", 45]]
# print(f"\ngalera2[0]: {galera2[0]}")
# print(f"galera2[0][0] {galera2[0][0]}")
# print(f"galera2[2][1] {galera2[2][1]}")
# print(f"galera2[2] {galera2[2]}")

for p in galera2:
    print(f"Printa toda a lista {p}")

for p in galera2:
    print(f"Printa apenas o elemento 0, que são os nomes {p[0]}")

for p in galera2:
    print(f"Print dos dados do elemento [1] {p[1]}")
for p in galera2:
    print(f"{p[0]} tem {p[1]} anos de idade.")

# No codigo abaixo deu append na lista dados sem ser cópia[:] a resposta do terminal é lista vazia

galera3 = list()
dado = list()
for c in range(0,3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera3.append(dado)
    dado.clear() # excluir dado
print(f"dado: {dado}")
print(f"galera3: {galera3}")

# # RESPOSTA DO TERMINAL
# dado: []
# galera3: [[], [], []]

galera3 = list()
dado = list()
total_maior_idade = total_menor_idade = 0 # Pode fazer com variavél simples, não composta
for c in range(0,3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera3.append(dado[:]) # cópia de dados
    dado.clear() # excluir dado
print(f"dado: {dado}")
print(f"galera3: {galera3}")

# # RESPOSTA DO TERMINAL:
# Nome: Pedro   
# Idade: 22
# Nome: Maria
# Idade: 33
# Nome: Claudia
# Idade: 55
# dado: []
# galera3: [['Pedro', '22'], ['Maria', '33'], ['Claudia', '55']]

for p in galera3:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        total_maior_idade += 1
    else:
        print(f"{p[0]} é menor de idade.")
        total_menor_idade += 1
print(f"Temos {total_maior_idade} maiores e {total_menor_idade} menores de idade.")
