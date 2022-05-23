"""Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""

stop = 'S'
cont = maior = menor = media = 0
while stop in 'S':
    num = int(input('Digite um número: '))

    if cont == 0:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    media += num

    cont += 1
    stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print(f'Maior: {maior}\n'
      f'Média: {media / cont:.1f}\n'
      f'Menor: {menor}')