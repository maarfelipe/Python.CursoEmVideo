"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela"""

lista = []

for c in range(1, 6):
    temp = int(input(f'Digite o {c}º valor: '))

    if c == 1 or temp > max(lista):
        lista.append(temp)
        print(f'Número {temp} adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if temp <= lista[pos]:
                lista.insert(pos, temp)
                print(f'Número {temp} adicionado na posição {pos} da lista.')
                break
            pos += 1
print(lista)