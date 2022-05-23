"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares"""

numbers = (int(input('Digite o primeiro número: ')), int(input('Digite o segundo número: ')),
            int(input('Digite o terceiro número: ')), int(input('Digite o quarto número: ')))

print(f'Quantas vezes apareceu o valor 9: {numbers.count(9)}')

if 3 in numbers:
    print(f'Em que posição foi digitado o primeiro valor 3: {numbers.index(3)+1}')

print('Quais foram os números pares: ', end='')
for c in numbers:
    if c % 2 == 0:
        print(c, end=' ')