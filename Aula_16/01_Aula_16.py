lanche = ('Burguer', 'Suco', 'Pizza', 'Pudim', 'Batatas Fritas')
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])
print(sorted(lanche))

for c in lanche:
    print(f'Eu vou comer {c}')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na posição {c}!')
print('Comi pra caramba!')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na posição {pos}!')
print('Comi pra caramba!')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))

pessoa = ('Gustavo', 39, 'Masc', 99.88)
del(pessoa)
print(pessoa)
