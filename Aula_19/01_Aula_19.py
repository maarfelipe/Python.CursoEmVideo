pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O dicionário completo é: {pessoas}\n'
      f'Para imprimir a key nome: {pessoas["nome"]}\n'
      f'Para imprimir a key idade: {pessoas["idade"]}\n'
      f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.\n')

print(f'Para imprimir somente as keys: {pessoas.keys()}\n'
      f'Para imprimir somente os values: {pessoas.values()}\n'
      f'Para imprimir keys e values: {pessoas.items()}\n')

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(f'O dicionário completo é: {pessoas}\n')

print('Para mostrar as keys: ', end='')
for k in pessoas.keys():
    print(k, end=' ')
print('\nPara mostrar os values: ', end='')
for v in pessoas.values():
    print(v, end=' ')
print('\nPara mostrar keys e values:')
for k, v in pessoas.items():
    print(f'{k} = {v}')

del pessoas['nome']
print(pessoas)
# =====================================================================================================================
brazil = []
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}

brazil.append(estado1)
brazil.append(estado2)

print(f'{estado1}\n'
      f'{estado2}\n'
      f'{brazil}\n')
print(brazil[0])
print(brazil[1])
print(brazil[0]['UF'])
print(brazil[1]['Sigla'])
# =====================================================================================================================
estado = {}
brazil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))

    brazil.append(estado.copy())

for e in brazil:
    for v in e.values():
        print(v, end=' ')
    print()
