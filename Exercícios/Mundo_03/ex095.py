""" Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador"""

listaGeral = []
dados = {}
gols = []

while True:
    print('=' * 38)
    dados['NOME'] = str(input('Nome do jogador: ')).capitalize().strip()
    partidas = int(input(f'Quantidade de partidas {dados["NOME"]} jogou: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'    Quantos gols na {c}ª partida? ')))
        dados['GOLS'] = gols[:]
        dados['TOTAL'] = sum(gols)

    listaGeral.append(dados.copy())
    gols.clear()

    while True:
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        if stop in 'SN':
            break
        print('\033[;1;31mERRO!\033[m Digite somente S ou N!')
    if stop in 'N':
        break

print(f'{"=" * 38}\n'
      f'{"CÓD.":<5}', end='')
for k in dados.keys():
    print(f'{k:<14}', end='')
print(f'\n{"=" * 38}')
for p, v in enumerate(listaGeral):
    print(f'{p:<5}', end='')
    for c in v.values():
        print(f'{str(c):<14}', end='')
    print()
print(f'{"=" * 38}')

while True:
    busca = int(input('Digite o CÓD. para mostrar os dados do jogador (999 quit): '))

    if busca == 999:
        break

    if busca >= len(listaGeral):
        print('\033[;1;31mERRO!\033[m CÓD. INVÁLIDO!')
    else:
        print(f'Informaçõs do Jogador {listaGeral[busca]["NOME"]}')
        for pos, val in enumerate(listaGeral[busca]['GOLS']):
            print(f'    No jogo {pos+1} fez {val} gols')
