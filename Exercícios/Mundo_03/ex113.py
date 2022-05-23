"""Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade"""


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Valor não informado!\033[m')
            return 'Nenhum número foi digitado'
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = input(msg)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número real válido!\033[m')
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Valor não informado!\033[m')
            return 0
        else:
            return num


# Código Principal
inteiro = leiaInt('Digite um número inteiro: ')
flutuante = leiaFloat('Digite um número real: ')
print(f'Número Inteiro: {inteiro}\n'
      f'Número Real: {flutuante}')
