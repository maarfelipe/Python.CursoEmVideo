"""Faça um mini-sistema que utilize o Interactive Help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores"""


def ajuda(comando):
    help(comando)


def titulo(msg, cor=0):
    c = ['\033[m',  # 0 - Padrão
         '\033[1;41m',  # 1 - Vermelho
         '\033[1;43m']  # 2 - Amarelo

    tam = len(msg) + 6
    print(f'{c[cor]}{"=" * tam}{c[0]}\n'
          f'{c[cor]}{msg:^{tam}}{c[0]}\n'
          f'{c[cor]}{"=" * tam}{c[0]}')


# Código Principal
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Função ou Biblioteta: ')).strip()
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FIM DA EXECUÇÃO ... VOLTE SEMPRE!', 2)