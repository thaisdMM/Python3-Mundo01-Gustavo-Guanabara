# testando cores
# no do professor dá pra ver as cores melhores quando ele coloca fundo, já no meu nao acho que tem haver com a extensao dark pro que to usando no meu VS code


# #texto vermelho
# print("\033[31mOlá, mundo!")

# #texto vermelho, fundo amarelo
# print("\033[31;43mOlá, Thaís!")

# # letra negrito, texto vermelho, fundo amarelo até o final da tela
# print("\033[1;31;43mOlá, Thaís!")

# print("Bem vindo!!!") # ele tá pegando as configurações anteriores. Vou comentar tudo para fazer os testes

# letra negrito, texto vermelho, fundo amarelo só na parte do texto - \033[m fechar as configurações
print("\033[1;31;43mHello, World!\033[m")

print("Teste") # não está pegando as configurações anteriores

# letra sublinhada, texto vermelho, fundo azul só na parte do texto - \033[m fechar as configurações
print("\033[4;31;44mLetra sublinhada, cor vermelha, fundo azul\033[m")
print("oii") # teste > tem que fechar senão continua pegando a configuração antarior de cor e estilo

#letra normal, branca(para o prof é branca, mas no meu terminal deu cinza), fundo lilas
print("\033[0;30;45mLetra normal, branca, fundo lilás\033[m")

# letra no meu, na verdade o 37 é que deixa branco, fundo preto
print("\033[37mLetra branca, fundo preto\033[m")

print("Cor normal") # cor normal, no meu é cinza

# 7 inverter para dar o fundo branco
print("\033[7;37mFundo branco, letra preta\033[m")

# negrito, letra amarela, fundo azul
print("\033[1;33;44mLetra amarela, fundo azul\033[m")

# invertendo, negrito, fundo amarelo, letra azul
print("\033[1;7;33;44mFundo amarelo, letra azul\033[m")

a = 3
b = 5
print(f"\nOs valores são \033[32m{a}\033[m e \033[45m{b}\033[m!!!")