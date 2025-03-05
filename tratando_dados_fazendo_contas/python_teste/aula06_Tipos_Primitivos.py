#Aqui o código é como se fosse uma string e concatena um número com outro
# n1= input('Digite um número: ')
# n2= input('Digite mais um número: ')
# print(type(n1))
# print(type(n2))
# soma= n1 + n2
# print('A soma vale', soma)

#Agora vamos resolver esse problema com os tipos primitivos convertendo para int

n1= int (input('Digite um número: '))
n2= int (input('Digite outro número: '))
print(type(n1))
print(type(n2))
s = n1 + n2
print('A soma entre {} e {} é: {}'.format(n1, n2, s))

# tipos
int= 7, -4, 0, 9875
float = 4.5, 0.076, -15.223, 7.0
bool = True, False
str = 'nome', 'Olá', '7.5', ''

#forma diferente de escrever o print

print(('A soma vale {}'.format(s)))
