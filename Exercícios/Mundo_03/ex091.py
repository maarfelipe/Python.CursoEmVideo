"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
from time import sleep
from operator import itemgetter

resultados = {}

for cont in range(1, 5):
    resultados[f'Jogador{cont}'] = randint(1, 6)

print('Os jogos foram feitos: ')
for k, v in resultados.items():
    print(f'{k} tirou {v}')
    sleep(0.8)

resultados = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print()
for k, v in enumerate(resultados):
    print(f'{k+1}º lugar: {v[0]} que tirou {v[1]}')
    sleep(0.8)
