"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela"""

boletim = {}

boletim['Nome'] = str(input('Nome do aluno: ')).capitalize().strip()
boletim['Média'] = float(input('Média: '))

if boletim["Média"] >= 7:
    boletim["Situação"] = 'Aprovado'
elif boletim["Média"] >= 5:
    boletim["Situação"] = 'Recuperação'
else:
    boletim["Situação"] = 'Reprovado'

print(f'{"=" * 30}')
for k, v in boletim.items():
    print(f'{k}: {v}')
print(f'{"=" * 30}')
