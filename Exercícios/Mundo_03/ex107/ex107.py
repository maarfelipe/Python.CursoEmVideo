"""Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções"""

from random import randint
from time import sleep
import moeda

print('Gerando um valor entre 0 e 100!')
num = randint(0, 100)
sleep(0.8)
print(f'\033[1;32m Número gerado: {num} \033[m')
sleep(0.8)
moeda.aumentar(num)
sleep(0.8)
moeda.diminuir(num)
sleep(0.8)
moeda.dobro(num)
sleep(0.8)
moeda.metade(num)
sleep(0.8)
print(f'\033[1;31m FIM DA EXECUÇÃO! \033[m')

