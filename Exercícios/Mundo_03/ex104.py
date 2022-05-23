"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""


def leiaInt(msg):
    validador = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            validador = True
        else:
            print('\033[1;31mERRO! Digite número inteiro!\033[m')

        if validador:
            break
    return valor


# Código Principal
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}.')
