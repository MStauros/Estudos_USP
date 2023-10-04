#Marcos Santos ICC Estatística Condicional 2

import numpy as np

entrada_1 = map(int,input().split(" "))
entrada_2 = input().split(" ")


def define_retangulo(entrada):

    xy_1, la_1= ([int(entrada[0]), int(entrada[1])]), ([int(entrada[2]), int(entrada[3])])
    
    return xy_1, la_1

def define_matriz_numpy(lista_alt_lar):
    matriz = np.zeros((lista_alt_lar[1][1],lista_alt_lar[1][0]))

    return matriz

def define_matriz (lar, alt, valor):
    matriz = []
    for i in range(alt+1):
        linha = []
        for j in range(lar+1):
            linha.append(valor)
        matriz.append(linha)

    return matriz

def atribui_valores(matriz,retangulo):
    for i,a in enumerate(matriz):
        for j,b in enumerate(matriz[i]):
            matriz[i][j] = ([retangulo[0][0] + j, retangulo[0][1] + i])

    return matriz


def define_matriz_interseccao(matriz_1, matriz_2):
    interseccao = []
    for h,a in enumerate(matriz_1):
        linha = []
        for i,b in enumerate(a):
            for j,c in enumerate(matriz_2):
                for k,d in enumerate(c):
                    if d == b:
                        linha.append(d)
        if len(linha) != 0:
            interseccao.append(linha)

    return interseccao

def define_interseccao(interseccao):
    valores_inter = []

    valores_inter.append(interseccao[0][0][0])
    valores_inter.append(interseccao[0][0][1])
    x = interseccao[-1][-1][0] - interseccao[0][0][0]
    y = interseccao[-1][-1][1] - interseccao[0][0][1]

    #valores_inter.append(len(interseccao[0]))
    #valores_inter.append(len(interseccao))

    if len(interseccao) == 0:
        logica = False
    else:
        logica = True
    return valores_inter, logica, x, y


r_1 = list(define_retangulo(entrada_1))
r_2 = list(define_retangulo(entrada_2))

#print(f"o retangulo 1 é:\n{r_1}\n")
#print(f"o retangulo 2 é:\n{r_2}\n")

matriz_1 = define_matriz_numpy(r_1)
matriz_2 = define_matriz_numpy(r_2)


matriz_1 = define_matriz(r_1[1][0], r_1[1][1], 0)
matriz_2 = define_matriz(r_2[1][0], r_2[1][1], 0)

matriz_1 = atribui_valores(matriz_1, r_1)
matriz_2 = atribui_valores(matriz_2, r_2)

#print(f"a matriz do retangulo 1 é:\n{matriz_1}\n")
#print(f"a matriz do retangulo 2 é:\n{matriz_2}\n")

inter = list(define_matriz_interseccao(matriz_1, matriz_2))

#print(f"a matriz intersecção é:\n{inter}\n")

if len(inter) != 0:
    valores_inter = list(define_interseccao(inter))
    if valores_inter[1] == True:
        print(valores_inter)
        print(f"HIT: {valores_inter[0][0]} {valores_inter[0][1]} {valores_inter[2]} {valores_inter[3]}")
else: 
    print("MISS")