
# *Linha de 10 (*)
size = 10

for i in range(size):
    print('*')


#* retângulo 10x10
size = 10

for i in range(size):
    print('*' * size)


#* de pé na esquerda
size = 10

for i in range(size):
    print('*' * (i+1))

#* invertido na esquerda
size = 10

for i in range(size):
    count = size - i
    print('*' * count)

#* de pé na direita

size = 10

for i in range(size):
    count = size - (i + 1)
    print (' ' * count + "*" * (i + 1))

#* invertido na direita

size = 10

for i in range(size):
    count = size - i
    spaces = i
    print(' ' * spaces + '*' * count)


#* Piramide completa

size = 10

for i in range(size):
    #calcula strelas para essa linha
    stars = 2 * i + 1

    #calcula os espaços para a centro da estrela
    spaces = size - i - 1

    #imprime
    print(' ' * spaces + '*' * stars)


