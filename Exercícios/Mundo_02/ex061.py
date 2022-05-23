"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while"""

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1
print(f'{primeiroTermo} → ', end='')
while cont < 10:
    primeiroTermo += razao
    print(primeiroTermo, end=' → ')
    cont += 1
print('FIM')
