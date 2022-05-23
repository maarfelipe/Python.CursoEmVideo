"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

num = int(input('Número: '))

cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print('\033[m→ ', end='')
if cont == 2:
    print('PRIMO')
else:
    print('NÃO PRIMO')
