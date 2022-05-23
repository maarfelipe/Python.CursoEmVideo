"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""

from math import factorial

num = int(input('Digite um número: '))

print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(factorial(num))

"""
from math import factorial

num = int(input('Digite um número: '))
temp = num

print(f'{num}! = ', end='')
while temp > 0:
    print(temp, end='')
    temp -= 1
    if temp > 0:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(factorial(num))
"""
