# # testando no terminal

# >>> 5+3*2
# 11
# quadrado
# >>> 5**2
# 25
# cubo

# >>> 5**3
# 125
# divisao inteiro
# >>> 19//2
# 9
# >>> 19/2
# 9.5

# >>> 18%2
# 0
# >>> 122%3
# 2
# potencia
# >>> 4**3
# 64
# potencia
# >>> pow(4,3)
# 64

# raiz quadrada de um numero mesmo coisa que a potencia dele por meio
# >>> 81**(1/2)
# 9.0
# >>> 25**(1/2)
# 5.0

# raiz cubica
# >>> 127**(1/3)
# 5.026525695313479

# string
# >>> "oi" + "ola"
# 'oiola'
# >>> "oi"*5
# 'oioioioioi'
# >>> "="*20
# '===================='
# >>> print("="*20)
# ====================

nome = input("Qual é o seu nome?")
print(f"Prazer em te conhecer {nome:>20}!") #esse código vai alinhar a direita em 20 espaços

nome = input("Qual é o seu nome?")
print(f"Prazer em te conhecer {nome:<20}!") #esse código vai alinhar a esquerda em 20 espaços

nome = input("Qual o seu nome?")
print(f"Prazer em te conhecer {nome:^20}") #esse código vai alinhar no centro em 20 espaços
nome = input("Qual o seu nome?")
print(f"Prazer em te conhecer {nome:=^20}")

# RESPOSTA DO TERMINAL
# Qual é o seu nome?Thaís
# Prazer em te conhecer                Thaís!
# Qual é o seu nome?Medeiros
# Prazer em te conhecer Medeiros            !
# Qual o seu nome?Moreira
# Prazer em te conhecer       Moreira 
# Qual o seu nome?Thaís 
#Prazer em te conhecer =======Thaís======== 

n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# print(f"A soma vale {n1+n2}") pode colocar assim sem variável se nao for usar a informação para mais nada

# {:.3f}para escolher só 3 float 
# end=" " esse é para continuar o print na mesma linha
# \n quebra linha
print(f"Os valores digitados são {n1} e {n2}.\nA soma é {s}, a multiplicação é {m}, e a divisão é {d:.3f}", end=" ") 
print(f"A divisão inteira é {di} e a potência é {e}")