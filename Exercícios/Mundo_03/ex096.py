"""Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno"""

def area(larg, comp):
    a = larg * comp
    print(f'A área de {larg} x {comp} é {a}m²')


# Programa Principal
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(larg, comp)