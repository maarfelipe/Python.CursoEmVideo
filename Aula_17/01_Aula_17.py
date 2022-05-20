num = [2, 5, 9, 1]

num[2] = 3                  # Troca o valor do 2º índice por 3
num.insert(1, 10)           # Add o valor 10 no índice 1
num.append(7)               # Add o valor 7 ao final da lista

num.pop()                  # Retira o valor do final da lista
num.pop(2)                 # Retira o valor do índice 2
if 4 in num:
    num.remove(4)          # Procura o valor 4 na lista e o remove
else:
    print('Não tem número 4')

num.sort()                 # Coloca a lista em ordem crescente
num.sort(reverse=True)     # Coloca a lista em ordem decrescente

print(len(num))
print(num)

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

valores = []
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}\n'
      f'Lista B: {b}')
