"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos"""

maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso {c}ª pessoa: '))

    if c == 1:
        maior = menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'Maior peso: {maior:.1f}kg\n'
      f'Menor peso: {menor:.1f}kg')
