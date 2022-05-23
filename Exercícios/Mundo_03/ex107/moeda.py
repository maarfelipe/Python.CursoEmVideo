def aumentar(valor):
    from random import randint
    var = randint(0, 100)
    print(f'Adicionando {var}% a {valor}: {valor * ((var / 100) + 1):.1f}')


def diminuir(valor):
    from random import randint
    var = randint(0, 100)
    print(f'Retirando {var}% de {valor}: {((100 - var)*valor)/100:.1f}')


def dobro(valor):
    print(f'Dobro de {valor}: {valor * 2}')


def metade(valor):
    print(f'Metade de {valor}: {valor / 2}')