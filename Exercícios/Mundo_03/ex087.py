"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = [[], [], []]
spar = s3Col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor [{l+1}, {c+1}]: ')))

print(f'\033[1;m{"=" * 21}\033[m\n'
      f'{"MATRIZ EM PYTHON":^21}\n'
      f'\033[1;m{"=" * 21}\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]

    print()
print(f'\033[1;m{"=" * 21}\033[m')

print(f'A soma de todos os valores pares digitados: {spar}')
for l in range(0, 3):
    s3Col += matriz[l][2]
print(f'A soma dos valores da terceira coluna: {s3Col}')
for c in range(0 ,3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha: {maior}')
