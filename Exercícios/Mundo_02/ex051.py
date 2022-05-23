"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão"""

p1 = int(input('Primeiro termo da P.A.: '))
razao = int(input('Razão: '))

for c in range(p1, (razao*9) + p1 + 1, razao):
    print(f'{c} → ', end='')
print('FIM')