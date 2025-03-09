numero = input("Digite um numero de 0 a 9999: ")
numero = numero.zfill(4) # Garante que a string tenha exatamente 4 caracteres  
unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f""" unidade = {unidade}
dezena = {dezena}
centena = {centena}
milhar = {milhar} """)