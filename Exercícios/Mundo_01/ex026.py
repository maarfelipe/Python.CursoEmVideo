"""Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez"""

frase = str(input('Digite a frase: ')).strip().upper()

print(f'Quantas vezes aparece a letra "A": {frase.count("A")}\n'
      f'Em que posição ela aparece a primeira vez: {frase.find("A")}\n'
      f'Em que posição ela aparece a última vez: {frase.rfind("A")}')
