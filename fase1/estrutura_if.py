#Funções com apenas duas opções, se atender ao requisito cai no if, se não cai no else
'''
a = 2
if (a > 3):
    print('Cai no if')
else: 
    print('cai no else')
'''
#Aqui já podemos ver mais de duas condições fazendo o uso do ELIF
'''
a = 7

if(a < 5):
    print('menor que 5')
elif(a == 5):
    print('é 5')
else:
    print('maior que 5')
'''

### EXERCÍCICIOS ###

# 1. Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.
'''
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if(a > b):
    print(f"O menor número é {b}")
elif(a == b):
    print(f"Os números são iguais")
else:
    print(f"O menor número é {a}")
'''
# 2 Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela pode doar sangue ou não.
'''
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (Ex: 55.1): "))
horas = int(input("Quantas horas você dormiu esta noite? "))

if(idade >= 16 and idade <= 69 and peso >= 50 and horas >= 6):
    print("Voce pode doar sangue normalmente.")
else:
    print("Você não pode doar sangue")
'''
# 3 - Valor de delta
'''
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b**2) - (4 * a * c)
print(delta)
if(delta > 0):
    print("Possui duas raízes reais")
elif(delta == 0):
    print("Possui uma raiz real")
else:
    print("Não possui raiz real")
    '''
# 4 - Adição com condicional.
'''
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

soma = a + b
if(soma > 20):
    print(f"Resultado: {soma + 8}")
else:
    print(f"Resultado: {soma - 5}")
'''
# 5 Raiz ou potência?
'''
import math

num = float(input("Digite um número: "))
if(num < 0):
    print(math.pow(num, 2))
else:
    print(math.sqrt(num))
'''
# 6 - Meses do ano
'''
mes = int(input("Digite um número de 1 a 12: "))

def definirMes(mes):
    match mes:
        case 1:
            return "Janeiro"
        case 2:
            return "Fevereiro"
        case 3:
            return "Março"
        case 4:
            return "Abril"
        case 5:
            return "Maio"
        case 6:
            return "Junho"
        case 7:
            return "Julho"
        case 8:
            return "Agosto"
        case 9: 
            return "Setembro"
        case 10:
            return "Outubro"
        case 11: 
            return "Novembro"
        case 12: 
            return "Dezembro"
        case _:
            return "Número inválido"
        
print(definirMes(mes))
'''