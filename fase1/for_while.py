'''
for i in range(0, 6):
    print(i)
'''
'''
i = 1
while(i < 11):
    print(i)
    i +=1
'''
'''
n = float(input("Digite um número: "))

soma = 0

while(n != 0):
    soma += n
    n = float(input("Digite outro número (0 para sair): "))

print(soma)
'''

# 2 - Ler do teclado uma lista com 5 inteiros e imprimir o menor valor.
lista = []
num = int(input("Digite um número: "))
lista.append(num)

while(len(lista) < 5):
    num = int(input("Digite um número: "))
    lista.append(num)

print(sum(lista))

