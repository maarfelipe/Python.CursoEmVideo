"""Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada"""

from math import sqrt

var = int(input('Digite um número: '))

print('=' * 50)
print(f'Dobro: {var * 2}')
print(f'Triplo: {var * 3}')
print('=' * 50)
print(f'\033[1;42m{"RAÍZ QUADRADA":^50}\033[m')
print(f'Utilizando função pow: {pow(var, 1/2):.2f}\n'
      f'Utilizando valor elevado a meio: {var ** (1/2):.2f}\n'
      f'Utilizando SQRT da biblioteca de matemática: {sqrt(var):.2f}')
print('=' * 50)
