"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa."""

""" 
from math import hypot
cata = int(input('Digite o valor do cateto adjacente: '))
cato = int(input('Digite o valor do cateto oposto: '))
print(f'O valor da hipotenusa é {hypot(cata, cato):.2f}')
"""

cata = int(input('Digite o valor do cateto adjacente: '))
cato = int(input('Digite o valor do cateto oposto: '))
print(f'O valor da hipotenusa é {((cata ** 2) + (cato ** 2)) ** (1/2):.2f}')
