"""Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for"""

num = int(input('Número: '))

for c in range(0, 11):
    print(f'{num:>2} x {c:>2} = {num * c:>2}')