"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nasc
alis =  (18 - idade) + date.today().year

if idade == 18:
    print('Você tem 18 anos, você deve ser alistar imediatamente!')
elif idade < 18:
    print(f'Você tem {idade} anos. Seu alistamento será em {alis}.')
else:
    print(f'Você tem {idade} anos. Seu alistamento foi em {alis}.')