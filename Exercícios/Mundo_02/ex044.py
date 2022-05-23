"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

preco = int(input('Valor da compra: R$ '))
pagamento = int(input(f'{"=" * 46}\n'
                      f'\033[1;30;45m{"FORMA DE PAGAMENTO":^46}\033[m\n'
                      f'{"=" * 46}\n'
                      '[ 1 ] à vista dinheiro/cheque: 10% de desconto\n'
                      '[ 2 ] à vista no cartão: 5% de desconto\n'
                      '[ 3 ] em até 2x no cartão: preço formal\n'
                      '[ 4 ] 3x ou mais no cartão: 20% de juros\n'
                      'Digite a forma de pagamento escolhida: '))
print(f'{"=" * 46}')

print(f'O valor da compra é R$ {preco:.2f} e a forma de pagamento escolhida foi: ', end='')
if pagamento == 1:
    print(f'à vista dinheiro/cheque com 10% de desconto\n'
          f'O valor final da compra será: R$ {preco * 0.9:.2f}')
elif pagamento == 2:
    print(f'à vista no cartão com 5% de desconto\n'
          f'O valor final da compra será: R$ {preco * 0.95:.2f}')
elif pagamento == 3:
    print(f'até 2x no cartão, preço formal sem desconto')
elif pagamento == 4:
    print(f'3x ou mais no cartão com 20% de juros\n'
          f'O valor final da compra será: R$ {preco * 1.2:.2f}')
else:
    print('\033[1;41mOpção inválida. Comece novamente!!!\033[m')

