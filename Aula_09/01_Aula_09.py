frase = ' Curso em Vídeo Python  '

# O print retornará o 3º valor da sentença: 'r'
print({frase[3]})

# O print retornará do 3º até o 12º valor: 'rso em Víd'
print(frase[3:13])

# O print mostrará no 2º valor até o final: 'urso em Vídeo Python  '
print(frase[2:])

# O print mostrará do início até o 12º valor: ' Curso em Víd'
print(frase[:13])

# O print retorna do 1º ao 14º valor, pulando 2 valores: 'Croe íe'
print(frase[1:15:2])

# O print retorna do 1º até o final da sentença, pulando de 2 em 2: 'Croe íe yhn '
print(frase[1::2])

# O print mostrará a sentença inteira pulando de 2 em 2: ' us mVdoPto '
print(frase[::2])

# O print mostra a primeira posição onde apareceu o caractére 'o': 3
print(frase.count('o'))

# O comando transforma a frase toda para maiúscula e mostra a primeira posição onde apareceu o caractére 'O': 3
print(frase.upper().count('O'))

# O comando mostra quantos caractéres foram utilizados na sentença, contando os espaços no começo e no final: 24
print(len(frase))

# O comando strip elimina os espaços desnecessários no início e no final da sentença: 21
print(len(frase.strip()))

# Replace altera nesta instância a sentença, mas não altera a sequência original: ' Curso em Vídeo Android  '
print(frase.replace('Python', 'Android'))

# Retorna True se 'Curso' estiver na sentença, e False caso não: True
print('Curso' in frase)

# Mostra a primeira posição em que 'Curso' aparece na sentença: 1
print(frase.find('Curso'))

# Caso find não encontre o que foi pedido, retornará valor negativo: -1
print(frase.find('vídeo'))

# Assim como upper(), lower() altera a sentença toda deixando tudo minúsculo, retornando a primeira posição do que foi solicitado: 10
print(frase.lower().find('vídeo'))

# Função split divide a sentença levando em consideração os espaços: 'Curso', 'em', 'Vídeo', 'Python'
dividido = frase.split()

# Dentro da sentença splitada, irá mostrar a palavra da posiçao 0: 'Curso'
print(dividido[0])

# Dentro da sentença splitada, irá mostrar o valor 3 da palavra na posição 2: 'e'
print(dividido[2][3])
