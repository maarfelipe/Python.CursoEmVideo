"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente"""


def ficha(nome, gols=False):
    return f'O jogador {nome} fez {gols} gol(s).'


# Código Principal
nome = str(input('Nome do jogador: ')).capitalize().strip()
if nome == '':
    nome = '<DESCONHECIDO>'

gols = str(input('Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome, gols))