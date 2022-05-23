"""Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

contMaior18 = contM = contFMen20 = 0
while True:
    print('=' * 26)
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sexo [F/M]: ')).upper().strip()[0]

    age = int(input('Idade: '))

    if age > 18:
        contMaior18 += 1

    if sex in 'M':
        contM += 1

    if sex in 'F' and age < 20:
        contFMen20 += 1

    print('=' * 26)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continua? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print(f'Quantas pessoas tem mais de 18 anos: {contMaior18}\n'
      f'Quantos homens foram cadastrados: {contM}\n'
      f'Quantas mulheres tem menos de 20 anos: {contFMen20}')
