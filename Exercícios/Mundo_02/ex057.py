"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto"""

sexo = ''
while sexo not in 'MF':
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
print('FIM')