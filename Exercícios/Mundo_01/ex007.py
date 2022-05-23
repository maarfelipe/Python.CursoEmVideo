"""Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média"""

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite  2ª nota: '))

print(f'Media: {(nota1 + nota2) / 2:.1f}')

"""
media = 0
for c in range(1, 3):
    var = float(input(f'Digite a {c}ª nota: '))
    media += var
print(f'Media: {media / c:.1f}')
"""
