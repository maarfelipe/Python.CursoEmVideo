"""Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108"""

from random import randint
import moeda

print(f'{"=" * 40}\n'
      f'Gerando um valor entre R$ 0 e R$ 100!')
num = randint(0, 100)
taxa = randint(0, 100)

formatar = randint(0, 1)
if formatar == 1:
    formatar = True
else:
    formatar = False
print(f'Apresentar valores formatados: {formatar}\n'
      f'{"=" * 40}')

print(f'\033[1;32m NÚMERO GERADO: {num} \033[m\n'
      f'Adicionando {taxa}% a {moeda.moeda(num)}: {moeda.aumentar(num, taxa, formatar)}\n'
      f'Retirando {taxa}% de {moeda.moeda(num)}: {moeda.diminuir(num, taxa, formatar)}\n'
      f'Dobro de {moeda.moeda(num)}: {moeda.dobro(num, formatar)}\n'
      f'Metade de {moeda.moeda(num)}: {moeda.metade(num, formatar)}\n'
      f'\033[1;31m FIM DA EXECUÇÃO! \033[m')
