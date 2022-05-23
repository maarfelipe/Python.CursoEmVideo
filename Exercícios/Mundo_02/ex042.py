"""Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes"""

lista = []
for c in range(1, 4):
    temp = int(input(f'Digite o valor da {c}ª reta: '))
    lista.append(temp)

print(f'As retas: {lista}')
if lista[0] + lista[1] > lista[2] and lista[1] + lista[2] > lista[0] and lista[0] + lista[2] > lista[1]:
    print('Formam um triângulo: ', end='')
    if lista[0] == lista[1] == lista[2]:
        print('EQUILÁTERO, todos os lados iguais')
    elif lista[0] == lista[1] or lista[0] == lista[2]:
        print('ISÓSCELES, dois lados iguais e um diferente')
    else:
        print('ESCALENO, todos os lados diferentes')
else:
    print('Não formam um triângulo!')

