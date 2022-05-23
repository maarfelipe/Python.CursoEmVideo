def aumentar(preco=0, taxa=0):
    res = preco + (preco * taxa / 100)
    return moeda(res)


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa / 100)
    return moeda(res)


def dobro(preco=0):
    res = preco * 2
    return moeda(res)


def metade(preco=0, formatar=False):
    res = preco / 2
    return moeda(res)


def moeda(preco=0):
    return f'R$ {preco:.2f}'.replace('.', ',')


def resumo(preco=0, taxa=0, ):
    print(f'\033[1;32m NÚMERO GERADO: {preco} \033[m\n'
          f'Adicionando {taxa}% a {moeda(preco)}: {aumentar(preco, taxa)}\n'
          f'Retirando {taxa}% de {moeda(preco)}: \t{diminuir(preco, taxa)}\n'
          f'Dobro de {moeda(preco)}: \t\t\t{dobro(preco)}\n'
          f'Metade de {moeda(preco)}: \t\t{metade(preco)}\n'
          f'\033[1;31m FIM DA EXECUÇÃO! \033[m')

