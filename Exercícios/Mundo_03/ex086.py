"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta"""

matriz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor [{l+1}, {c+1}]: ')))

print(f'\033[1;m{"=" * 21}\033[m\n'
      f'{"MATRIZ EM PYTHON":^21}\n'
      f'\033[1;m{"=" * 21}\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'\033[1;m{"=" * 21}\033[m')
