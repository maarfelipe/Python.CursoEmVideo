"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""

"""
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'Maior: {n1}')
elif n2 > n3 and n2 > n1:
    print(f'Maior: {n2}')
else:
    print(f'Maior: {n3}')

if n1 < n2 and n1 < n3:
    print(f'Menor: {n1}')
elif n2 < n3 and n2 < n1:
    print(f'Menor: {n2}')
else:
    print(f'Menor: {n3}')
    """


for c in range(1, 4):
    num = int(input(f'Digite o {c}º número: '))
    if c == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'Maior: {maior}\n'
      f'Menor: {menor}')
