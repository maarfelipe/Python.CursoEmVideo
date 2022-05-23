"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar"""

var = float(input('Quanto dinheiro você tem em carteira? R$ '))

print(f'Com R$ {var:.2f} é possível comprar US$ {var / 3.27:.2f}')
