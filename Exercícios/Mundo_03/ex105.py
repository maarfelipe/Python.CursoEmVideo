"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor."""


def notas(valores, situacao=False):
    """
    -> Através de um dicionário, faz validação de itens que estavam em lista
    :param valores: Lê os valores de uma lista
    :param situacao: Mostra em escala I, R, B, MB, O a situação da média da sala
    :return: Mostra valores em formato lista de todos os dados
    """
    r = {'Quantidade de notas': len(valores),
         'A maior nota': max(valores),
         'A menor nota': min(valores),
         'A média da turma': sum(valores) / len(valores)}

    if situacao:
        if r['A média da turma'] >= 9:
            r['Situação'] = 'ÓTIMO'
        elif r['A média da turma'] >= 7.5:
            r['Situação'] = 'MUITO BOM'
        elif r['A média da turma'] >= 6:
            r['Situação'] = 'BOM'
        elif r['A média da turma'] >= 4:
            r['Situação'] = 'RUIM'
        else:
            r['Situação'] = 'INSUFICIENTE'

    for k, v in r.items():
        print(f'{k}: {v}')


# Código Principal
lista = []
cont = 0
while True:
    cont += 1
    lista.append(float(input(f'Digite a {cont}ª nota: ')))

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if stop == 'N':
        break

while True:
    situacao = ' '
    while situacao not in 'SN':
        situacao = str(input('Apresentar situação? [S/N] ')).upper().strip()[0]
    if situacao == 'S':
        situacao = True
    else:
        situacao = False
    break

notas(lista, situacao)
