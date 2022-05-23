"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta."""

"""expressao = str(input('Digite a expressão: '))
lista = []

for symbol in expressao:
    if symbol == '(':
        lista.append('(')
    elif symbol == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\033[1;42mEXPRESSÃO VÁLIDA\033[m')
else:
    print('\033[1;41mEXPRESSÃO INVÁLIDA\033[m')"""

expressao = str(input('Digite a expressão: '))

parenteses = 0
for symbol in expressao:
    if symbol == '(':
        parenteses += 1
    elif symbol == ')':
        parenteses -= 1

    if parenteses < 0:
        break

if parenteses == 0:
    print('\033[1;42mEXPRESSÃO VÁLIDA\033[m')
else:
    print('\033[1;41mEXPRESSÃO INVÁLIDA\033[m')
