"""Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato."""

soma = contMaisMil = cont = precoMaisBarato = 0
nomeMaisBarato = ''
while True:
    nomeProduto = str(input('Produto: ')).upper().strip()
    precoProduto = float(input('Preço: R$'))

    soma += precoProduto

    if precoProduto > 1000:
        contMaisMil += 1

    cont += 1
    if cont == 1:
        precoMaisBarato = precoProduto
        nomeMaisBarato = nomeProduto
    elif precoProduto < precoMaisBarato:
        precoMaisBarato = precoProduto
        nomeMaisBarato = nomeMaisBarato

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if stop in 'N':
        break
print(f'Qual é o total gasto na compra: R${soma:.2f}\n'
      f'Quantos produtos custam mais de R$1000: {contMaisMil}\n'
      f'Qual é o nome do produto mais barato: {nomeMaisBarato}')
