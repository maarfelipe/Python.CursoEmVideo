"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
possíveis sobre ele"""

var = input('Digite um valor: ')
print(f'O tipo primitivo desta variável sempre será {type(var)} pois o input não foi convertido.')
print('É alfabética? ', var.isalpha())
print('É alfanumérica? ', var.isalnum())
print('É um número? ', var.isnumeric())
print('Está em minúsculas? ', var.islower())
print('Está em maiúsculas? ', var.isupper())
print('É somente espaços? ', var.isspace())
print('Está capitalizada? ', var.istitle())
