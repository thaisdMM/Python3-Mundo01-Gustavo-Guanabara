expressoes_usuarios = input(
    "Digite uma expressão matemática que use parênteses para ver se a expressão está correta: "
)
# expressoes = [expressoes_usuarios]
# expressoes2 = [(a+b)]

# print(type(expressoes))
# print(f"Tamaho da lista {len(expressoes)}")


abriu_paretense = fechou_parentese = contador= 0
for valores in expressoes_usuarios:
    print(f"Valores: {valores}")
    if expressoes_usuarios[0] == ")":
        print("Expressao aberta inválidamente.")
        break
    elif expressoes_usuarios[-1] == "(":
        print("Expressao fechada inválidamente.")
        break
    elif valores == ")":
        fechou_parentese -= 1
    elif valores == "(":
        abriu_paretense += 1
    total_parenteses = fechou_parentese + abriu_paretense
    if total_parenteses < 0:
        print("Expressão inválida.")
        break


    contador +=1
    print(contador)
    print(f"total: {total_parenteses}")

print(f"A expressão digitada foi: {expressoes_usuarios}")
print(f"Total de abriu parenteses {abriu_paretense}")
print(f"Total de fechou parenteses {fechou_parentese}")
if abriu_paretense == fechou_parentese != 0:
    print(f"A expressão é valida!")
else:
    print(f"A expressão é inválida.")

    # if expressoes_usuarios.find(")") == True:
    #     print("Expressao aberta inválidamente.")
    #     break

    # elif expressoes_usuarios[-1] == "(":
    #     print("Expressao fechada inválidamente.")
    #     break
