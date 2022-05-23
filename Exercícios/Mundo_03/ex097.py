"""Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~"""


def escreva(txt):
    tam = len(txt) + 6
    print(f'{"~" * tam}\n'
          f'{txt:^{tam}}\n'
          f'{"~" * tam}')


# Código Principal
msg = str(input('Digite sua mensagem: ')).capitalize().strip()
escreva(msg)
