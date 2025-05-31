# #from uteis import fatorial, dobro
# ## > Use from x import y quando o nome for claro, controlado e o projeto for pequeno ou bem organizado.
# import uteis # esse é a melhor prática para evitar conflitos internos com outras bliblitecas do python
# ## Prefira import x quando quiser segurança, evitar conflitos e melhorar a rastreabilidade, especialmente em projetos maiores.

from uteis import numeros

## aqui foi criado um pacote chamado uteis
## depois outros pacotes ou módulos dentro dele


# num = int(input("Digite um valor "))
# fat = uteis.fatorial(num)
# print(f"O fatoria de {num} é {fat}")
# print(f"O dobro de {num} é {uteis.dobro(num)}")

# num = int(input("Digite um valor "))
# fat = fatorial(num)
# print(f"O fatoria de {num} é {fat}")
# print(f"O dobro de {num} é {dobro(num)}")

num = int(input("Digite um valor "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}")
print(f"O dobro de {num} é {numeros.dobro(num)}")
