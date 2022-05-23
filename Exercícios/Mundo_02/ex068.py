"""Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo"""

from random import randint

contador = 0
while True:
    computador = randint(0, 6)

    jogador_pi = ' '
    while jogador_pi not in 'PI':
        jogador_pi = str(input('PAR ou ÍMPAR? [P/I]: ')).upper().strip()[0]

    jogador_valor = -1
    while jogador_valor < 0 or jogador_valor > 5:
        jogador_valor = int(input('Faça sua jogada [0/5]: '))

    soma = computador + jogador_valor

    if jogador_pi in 'P' and soma % 2 == 0:
        jogador_ganhou = True
    elif jogador_pi in 'I' and soma % 2 == 1:
        jogador_ganhou = True
    else:
        jogador_ganhou = False

    print(f'COMPUTADOR: {computador}\n'
          f'JOGADOR: {jogador_valor:>4}\n'
          f'\033[1;30;46m{f"RODADA: {soma}":^14}\033[m')

    if jogador_ganhou is True:
        contador += 1
        print(f'\033[1;30;46m{"GANHOU !!!":^14}\033[m\n'
              f'{"=" * 14}')
    else:
        print(f'\033[1;30;41m{"PERDEU !!!":^14}\033[m\n'
              f'{"=" * 14}')
        break

if contador == 0:
    print('O jogador não venceu nenhuma vez!')
elif contador == 1:
    print('O jogador venceu uma vez!')
else:
    print(f'O jogador venceu {contador} vezes.')
