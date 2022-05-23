"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""

media = 0
for c in range(1, 3):
    var = float(input(f'Digite a {c}ª nota: '))
    media += var

print('=' * 12)
media = media / c
print(f'Média: {media:.1f}')

if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif 5 <= media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
print('=' * 12)

"""
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print('=' * 12)
media = (n1 + n2) / 2
print(f'Média: {media:.1f}')

if media < 5:
    print('\033[1;31mREPROVADO\033[m')
elif 5 <= media <= 6.9:
    print('\033[1;33mRECUPERAÇÃO\033[m')
else:
    print('\033[1;32mAPROVADO\033[m')
print('=' * 12)"""