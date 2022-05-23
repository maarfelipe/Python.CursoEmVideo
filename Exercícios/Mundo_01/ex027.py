"Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente"

nome = str(input('Digite um nome completo: ')).strip().title().split()
print(f'Primeiro: {nome[0]}\n'
      f'Último: {nome[len(nome)-1]}')
