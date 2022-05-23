def aumentar(preco=0, taxa=0, formatar=False):
    res = preco + (preco * taxa / 100)
    return res if formatar is False else moeda(res)


def diminuir(preco=0, taxa=0, formatar=False):
    res = preco - (preco * taxa / 100)
    return res if formatar is False else moeda(res)


def dobro(preco=0, formatar=False):
    res = preco * 2
    return res if not formatar else moeda(res)


def metade(preco=0, formatar=False):
    res = preco / 2
    return res if not formatar else moeda(res)


def moeda(preco=0):
    return f'R$ {preco:.2f}'.replace('.', ',')

