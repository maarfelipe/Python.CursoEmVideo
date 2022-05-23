"""Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato"""

dados = {}
gols = []

dados['NOME'] = str(input('Nome do jogador: ')).capitalize().strip()
partidas = int(input(f'Quantidade de partidas {dados["NOME"]} jogou: '))
for c in range(1, partidas+1):
    gols.append(int(input(f'    Quantos gols na {c}ª partida? ')))
dados['GOLS'] = gols[:]
dados['TOTAL'] = sum(gols)

print(f'{"=-" * 30}\n'
      f'{dados}\n'
      f'{"=-" * 30}')
for k, v in dados.items():
    print(f'{k} = {v}')
print(f'{"=-" * 30}\n'
      f'O jogador {dados["NOME"]} jogou {partidas} partidas:')
for p, v in enumerate(gols):
    print(f'Na partida {p+1}, fez {v} gols.')
print(f'Total de {dados["TOTAL"]} gols')
