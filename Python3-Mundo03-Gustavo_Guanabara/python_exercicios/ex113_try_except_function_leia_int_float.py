# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            valor_digitado = input(msg)
            valor_convertido = int(valor_digitado)
        except (ValueError, TypeError):
            print(
                f"\033[0;31mErro! '{valor_digitado}' Por favor digite um número inteiro válido!\033[m"
            )
            continue
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_convertido


def leiaFloat(msg):
    while True:
        try:
            valor_digitado = input(msg)
            valor_convertido = float(valor_digitado)
        except (ValueError, TypeError):
            print(
                f"\033[0;31mERRO! '{valor_digitado}' Por favor digite um número real válido!\033[m"
            )
            continue
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0
        else:
            return valor_convertido


numero_inteiro = leiaInt("Digite um número inteiro: ")
numero_float = leiaFloat("Digite um número real: ")
print(f"O número inteiro digitado foi: {numero_inteiro} e o real foi {numero_float}")
