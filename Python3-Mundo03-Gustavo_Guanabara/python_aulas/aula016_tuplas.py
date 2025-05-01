lanche = "Hambúrguer"
print(lanche)
lanche = "Hambúrguer"
lanche = "Suco"
print(lanche)

# TUPLAS SÃO IMUTÁVEIS

# tupla é entre parenteses, apesar de nao ser mais obrigatorio
# também é uma tupla, depois do python 3.5 não precisa do parênteses
lanche2 = "Hambúrguer", "Suco", "Pizza", "Pudim"
print(lanche2)
print(type(lanche2))


lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche)
print(type(lanche))
print(lanche[1])
print(lanche[3])  # lembrar que ignora o ultimo elemento
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])

# tuplas são imutáveis
# #esse codigo dá erro, pois tenta mudar a tupla:

# lanche[1] = "Refrigerante"
# print(lanche[1])
# # TypeError: 'tuple' object does not support item assignment

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche)
# com esse for vai printar cada comida na frase "Eu vou comer {comida}"
# observe abaixo que os dois for dão o mesmo ressultado - tem momentos que só uma delas irá funcionar

for comida in lanche:
    print(f"Eu vou comer {comida}")
print("Comi muito usando o for sem contador!")

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(len(lanche))  # vai dar que tem 4 comidas

# Quando o programa não está em execução pode mexer na tupla:
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(len(lanche))  # agora vai dar que tem 5 comidas
for contador in range(0, len(lanche)):
    # print(contador) # vai aparecer só os numeros(0,1,2,3,4)
    # print(lanche[contador])
    # print(f"Eu vou comer {lanche[contador]}")
    # nesse for dá para mostrar a posição do item da tupla
    print(f"Eu vou comer{lanche[contador]} na posição {contador}")
print("Comi demais usando o range(len)!")

# ENUMERATE - Dá tanto o dado quanto a posição

lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
for posicao, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} e na posição {posicao}")
print("Comi muito usando ENUMERATE.")

# SORTED - mostra em ordem
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim", "Batata Frita")
print(
    sorted(lanche)
)  # não altera a tupla, apenas coloca em ordem, abaixo ela é impressa normal
print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a  # diferente de c
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(5))  # quantas vezes aparece 5 em c
print(c.count(4))
print(c.count(9))  # aparece 0 pois nao tem 9 em c
print(c)
print(c.index(8))  # em que posição está o 8
print(c.index(4))
# aparece a primeira posição que encontra o número, mesmo tendo ele mais de uma vez
print(c.index(2))
# o segundo número é para escolher(deslocamento) a partir de qual posição quer encontrar o número 2, coloquei 1 pq o primeiro aparece na posição 0
print(c.index(2, 1))

# PODE ter dados de tipos diferentes na tupla
pessoa = ("Gustavo", 39, "M", 99.88)
print(pessoa)
# existe uma forma de "MUDAR A TUPLA": APAGANDO ELA TODA,
#  não dá  para apagar apenas um elemento
del pessoa[0]
# TypeError: 'tuple' object doesn't support item deletion
del pessoa
# print(pessoa)
# # NameError: name 'pessoa' is not defined
# # erro acima porque pessoa já foi apagada
