entrada_pontos = list(map(int,input().split()))

for i, j in enumerate(entrada_pontos):
    if entrada_pontos[i] > 40:
        prox_div_5 = ((j / 5) +1) * 5

        if prox_div_5 - j < 3:
            entrada_pontos[i] = j

print(entrada_pontos)
