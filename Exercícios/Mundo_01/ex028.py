"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu"""

from random import randint

computador = randint(0, 5)
jogador = int(input('O computador escolheu um número de 0 a 5. Tente adivinhar qual foi: '))

if computador == jogador:
    print('\033[1;32mVENCEU!\033[m')
else:
    print('\033[1;31mPERDEU!\033[m')

print(f'O computador escolheu: {computador}\n'
      f'Você escolheu o número: {jogador}')

