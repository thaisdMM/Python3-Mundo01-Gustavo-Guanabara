# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva(‘Olá, Mundo!’)
# Saída: Olá, Mundo!


def escreva(txt):
    tamanho = len(txt) + 4
    print("~" * tamanho)
    print(f"  {txt}")  # deu 2 espaços para centralizar já que adiciou +4
    print("~" * tamanho)


escreva("Thaís Moreira")
escreva("criou uma função escreva")
escreva("com o professor Gustavo Guanabara")
