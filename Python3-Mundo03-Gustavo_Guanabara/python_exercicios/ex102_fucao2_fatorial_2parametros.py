# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor de fatorial de um número em param número.
    """
    resultado_fatorial = 1
    for i in range(numero, 0, -1):
        resultado_fatorial *= i
        if show == True:
            print(f"{i}", end="")
            print(f" x " if i > 1 else " = ", end="")
        # NAO PRECISO DO CÓDIGO ABAIXO, POIS ELE JÁ É EXIBIDO DE QUALQUER FORMA NO RETURN
        #      resultado_fatorial
        # else:
        #     resultado_fatorial

    return resultado_fatorial


print(fatorial(5, True))
print(fatorial(4))
#help(fatorial)
