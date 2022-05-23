"""Faça um programa que leia um ano qualquer e mostre se ele é bissexto"""

from datetime import date

ano = int(input('Digite o ano (digite 0 para ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print('\033[1;32mBISSEXTO\033[m')
else:
    print('\033[1;31mNÃO É BISSEXTO\033[m')
