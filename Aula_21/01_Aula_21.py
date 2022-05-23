def factorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
    return f


# Código Principal
"""n = int(input('Digite um número: '))
print(f'O factorial de {n} é {factorial(n)}')"""

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'Os resultados são: {f1}, {f2} e {f3}')
# =====================================================================================================================


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Código Principal
num = int(input('Digite um número: '))
if par(num):
    print('PAR')
else:
    print('ÍMPAR')
