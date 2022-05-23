"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista"""

valores = []
for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}º valor: ')))

print(f'Os valores digitados são: {valores}\n'
      f'Maior: {max(valores)}, na posição: ', end='')
for pos, v in enumerate(valores):
    if max(valores) == v:
        print(pos+1, end=' ')
print(f'\nMenor: {min(valores)}, na posição: ', end='')
for pos, v in enumerate(valores):
    if min(valores) == v:
        print(pos+1, end=' ')
