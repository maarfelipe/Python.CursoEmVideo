"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite"""

velocidade = int(input('Qual a velocidade do automóvel: '))

print('Velocidade máxima permitida é 80km/h ... ')
if velocidade <= 80:
    print(f'Seu automóvel está a {velocidade}km/h. Dirija com segurança!')
else:
    print(f'Seu automóvel está a {velocidade}Km/h e você excedeu o limite de velocidade!\n'
          f'Sua multa é de R${(velocidade - 80) * 7:.2f}!')
