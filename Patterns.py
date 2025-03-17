

#* Borda retangular

width = 30
height = 5

for i in range (height):
    if i == 0 or i == height - 1:
        print('*' * width)
    else:
        print('*' + ' ' * (width - 2) + '*')


#* Barra de progresso

import time

total = 100
for i in range(total + 1):
    barra = '[' + '#' * i + ' ' * (total - i) + ']'
    print(f'\r{barra} {i}%', end='')
    time.sleep(0.05)


#* Tabela Simples

dados = [
    ['Nome','Idade', 'Cidade'],
    ['Ana', '25', 'São Paulo'],
    ['Pedro', '30', 'Rio de Janeiro'],
    ['Maria', '22', 'Belo Horizonte']
]

for linha in dados:
    print ('|'.join (f'{item:<10}' for item in linha))
    if linha == dados[0]: #cabecalho
        print('-' * 33)


#* Padrão de grid

tamanho = 5
for i in range(tamanho):
    for j in range(tamanho):
        print(f'({i},{j})', end='')
    print()


#* Padrão de matriz

tamanho = 5
for i in range(tamanho):
    linha = ''
    for j in range(tamanho):
        if i == j:
            linha += '1 '
        else:
            linha += '0 '
    print(linha)


#* Histograma simples

dados = [4, 7, 2, 9, 5, 3]
for i, valor in enumerate(dados):
    print(f'Item {i}: {'#' * valor} ({valor})')


#* Padrào de bordas arredondadas

largura = 20
altura = 6

print('/' + '-' * (largura - 2) + '\\')
for i in range(altura - 2):
    print('|' + ' ' * (largura - 2) + '|')
print('\\' + '-' * (largura - 2) + '/')


#* Calendário Simples

dias = ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab']
print(' '.join(f'{dia:^5}' for dia in dias))
print('-' * 35)

dia_inicial = 3 #Começa na quarta-feira
dias_no_mes = 30
semana = ['     '] * 7
for dia in range(1, dias_no_mes + 1):
    indice = (dia_inicial + dia - 1) % 7
    semana[indice] = f'{dia:^5}'

    if indice == 6 or dia == dias_no_mes:
        print(' '.join(semana))
        semana = ['     '] * 7


