"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado."""

valor = int(input('Valor do imóvel: R$'))
salario = int(input('Salário do comprador: R$'))
tempo = int(input('Quantos anos gostaria de pagar: '))

parcela = valor / (tempo * 12)

if parcela > (salario * 0.30):
    print(f'\033[1;41mEMPRÉSTIMO NEGADO!!!\033[m\n'
          f'O valor da parcela é R${parcela:.2f} e equivale a mais de 30% do salário do comprador.')
else:
    print(f'\033[1;42mEMPRÉSTIMO APROVADO!!!\033[m\n'
          f'O valor da parcela será R${parcela:.2f} e equivale {(100 * parcela) / salario:.1f}% do salário do comprador.')