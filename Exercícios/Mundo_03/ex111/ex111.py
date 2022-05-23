"""Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando"""

from random import randint
from utilidadesCeV import moeda

print(f'Gerando um valor entre R$ 0 e R$ 100!')
num = randint(0, 100)
taxa = randint(0, 100)

moeda.resumo(num, taxa)
