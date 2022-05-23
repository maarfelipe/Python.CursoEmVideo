def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mERRO! Valor não informado!\033[m')
            return 'Nenhum número foi digitado'
        else:
            return num


def linha(tam=42):
    return '=' * tam


def cabecalho(txt):
    print(f'{linha()}\n'
          f'{txt.center(42)}\n'
          f'{linha()}')


def menu(lista):
    cabecalho(f'MENU PRINCIPAL')
    for key, val in enumerate(lista):
        print(f'\033[1;33m{key+1} - \033[34m{val}\033[m')
    print(linha())
    opc = leiaInt('Sua opção: ')
    return opc