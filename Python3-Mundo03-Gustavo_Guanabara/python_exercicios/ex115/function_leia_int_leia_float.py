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
