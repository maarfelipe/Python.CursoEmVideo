try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except (ValueError, TypeError):
    print('Tipos de dados inválidos.')
except ZeroDivisionError:
    print('Divisão por zero é inválida')
except KeyboardInterrupt:
    print('Dados não informados')
except Exception as erro:
    print(f'Problema encotrado: {erro}')

else:
    print(f'O resultado é {r:.1f}')
finally:
    print('EXECUTAÇÃO FINALIZADA')
