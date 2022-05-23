"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo"""

"""
a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    print('\033[1;32mFORMA TRIÂNGULO\033[m')
else:
    print('\033[1;31mNÃO FORMA TRIÂNGULO\033[m')
"""

lista = []
for c in range(1, 4):
    temp = int(input(f'Digite o valor da {c}ª reta: '))
    lista.append(temp)

if lista[0] + lista[1] > lista[2] and lista[1] + lista[2] > lista[0] and lista[0] + lista[2] > lista[1]:
    print('\033[1;32mFORMA TRIÂNGULO\033[m')
else:
    print('\033[1;31mNÃO FORMA TRIÂNGULO\033[m')