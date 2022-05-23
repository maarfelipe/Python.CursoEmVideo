"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial"""


def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado
    :param show: (opcional) Mostrar ou não conta
    :return: Valor do fatorial de um número
    """
    from math import factorial
    f = factorial(num)

    if show:
        print(f'{num}! ', end='')
        for cont in range(num, 0, -1):
            print(cont, end=' ')
            if cont > 1:
                print('x ', end='')
            else:
                print('= ', end='')

    return f


# Código Principal
num = int(input('Digite um número para ver seu fatorial: '))
while True:
    show = ' '
    while show not in 'SN':
        show = str(input('Deseja apresentar a conta? [S/N] ')).upper().strip()[0]
    if show == 'S':
        show = True
    else:
        show = False
    break

print(fatorial(num, show))