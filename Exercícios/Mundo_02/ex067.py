"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo"""

while True:
    num = int(input('Digite um número: '))

    if num < 0:
        break

    print('=' * 20)
    for c in range(0, 11):
        print(f'{num:>2} x {c:>2} = {num * c:>2}')
    print('=' * 20)
print('FIM')
