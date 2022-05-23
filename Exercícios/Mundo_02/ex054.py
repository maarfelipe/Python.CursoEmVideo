"""Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores"""

from datetime import datetime

contmaior = contmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Ano de nascimento da {c}ª pessoa: '))

    idade = datetime.today().year - nasc

    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

if contmaior == 0 or contmenor == 0:
    if contmaior == 0:
        print('Não há nenhuma pessoa maior de idade, 07 (sete) menores de idade.')
    else:
        print('Não há nenhuma pessoa menor de idade, 07 (sete) maiores de idade.')
elif contmaior == 1 or contmenor == 1:
    if contmaior == 1:
        print(f'Temos uma pessoa maior de idade, 06 (seis) menores de idade.')
    else:
        print('Temos uma pessoa menor de idade, 06 (seis) maiores de idade.')
else:
    print(f'{contmaior} pessoas maiores de idade\n'
          f'{contmenor} pessoas menores de idade')