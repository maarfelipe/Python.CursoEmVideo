"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar"""

from datetime import datetime
anoAtual = datetime.now().year

dados = {}

dados['NOME'] = str(input('Digite o nome: ')).capitalize().strip()
nascimento = int(input('Ano de nascimento: '))
dados['IDADE'] = anoAtual - nascimento
dados['CTPS'] = int(input('CTPS [Pressione 0 caso não tenha]: '))

if dados['CTPS'] != 0:
    dados['CONTRATACAO'] = int(input('Ano de contratação: '))
    dados['SALARIO: R$'] = int(input('Salário: R$ '))
    dados['APOSENTADORIA'] = (dados['CONTRATACAO'] + 35) - nascimento

print(f'{"=" * 30}')
for k, v in dados.items():
    print(f'{k}: {v}')
print(f'{"=" * 30}')
