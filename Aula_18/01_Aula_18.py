teste = []
teste.append('Gustavo')
teste.append('40')
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera)
print(galera[0])
print(galera[0][0])
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos.')

galera = []
dados = []
totalMaior = totalMenor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade!')
        totalMaior += 1
    else:
        print(f'{pessoa[0]} é menor de idade!')
        totalMenor += 1
print(f'Temos {totalMaior} pessoas maiores de idade e {totalMenor} menores.')
