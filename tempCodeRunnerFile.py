dados = [3, 7, 2, 9, 4, 8, 5]
altura_max = 10
largura = len(dados)

for y in range(altura_max, 0, -1):
    linha = ""
    for valor in dados:
        if valor >= y:
            linha += "| "
        else:
            linha += "  "
    print(linha)

print("-" * (largura * 2))
print(" ".join(str(i) for i in range(largura)))