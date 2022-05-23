"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular"""

lista = ('Item 01', 29.80, 'Item 02', 12.50, 'Item 03', 36.45, 'Item 04', 9.90, 'Item 05', 18.99,
         'Item 06', 45.30, 'Item 07', 31.10, 'Item 08', 19.20, 'Item 09', 3.80, 'Item 10', 1.80)

for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<20} ', end='')
    else:
        print(f'R$ {lista[c]:>5.2f}')
