"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista"""

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if stop in 'N':
        break

lista.sort(reverse=True)
print(f'Quantos números foram digitados: {len(lista)}\n'
      f'A lista de valores, ordenada de forma decrescente: {lista}\n'
      f'Se o valor 5 foi digitado e está ou não na lista: ', end='')
if 5 in lista:
    print('SIM')
else:
    print('NÃO')