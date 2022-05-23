"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o"""

cont = soma = 0
for c in range(1, 7):
    num = int(input(f'{c}º número: '))
    if num % 2 == 0:
        cont += 1
        soma += num

if cont == 0:
    print('Nenhum número par foi digitado.')
elif cont == 1:
    print(f'Somente um número par foi digitado, {soma}.')
else:
    print(f'{cont} números foram digitados e sua soma é {soma}.')
