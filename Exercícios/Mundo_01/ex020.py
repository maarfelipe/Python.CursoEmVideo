"""O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada"""


from random import shuffle
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem de apresentação dos alunos será: {lista}')



from random import shuffle
lista = []
for c in range(1, 5):
    temp = str(input(f'Digite o nome do {c}º aluno: '))
    lista.append(temp)
shuffle(lista)
print(f'A ordem de apresentação será: {lista}')