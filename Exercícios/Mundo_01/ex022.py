"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas
- Quantas letras ao total (sem considerar espaços)
- Quantas letras tem o primeiro nome"""

nome = str(input('Digite o nome completo: ')).strip()

print(f'O nome com todas as letras maiúsculas e minúsculas: {nome.title()}\n'
      f'Quantas letras ao total (sem considerar espaços): {len(nome.replace(" ", ""))}\n'
      f'Quantas letras tem o primeiro nome: {len(nome.split()[0])}')
