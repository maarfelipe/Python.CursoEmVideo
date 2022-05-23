"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer"""

from random import randint

computador = randint(0, 11)
jogador = int(input('O computador escolheu um número de 0 a 10. Tente adivinhar qual foi: '))

if computador == jogador:
    print(f'Você adivinhou na 1ª tentativa! Parabéns!')
else:
    cont = 1
    while jogador != computador:
        jogador = int(input('Tente novamente: '))
        cont += 1

print(f'Você conseguiu em {cont} tentativas!\n'
      f'COMPUTADOR: {computador}\n'
      f'JOGADOR: {jogador}')