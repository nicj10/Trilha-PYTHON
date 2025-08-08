# OPERADORES 

# OPERDAORES ARITMÉTICOS

# SOMA - print(1+2) = 3
# SUBTRAÇÃO - print (2-1) = 1
# MULTIPLICAÇÃO - print(50*2) = 100
# DIVISÃO - print(10/2) = 5
# RESTO DA DIVISÃO - print(10%3) = 1
# PARTE INTEIRA DA DIVISÃO - print(10//3) = 3

# OPERADORES DE ATRIBUIÇÃO

# += (A MESMA LÓGICA SERVE PARA AS DEMAIS OPERAÇÕES )
""" i = 0

while i < 10:
    print('oii')
    i +=1 """

# := (walrus)
# Ele atribui um valor a variavel ao mesmo tempo que imprime.
# print(qtde:=10) 

# OPERADORES DE COMPARÇÃO

# == (Verifica se dois valores são iguais)
"""
a = 5
b = 5
print("A é igual a B")
print(a == b) 
"""
# != (Verifica se dois valores são diferentes)
""""
a = 3
b = 5
print("A é diferente de B")
print(a != b)
"""

# > (Maior que) ou >= (Maior ou igual)
""""
a = 16
b = 16

print("A é maior que B")
print(a > b)

print("A é maior ou igual a B")
print(a >= b)
OBS: A mesma lógica se aplica ao menor que e ao menor ou igual a que.
"""

# OPERADORES LÓGICOS

# AND (Depende dos dois fatores)
"""
a = 10
b = 15

print("A é maior que B e B é meaior que 9")
print(a > b and b > 9) # B é maior que 9, mas A não é maior que B

print("A é menor que B e B é maior que 11")
print(a < b and b > 11) # A combinação dos dois gera o True
"""

# OR (Depende apenas de uma das condições)
"""
a = "Nicholas"
b = 19

print("A pessoa se chama nicholas? ou tem mais de 20 anos?")
print(a == "Nicholas" or b > 20) # Partindo da primeira condição ele retorna o true

print(a == "Matheus" or b > 20) # As duas condições são falsas
"""

# NOT (inverte o valor de uma condição)
'''
a = 5 
print("A não é maior que 7")
print(not a > 7)
'''
# OPERADOR DE IDENTIDADE - IS
# Verifica se dois objetos são o mesmo objeto na memória
'''
a = [1, 2, 3]
b = a 
c = [1, 2, 3]

print("A e B são a mesma coisa")
print(a is b) # Retorna true pois A = B

print("A e C são a mesma coisa")
print(a is c) # Apesar de terem os mesmos dados são diferentes e ocupam objetos de memória distintos
'''
# OPERADOR DE PERTENCIMENTO - IN

lista = ['Nicholas', 'Jhossuan', 'João', 'Matheus']

print('Seu nome está na lista?')
nome = input("Digite seu nome: ")

if(nome in lista):
    print('SIM')
else: 
    print('NÃO')