entrada_tam = int(input())
entrada_pontos = list(map(int,input().split()))

negativos = 0
positivos = 0
zeros = 0
for i in range(entrada_tam):
    if entrada_pontos[i] < 0:
        negativos += 1
    elif entrada_pontos[i] > 0:
        positivos += 1
    else:
        zeros += 1

pro_neg = negativos / entrada_tam
pro_pos = positivos / entrada_tam
pro_zer = zeros / entrada_tam

print(pro_neg,"\n",pro_pos,"\n",pro_zer)