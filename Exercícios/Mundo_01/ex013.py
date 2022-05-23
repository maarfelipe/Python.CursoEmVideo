"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento"""

salario = float(input('Digite o valor do salário: R$ '))

aumento = salario * 0.15

print(f'O funcionário terá 15% de aumento no valor de R$ {aumento:.2f}\n'
      f'O valor do salário com o aumento será R$ {salario + aumento:.2f}')
