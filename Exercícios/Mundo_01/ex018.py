"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo"""

from math import sin, cos, tan, radians
var = int(input('Digite o valor do ângulo: '))

angulo = radians(var)
print(f'Seno: {sin(angulo):.2f}\n'
      f'Cosseno: {cos(angulo):.2f}\n'
      f'Tangente: {tan(angulo):.2f}')
