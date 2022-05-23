""" Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais"""

palavras = ('aprenda', 'programar', 'curso', 'python', 'programador')

for c in palavras:
    print(f'\nNa palava {c.upper()} temos as vogais: ', end='')
    for vogais in c:
        if vogais in 'aeiou':
            print(vogais.upper(), end=' ')
