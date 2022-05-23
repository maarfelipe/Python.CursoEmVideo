"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente"""

valores = []

while True:
    temp = int(input(f'Digite um valor: '))
    if temp not in valores:
        valores.append(temp)
    else:
        print('Valor já informado, tente novamente!')

    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if stop in 'N':
        break

valores.sort()
print(f'Valores: {valores}')
