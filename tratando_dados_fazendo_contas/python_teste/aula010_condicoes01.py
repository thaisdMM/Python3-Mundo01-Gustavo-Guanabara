# estrutura condicional composta if/else; simples só if

# nome = input("Qual é o seu nome? ")
# if nome == "Thaís":
#    print("Que nome lindo você tem!")
# else:
#    print("Que nome normal você tem.")
# print(f"Bom dia, {nome}!")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
print(f"A sua média foi: {media:.1f}")
if media >= 6:
   print("Sua média foi boa, parabéns!")
else:
   print("Sua média foi ruim, estude mais!")

#o mesmo comando, mas simplificado(condição simplificada):
print("PARABÉNS!" if media >= 6 else "Estude mais" )