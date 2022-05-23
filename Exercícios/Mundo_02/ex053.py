"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA"""

frase = str(input('Digite a frase: ')).replace(' ', '')

inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]

if inverso == frase:
    print(f'{frase} = {inverso}\n'
          f'\033[1;32mTEMOS UM PALÍNDROMO!\033[m')
else:
    print(f'{frase} != {inverso}\n'
          f'\033[1;31mNÃO TEMOS UM PALÍNDROMO!\033[m')
