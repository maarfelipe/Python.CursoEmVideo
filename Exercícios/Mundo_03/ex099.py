"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior"""

from random import sample


def maior(ini, fim, qtde):
    randomizador = sample(range(ini, fim), qtde)
    print(f'Os valores gerados foram: {randomizador}\n'
          f'O maior valor foi: {max(randomizador)}\n'
          f'{"=" * 50}')


# Código Principal
maior(1, 10, 3)
maior(1, 50, 6)
maior(1, 1000, 3)