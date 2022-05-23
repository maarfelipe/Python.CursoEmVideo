"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente"""

listaGeral = []
cont = 1

while True:
    print(f'{"=" * 27}\n'
          f'{f"{cont}º ALUNO":^27}\n'
          f'{"=" * 27}')
    nome = (str(input('Nome: ')).capitalize())
    nota1 = (float(input('1ª nota: ')))
    nota2 = (float(input('2ª nota: ')))
    media = (nota1 + nota2) / 2
    listaGeral.append([nome, [nota1, nota2], media])
    cont += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input(f'{"=" * 27}\n'
                              f'Deseja continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break

print(f'{"=" * 27}\n'
      f'{"DADOS GERAIS":^27}\n'
      f'{"=" * 27}\n'
      f'{"Nº":<5}{"Nome":<16}Media\n'
      f'{"=" * 27}')
for pos, val in enumerate(listaGeral):
    print(f'{pos:<5}{val[0]:<16}{val[2]:.1f}')
print(f'{"=" * 27}')

while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 quit) '))

    if aluno == 999:
        break

    print(f'As notas de {listaGeral[aluno][0]} foram: {listaGeral[aluno][1]}\n'
          f'{"=" * 27}')

print('FIM DA EXECUÇÃO')
