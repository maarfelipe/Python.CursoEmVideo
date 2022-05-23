"""Crie um programa que faça o computador jogar Jokenpô com você"""

from random import randint
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']

computador = randint(0, 2)
jogador = int(input(f'{"=" * 22}\n'
                    f'\033[1;30;45m{"VAMOS JOGAR JOKENPÔ!!!":^22}\033[m\n'
                    f'{"=" * 22}\n'
                    f'[ 0 ] PEDRA\n'
                    f'[ 1 ] PAPEL\n'
                    f'[ 2 ] TESOURA\n'
                    f'Escolha sua jogada: '))

if jogador == 0 or jogador == 1 or jogador == 2:
    print(f'{"=" * 22}\n'
          f' JO ... ', end=''), sleep(0.8)
    print('KEN ... ', end=''), sleep(0.8)
    print(f'PÔ !!\n'
          f'{"=" * 22}\n'
          f'Computador: {lista[computador]}\n'
          f'Jogador: {lista[jogador]}\n'
          f'{"=" * 22}')

    if jogador == computador:
        print(f'\033[1;43m{"EMPATE":^22}\033[m\n'
              f'{"=" * 22}')
    elif jogador == 0:
        if computador == 1:
            print(f'\033[1;30;45m{"COMPUTADOR GANHOU!!!":^22}\033[m\n'
                  f'{"=" * 22}')
        else:
            print(f'\033[1;30;44m{"JOGADOR GANHOU!!":^22}\033[m\n'
                  f'{"=" * 22}')
    elif jogador == 1:
        if computador == 2:
            print(f'\033[1;30;45m{"COMPUTADOR GANHOU!!!":^22}\033[m\n'
                  f'{"=" * 22}')
        else:
            print(f'\033[1;30;44m{"JOGADOR GANHOU!!":^22}\033[m\n'
                  f'{"=" * 22}')
    elif jogador == 2:
        if computador == 0:
            print(f'\033[1;30;45m{"COMPUTADOR GANHOU!!!":^22}\033[m\n'
                  f'{"=" * 22}')
        else:
            print(f'\033[1;30;44m{"JOGADOR GANHOU!!":^22}\033[m\n'
                  f'{"=" * 22}')
else:
    print('\033[1;31mJOGADA INVÁLIDA. TENTE NOVAMENTE!\033[m')


