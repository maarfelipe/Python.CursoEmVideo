"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta"""

from random import randint
from time import sleep
jogadas = []
dados = []

qtdeJogos = int(input('Quantos jogos quer gerar? '))

for jogos in range(0, qtdeJogos):
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in dados:
            dados.append(num)
            cont += 1
        if cont >= 6:
            break
    jogadas.append(dados[:])
    dados.clear()

if qtdeJogos == 1:
    print('Foi gerado um jogo:')
else:
    print(f'Foi gerado {len(jogadas)} jogos:')
for pos, cont in enumerate(jogadas):
    cont.sort()
    print(f'{pos+1}º Jogo: ', end='')
    for c in cont:
        print(c, end=' ')
        sleep(0.6)
    print()
