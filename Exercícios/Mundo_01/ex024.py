"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"""

cidade = str(input('Digite o nome da cidade: ')).upper().strip().split()
print('SANTO' in cidade[0])
