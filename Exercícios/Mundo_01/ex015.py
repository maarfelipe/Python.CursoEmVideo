"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
 pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado"""

dias = int(input('Por quantos dias o automóvel ficou alugado? '))
distancia = int(input('Quantos km rodados durante a locação? '))

valoraluguel = dias * 60
valordistancia = distancia * 0.15

print(f'O automóvel foi alugado por {dias:.0f} dias e percorreu {distancia:.0f}km\n'
      f'O aluguel custa R$ 60.00 por dia, totalizando R$ {valoraluguel:.2f}\n'
      f'Cada km rodado custa R$ 0.15 totalizando R$ {valordistancia:.2f}\n'
      f'Total: R$ {valordistancia + valoraluguel:.2f}')