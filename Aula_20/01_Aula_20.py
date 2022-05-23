def soma(a, b):
    print(f'A = {a} // B = {b}')
    s = a + b
    print(f'A soma vale {s}\n'
          f'{"=" * 20}')


# Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=4, a=1)


# ======================================================================================================================
def contador(*num):
    for v in num:
        print(v, end=' ')
    print()

    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# ======================================================================================================================
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


# ======================================================================================================================
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
# ======================================================================================================================
