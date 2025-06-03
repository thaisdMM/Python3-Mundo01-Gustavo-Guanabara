# try: 'tentar' a operação
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# except: "falhou"/deu problema a operação que foi tentada
except:
    print("Infelizmente tivemos um problema :(")
# else é uma clausula opcional, você não precisa usar sempre
# else: deu certo o try
else:
    print(f"O resultado é {r:.1f}")
# finaly é uma clausula opcional, você não precisa usar sempre
# finaly se usar esse comando o que está dentro dela acontece sempre.
# > ou seja: aparece quando try dá certo ou quando falha e entra no except
finally:
    print("Volte sempre! Muito obrigado.")

# Podemos escrever qual foi o problema:

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito obrigado.")

# # # Resposta TERMINAL:
# # Numerador: 5
# # Denominador: oi
# # Problema encontrado foi <class 'ValueError'>
# # Volte sempre! Muito obrigado.

# # Numerador: 5
# # Denominador: 0
# # Problema encontrado foi <class 'ZeroDivisionError'>
# # Volte sempre! Muito obrigado

# # O mesmo try pode ter varios except:
## também pode fazer um try com except para cada ação, no exemplo abaixo poderia ser 1 para a outro para b e outro para r

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# se for mais de um erro pode colocar entre() separados por virgula
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
except KeyboardInterrupt:
    print("O usuário prefiriu não informar os dados!")
# dá para fazer també o erro genérico:
# é interessante usar no desenvolvimento
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print("Volte sempre! Muito obrigado.")

# # RESULTADOS DO TERMINAL:

# # Numerador: 7
# # Denominador: 0
# # Não é possível dividir um número por zero!
# # Volte sempre! Muito obrigado.

# # Numerador: 8
# # Denominador: dois
# # Tivemos um problema com os tipos de dados que você digitou.
# # Volte sempre! Muito obrigado.
# # DEU ENTER SEM DIGITAR NADA:
# # Numerador:
# # Tivemos um problema com os tipos de dados que você digitou.
# # Volte sempre! Muito obrigado.
# # PAROU O PROGRAMA NO MEIO (control+c ou stop):
# Numerador: 200
# Denominador: ^CO usuário prefiriu não informar os dados!
# Volte sempre! Muito obrigado.
