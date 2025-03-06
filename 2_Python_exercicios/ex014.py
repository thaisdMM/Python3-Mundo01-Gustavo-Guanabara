celsius = float(input("Digite a temperatura em graus celsius para ser convertida em fahrenheit: "))
# conversao_celsius_fahrenheit = (celsius * 1.8) + 32
conversao_celsius_fahrenheit = ((9*celsius)/5)+32 #pode fazer sem os parenteses pq a ordem de precedencia dessa expressao é a ordem que os operadores aparecem
print(f"{celsius} C graus celsius convertidos para fahrenheit são: {conversao_celsius_fahrenheit} F")