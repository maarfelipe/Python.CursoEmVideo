"""Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa num dicionário e todos os dicionários numa lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

listaGeral = []
pessoas = {}
somaIdade = mediaIdade = 0

while True:
    print('=' * 30)
    pessoas['NOME'] = str(input('Nome: ')).capitalize().strip()
    while True:
        pessoas['SEXO'] = str(input('Sexo: [F/M] ')).upper().strip()[0]
        if pessoas['SEXO'] in 'MF':
            break
        print('\033[;1;31mERRO!\033[m Digite somente F ou M!')
    pessoas['IDADE'] = int(input('Idade: '))
    somaIdade += pessoas['IDADE']

    listaGeral.append(pessoas.copy())

    while True:
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('\033[;1;31mERRO!\033[m Digite somente S ou N!')
    if stop in 'N':
        print('=' * 30)
        break

mediaIdade = somaIdade / len(listaGeral)

print(f'Quantas pessoas foram cadastradas: {len(listaGeral)}\n'
      f'A média de idade: {mediaIdade:.1f}\n'
      f'Uma lista com as mulheres:', end=' ')
for p in listaGeral:
    if p['SEXO'] == 'F':
        print(p["NOME"], end=' ')
print(f'\nUma lista de pessoas com idade acima da média:')
for p in listaGeral:
    if p['IDADE'] >= mediaIdade:
        for k, v in p.items():
            print(f'{k}: {v}', end=' ')
        print()