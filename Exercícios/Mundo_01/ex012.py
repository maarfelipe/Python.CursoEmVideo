"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto"""

preco = float(input('Digite o valor do produto: R$ '))

desconto = preco * 0.05

print(f'Este produto tem 5% de desconto no valor de R$ {desconto:.2f}\n'
      f'Seu valor final é R$ {preco - desconto:.2f}')
