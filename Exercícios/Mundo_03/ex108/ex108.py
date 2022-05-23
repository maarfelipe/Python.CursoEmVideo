"""Adapte o código do desafio #107, criando uma função adicional chamada moeda()
que consiga mostrar os números como um valor monetário formatado"""

from random import randint
import moeda

print('Gerando um valor entre R$ 0 e R$ 100!')
num = randint(0, 100)
taxa = randint(0, 100)

print(f'\033[1;32m NÚMERO GERADO: {num} \033[m\n'
      f'Adicionando {taxa}% a {moeda.moeda(num)}: {moeda.moeda(moeda.aumentar(num, taxa))}\n'
      f'Retirando {taxa}% de {moeda.moeda(num)}: {moeda.moeda(moeda.diminuir(num, taxa))}\n'
      f'Dobro de {moeda.moeda(num)}: {moeda.moeda(moeda.dobro(num))}\n'
      f'Metade de {moeda.moeda(num)}: {moeda.moeda(moeda.metade(num))}\n'
      f'\033[1;31m FIM DA EXECUÇÃO! \033[m')