"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves"""

listaGeral = []
temp = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    listaGeral.append(temp[:])
    temp.clear()

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Desejar continuar? [S/N] ')).upper().strip()[0]
    if stop in 'N':
        break

mediaPeso = 0
for peso in listaGeral:
    mediaPeso += peso[1]
mediaPeso = mediaPeso / len(listaGeral)

pesadas = []
leves = []
for dado in listaGeral: 
    if dado[1] > mediaPeso:
        pesadas.append(dado[0].capitalize())
    else:
        leves.append(dado[0].capitalize())

print(f'Quantas pessoas foram cadastradas: {len(listaGeral)}\n'
      f'Uma listagem com as pessoas mais pesadas: {pesadas}\n'
      f'Uma listagem com as pessoas mais leves: {leves}')
