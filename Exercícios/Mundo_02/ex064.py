"""Crie um programa que leia vários números inteiros pelo teclado.

O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""

soma = contador = 0
num = int(input('Digite um valor: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um valor: '))
print(f'{contador} números foram digitados\n'
      f'Resultado: {soma}')
