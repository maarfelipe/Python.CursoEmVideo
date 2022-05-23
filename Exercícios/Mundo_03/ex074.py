"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla"""

from random import randint

numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'Lista: {numeros}\n'
      f'Maior: {max(numeros)}\n'
      f'Menor: {min(numeros)}')
