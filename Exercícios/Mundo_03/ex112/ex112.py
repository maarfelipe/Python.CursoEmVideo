"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários"""

from random import randint
from utilidadesCeV import moeda, dado

num = dado.leiaDinheiro('Digite um valor: R$ ')
taxa = randint(0, 100)

moeda.resumo(num, taxa)
