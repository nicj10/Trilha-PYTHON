# Python é uma linguagem dinamicamente tipada, eu não preciso declarar o tipo da váriavel algumas vezes

#idade = 18 
#print(type(idade)) # Ele já reconhece que o tipo é inteiro(int).

# INTEIRO (int)
# Escrito sem componente decimal, apenas números inteiros
print('INT')
ano = 2005
print(ano)
print(type(ano))
print('-------------------------------------------')

#PONTO FLUTUANTE (float)
# Caracteres numéricos decimais
print('FLOAT')
altura = 1.72
print(altura)
print(type(altura))
print('-------------------------------------------')

# COMPLEXO (complex)
# Normalmente usado em cálculos geométricos e científicos
print('COMPLEX')

a = 5 + 2j
b = 20 + 6j
print(complex(a, b))
print(type(a))
print(type(b))
print('-------------------------------------------')

# STRING (str)
# Usado para representar palavras
print("STRING")

nome = 'Nicholas Matheus'

print(nome)
print(type(nome))
print('-------------------------------------------')

#BOOLEANO (bool)
# Só pode assumir apenas dois valores (TRUE OR FALSE)

fds = True
ferias = False

print(fds)
print(ferias)
print(type(fds))
print(type(ferias))
print('-------------------------------------------')

#LISTAS (List)
#Agrupam um conjunto de elementos variados 
print('LIST')
dias = [1, 2, 3, 4, 5, 6, 7]

print(dias)
print(type(dias))

# Percebe-se que, em nenhum momento precisamos declarar o tipo da variavel antes dela ou na atribuiçção de um dado. Isso se dá pela tipagem da linguagem.