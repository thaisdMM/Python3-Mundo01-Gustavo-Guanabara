expressoes_usuarios = list(input(
    "Digite uma expressão matemática que use parênteses para ver se a expressão está correta: "
))
# print(f"expressoes_usuarios: {expressoes_usuarios}")
# print(type(expressoes_usuarios))
# print(f"Tamaho da lista {len(expressoes_usuarios)}")


abriu_paretense = fechou_parentese = contador= 0

if  "(" not in expressoes_usuarios and ")" not in expressoes_usuarios:
    print(f"A expressão é inválida. Sequer tem parenteses.")
if expressoes_usuarios[0] == ")":
    print("Expressao aberta inválidamente.")
elif expressoes_usuarios[-1] == "(":
    print("Expressao fechada inválidamente.")
else:
    for valores in expressoes_usuarios:
        # if  "(" not in expressoes_usuarios and ")" not in expressoes_usuarios:
        #     print(f"A expressão é inválida. Sequer tem parenteses.")
        #     break
        # print(f"Valores: {valores}")
        # if expressoes_usuarios[0] == ")":
        #     print("Expressao aberta inválidamente.")
        #     break
        # elif expressoes_usuarios[-1] == "(":
        #     print("Expressao fechada inválidamente.")
        #     break
        if valores == ")":
            fechou_parentese -= 1
        elif valores == "(":
            abriu_paretense += 1
        total_parenteses = fechou_parentese + abriu_paretense
        if total_parenteses < 0:
            print("Expressão inválida.")
            break


        contador +=1
        # print(contador)
        # print(f"total: {total_parenteses}")
    if  total_parenteses == 0:
        print(f"A expressão é valida!")
    else:
        print(f"A expressão é inválida.")


print(f"A expressão digitada foi: {expressoes_usuarios}")
# print(f"Total de abriu parenteses {abriu_paretense}")
# print(f"Total de fechou parenteses {fechou_parentese}")
