"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense"""

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print('Os 5 primeiros times:')
for c in range(0, 5):
    print(f'{c+1} - {times[c]}')

print('\nOs últimos 4 colocados:', end=' ')
for c in range(-4, 0):
    print(times[c], end='')
    if c < -1:
        print(end=', ')
    else:
        print(end='.')

print('\n\nTimes em ordem alfabética: ', end='')
for c in sorted(times):
    print(c, end=', ')

print(f'\n\nEm que posição está o time da Chapecoense: {times.index("Chapecoense")+1}')


