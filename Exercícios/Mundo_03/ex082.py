"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas"""

geral = []
par = []
impar = []

while True:
    geral.append(int(input('Digite um número: ')))

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if stop in 'N':
        break
geral.sort()

for c in geral:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Geral: {geral}\n'
      f'Pares: {par}\n'
      f'Ímpar: {impar}')
