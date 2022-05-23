"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos"""

media = ihmv = cont = 0
nhmv = ''
for c in range(1, 5):
    print(f'{f" {c}ª PESSOA  " :-^21}')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()[0]

    media += idade

    if 'M' in sexo:
        if c == 1:
            nhmv = nome
            ihmv = idade
        elif idade > ihmv:
            nhmv = nome
            ihmv = idade

    if 'F' in sexo:
        if idade < 20:
            cont += 1

print(f'A média de idade do grupo é {media / c:.1f} anos.\n'
      f'Qual é o nome do homem mais velho: {nhmv} com {ihmv} anos.\n'
      f'Quantas mulheres têm menos de 20 anos: {cont} mulheres.')
