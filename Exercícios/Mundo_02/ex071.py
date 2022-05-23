"""Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro),
o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""

saque = int(input('Valor do saque: R$ '))

cont50 = cont20 = cont10 = cont1 = 0
while saque != 0:
    if saque > 50:
        saque -= 50
        cont50 += 1
    elif saque > 20:
        saque -= 20
        cont20 += 1
    elif saque > 10:
        saque -= 10
        cont10 += 1
    else:
        saque -= 1
        cont1 += 1
print(f'''R$ 50 = {cont50}
R$ 20 = {cont20}
R$ 10 = {cont10}
R$  1 = {cont1}''')
