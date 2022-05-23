"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal"""

num = int(input('Digite um número: '))
conv = int(input('[ 1 ] BINARIO\n'
                 '[ 2 ] OCTAL\n'
                 '[ 3 ] HEXADECIMAL\n'
                 'Escolha qual base deseja ver a convesão: '))
if conv == 1:
    print(f'{num} em BINARIO é: {bin(num)[2:]}')
elif conv == 2:
    print(f'{num} em OCTAL é: {oct(num)[2:]}')
else:
    print(f'{num} em HEXADECIMAL é: {hex(num)[2:]}')

