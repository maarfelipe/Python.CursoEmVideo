"""Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit"""

celsius = float(input('Digite a temperatura em Celsius: '))

print(f'{celsius}ºC convertido para Fahrenheit é {(celsius * 1.8) + 32:.1f}ºF')
