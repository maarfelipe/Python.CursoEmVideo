"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista
 e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior"""

from random import randint


def sorteia(lista):
    for val in range(0, 5):
        lista.append(randint(0, 99))
    lista.sort()
    print(f'Os números sorteados foram: {lista}')


def somaPar(lista):
    soma = 0
    for val in lista:
        if val % 2 == 0:
            soma += val
    print(f'A soma dos valores pares é {soma}')


# Código Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
