"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci.

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8"""

n = int(input('Quantos termos o programa deve apresentar: '))

primeiro = 0
segundo = 1
contador = 0

while contador < n:
    print(primeiro, end=' → ')
    contador += 1
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
print('FIM')
