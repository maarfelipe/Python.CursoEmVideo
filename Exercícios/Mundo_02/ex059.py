"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

print(f'{"=" * 30}\n'
      f'\033[1;40m{"EX 059 - MUNDO 2":^30}\033[m\n'
      f'{"=" * 30}')

lista = []
for c in range(1, 3):
    temp = int(input(f'{c}º valor: '))
    lista.append(temp)

operacao = 0
while operacao != 5:
    operacao = int(input(f'{"=" * 30}\n'
                         f'\033[1;40m{"OPERAÇÕES":^30}\033[m\n'
                         f'{"=" * 30}\n'
                         f'[ 1 ] Somar\n'
                         f'[ 2 ] Multiplicar\n'
                         f'[ 3 ] Maior\n'
                         f'[ 4 ] Novos números\n'
                         f'[ 5 ] Sair do programa\n'
                         f'Escolha o comando desejado: '))
    if operacao == 1:
        print(f'{"=" * 30}\n'
              f'\033[1;40m{"SOMA":^30}\033[m\n'
              f'{"=" * 30}\n'
              f'{lista[0]} + {lista[1]} = {lista[0] + lista[1]}')
    elif operacao == 2:
        print(f'{"=" * 30}\n'
              f'\033[1;40m{"MULTIPLICACAO":^30}\033[m\n'
              f'{"=" * 30}\n'
              f'{lista[0]} * {lista[1]} = {lista[0] * lista[1]}')
    elif operacao == 3:
        print(f'{"=" * 30}\n'
              f'\033[1;40m{"MAIOR VALOR":^30}\033[m\n'
              f'{"=" * 30}')
        if lista[0] > lista[1]:
            print(f'Maior: {lista[0]}')
        else:
            print(f'Maior: {lista[1]}')
    elif operacao == 4:
        print(f'{"=" * 30}\n'
              f'\033[1;40m{"NOVOS VALORES":^30}\033[m\n'
              f'{"=" * 30}')
        lista.clear()
        for c in range(1, 3):
            temp = int(input(f'{c}º valor: '))
            lista.append(temp)
    elif operacao == 5:
        print(f'{"=" * 30}\n'
              f'\033[1;40m{"ENCERRANDO PROGRAMA":^30}\033[m\n'
              f'{"=" * 30}')
    else:
        print(f'{"=" * 30}\n'
              f'\033[1;30;41m{"COMANDO INVÁLIDO":^30}\033[m')
print('FIM')
