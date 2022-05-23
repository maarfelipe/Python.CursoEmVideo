"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Digite o valor do salário: R$'))

if salario <= 1250:
    print(f'Para os salários inferiores ou iguais a R$1250, o aumento é de 15%: R${salario * 1.15:.2f}')
else:
    print(f'Para salários superiores a R$1250, um aumento de 10%: R${salario * 1.10:.2f}')