"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados"""

numero = int(input('Digite um número entre 0 e 9999: '))    # 1234
print(f'Unidade: {numero // 1 % 10}\n'                      # 1234 // 1 = 1234 % 10 = 4
      f'Dezena: {numero // 10 % 10}\n'                      # 1234 // 10 = 123 % 10 = 3
      f'Centena: {numero // 100 % 10}\n'                    # 1234 // 100 = 12 % 10 = 2
      f'Milhar: {numero // 1000 % 10}')                     # 1234 // 1000 = 1 % 10 = 1
