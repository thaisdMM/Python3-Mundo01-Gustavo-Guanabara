frase = "Curso em Vídeo Python"
print(frase)
# Fatiamento
print(frase[3])
print(frase[3:13]) #no fatiamento nao conta a ultima
print(frase[:13])
print(frase[9:])
print(frase[1:15:2]) #pulando de 2 em 2
print(frase[::2]) #: nao sabe o início : nao sabe o final 2 pula de 2 em 2

print("Oi")

# # Usando """ para textos grandes
# print("""Start where you are. Use what you have. Do what you can. We are what we repeatedly do. All progress takes place outside the comfort zone. If your dreams don't scare you, they are not big enough.The future belongs to those who believe in the beauty of their dreams.""")

print(frase.count("o"))
print(frase.count("O")) # minúsculo e maiúsculo são diferentes

#Contanto a quantidade de O maiúsculo na frase que foi jogada para maíusculo com o uper
print(frase.upper())
print(frase.upper().count("O"))

# len > tamanho
print(len(frase))
frase = "    Curso em Vídeo Python   " # aumentou o tamanho, pois conta os espaços
print(len(frase))
print(len(frase.strip())) # strip remove espaços no início e no final

frase = "Curso em Vídeo Python"
print(len(frase))
print(frase.replace("Python", "Androide")) 
frase.replace("Python", "Androide")
print(frase)

#REPLACE muda só nesse codigo, para mudar efetivamente, teria que fazer frase receber esse código
frase = frase.replace("Python", "Androide")
print(frase)
print(len(frase))

# Verificar se a palava curso está em frase
frase = "Curso em Vídeo Python"
print("Curso" in frase)
print(frase.find("Curso"))
print(frase.find("Vídeo"))
print(frase.find("vídeo")) # respota é -1 e a string começa com 0 o que é falso, deu falso por causa do v minúsculo
print(frase.lower())
print(frase.lower().find("vídeo")) # transformou primeiro pra minúsculo e depois sim achou

# split> separou cada frase e criou uma lista
print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0]) # como divido é uma lista, vc pode mostrar os itens da lista
print(dividido[3])
print(dividido[2][3]) # pega dividido 2[Vídeo] e mostra a letra[3] da lista, contando do 0