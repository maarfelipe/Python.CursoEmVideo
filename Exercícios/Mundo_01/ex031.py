"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas"""

distancia = int(input('Digite a distância da viagem: '))

if distancia <= 200:
    print(f'R$0,50 por Km para viagens de até 200Km: R${distancia * 0.50:.2f}')
else:
    print(f'R$0,45 por km para viagens mais longas que 200km: R${distancia * 0.45:.2f}')
