# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            numero = input(msg)
            return int(numero)
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            return 0

        except:
            print(
                f"\033[0;31mErro! '{numero}' Por favor digite um número inteiro válido!\033[m"
            )


def leiaFloat(msg):
    while True:
        try:
            numero = input(msg)
            return float(numero)
        except KeyboardInterrupt:
            print(f"\33[0;31mUsuário preferiu não digitar esse número.\033[m")
            numero = 0
            return numero

        except:
            print(
                f"\033[0;31mERRO! '{numero}' Por favor digite um número real válido!\033[m"
            )


numero_inteiro = leiaInt("Digite um número inteiro:")
numero_float = leiaFloat("Digite um número real: ")
print(f"O número inteiro digitado foi: {numero_inteiro} e o real foi {numero_float}")
