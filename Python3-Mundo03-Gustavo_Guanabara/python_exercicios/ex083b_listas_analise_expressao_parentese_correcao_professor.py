# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite a espressão: ")
pilha = []
for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        # lista cheia
        if len(pilha) > 0:
            pilha.pop()
        # pilha vazia
        else:
            pilha.append(")")  # tem mais parenteses do que deveria
            break
# se a pilha tiver vazia tá correta
if len(pilha) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está errada.")
