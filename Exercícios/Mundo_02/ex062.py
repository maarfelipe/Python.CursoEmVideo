"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos."""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(primeiro, end=' → ')
        primeiro += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja apresentar a mais? '))
print(f'{total} FIM')
