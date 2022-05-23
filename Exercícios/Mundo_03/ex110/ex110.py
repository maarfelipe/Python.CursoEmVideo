"""Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(),
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui"""

from random import randint
import moeda

print(f'Gerando um valor entre R$ 0 e R$ 100!')
num = randint(0, 100)
taxa = randint(0, 100)

moeda.resumo(num, taxa)
