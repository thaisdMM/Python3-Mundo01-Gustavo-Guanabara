# Para declarar um dicionário usa chaves {}
pessoas = {"nome": "Thaís", "sexo": "F", "idade": 30}
print(f"Dicionario pessoas: {pessoas}")
# print(f"Erro se pessoas[0] {pessoas[0]}")
# KeyError: 0
# Para referenciar um elemento do dicionário usa colchetes []
print(f"Pessoas['nome']: {pessoas['nome']}")
print(f"pessoas['idade']: {pessoas['idade']}")
print(f"A {pessoas['nome']} tem {pessoas['idade']} anos")
print(f"pessoas.keys(): {pessoas.keys()}")
print(f"pessoas.values(): {pessoas.values()}")
print(f"pessoas.items(): {pessoas.items()}")
# a resposta do terminal desse comando é uma lista de tuplas dentro:
# pessoas.items(): dict_items([('nome', 'Thaís'), ('sexo', 'F'), ('idade', 30)])
for key in pessoas.keys():
    print(f"printa cada chave. key: {key}")
for values in pessoas.values():
    print(f"printa cada valor do dicionário. values: {values}")
# o codigo abaixo é como se fosse o enumerates. Como não tem enumerates, usa o items()
for key, values in pessoas.items():
    print(f"{key} = {values}")
# del APAGA 
del pessoas["sexo"]
for key, values in pessoas.items():
    print(f"{key} = {values}")
# trocar um valor:
pessoas["nome"] = "Carol"
print(f"pessoas {pessoas}")
# adicionando uma chave e valor não precisa de "append"
pessoas["sexo"] = "F"
pessoas["peso"] = 62.5
print(f"pessoas {pessoas}")

# RESPOSTA DO TERMINAL
# Dicionario pessoas: {'nome': 'Thaís', 'sexo': 'F', 'idade': 30}
# Pessoas['nome']: Thaís
# pessoas['idade']: 30
# A Thaís tem 30 anos
# pessoas.keys(): dict_keys(['nome', 'sexo', 'idade'])
# pessoas.values(): dict_values(['Thaís', 'F', 30])
# pessoas.items(): dict_items([('nome', 'Thaís'), ('sexo', 'F'), ('idade', 30)])
# # printa cada chave. key: nome
# # printa cada chave. key: sexo
# # printa cada chave. key: idade
# # printa cada valor do dicionário. values: Thaís
# # printa cada valor do dicionário. values: F
# # printa cada valor do dicionário. values: 30
# nome = Thaís
# sexo = F
# idade = 30
# nome = Thaís
# idade = 30
# pessoas {'nome': 'Carol', 'idade': 30}
# pessoas {'nome': 'Carol', 'idade': 30, 'sexo': 'F', 'peso': 62.5}

## Criando um dicionário dentro de uma lista:

brasil = []
estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil.append(estado1)
brasil.append(estado2)

print(f"dicionario: estado1 {estado1}")
print(f"dicionário: estado2 {estado2}")
print(f"lista: brasil {brasil}")
# # criou uma lista com 2 dicionários:
## lista: brasil [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
print(f"brasil[0]: {brasil[0]}")
print(f"brasil[1]: {brasil[1]}")
print(f"brasil[0]['uf']: {brasil[0]['uf']}")
print(f"brasil[1]['sigla']: {brasil[1]['sigla']}")

# # RESPOSTA DO TERMINAL
# # dicionario: estado1 {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# # dicionário: estado2 {'uf': 'São Paulo', 'sigla': 'SP'}
# # lista: brasil [{'uf': 'Rio de Janeiro', 'sigla': 'RJ'}, {'uf': 'São Paulo', 'sigla': 'SP'}]
# # brasil[0]: {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# # brasil[1]: {'uf': 'São Paulo', 'sigla': 'SP'}
# # brasil[0]['uf']: Rio de Janeiro
# # brasil[1]['sigla']: SP

# LENDO DADOS COM INPUT

## O código abaixo apresenta PROBLEMAS
estado = dict()
brasil = list()
for i in range(0,3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do Estado: ")
    brasil.append(estado)
print(brasil)
# [{'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}, {'uf': 'Acre', 'sigla': 'AC'}]

## Na lista tinha que fazer a cópia[:], mas no dicionário não dá PARA FAZER FATIAMENTO
estado = dict()
brasil = list()
for i in range(0,3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do Estado: ")
    brasil.append(estado[:])
print(brasil)
# brasil.append(estado[:]
# TypeError: unhashable type: 'slice'

# MÉTODO copy() - para resolver o problema do fatiamento

estado = dict()
brasil = list()
for i in range(0,3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
print(brasil)
# AGORA DEU CERTO
# [{'uf': 'Minas Gerais', 'sigla': 'MG'}, {'uf': 'Acre', 'sigla': 'Ac'}, {'uf': 'Goias', 'sigla': 'GO'}]

estado = dict()
brasil = list()
for i in range(0,3):
    estado["uf"] = input("Unidade Federativa: ")
    estado["sigla"] = input("Sigla do Estado: ")
    brasil.append(estado.copy())
O primeiro for é da lista, o segundo será do dicionário    
for estado in brasil:
    #print(f"estado {estado}")
    for key, value in estado.items():
        print(f"O campo {key} tem o valor {value}")
## TERMINAL:
# O campo uf tem o valor Rio de Janeiro
# O campo sigla tem o valor RJ
# O campo uf tem o valor São Paulo
# O campo sigla tem o valor SP
# O campo uf tem o valor Goias
# O campo sigla tem o valor GO

for estado in brasil:
    for value in estado.values():
        print(f"{value}", end=" ")
    print()
# ACRE AC 
# PARA PA 
# GOIAS GO 
