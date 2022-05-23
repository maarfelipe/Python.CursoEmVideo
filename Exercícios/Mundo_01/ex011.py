"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados"""

alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))

area = alt * lar

print('')
print(f'A parede mede {alt:.1f}m x {lar:.1f}m\n'
      f'Sua área total é {area:.1f}m\n'
      f'Será necessário {area / 2:.1f}lts de tinta para preencher a parede')