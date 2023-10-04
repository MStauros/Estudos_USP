#Marcos Santos ICC Estatística Astronalta Perdido 3

import numpy as np

#primeiro separar o input em 2: tamanho da matriz e posição do astronauta
tam_matriz, posi_astro = map(int,input().split(" "))


#Definindo todos os elementos da matriz com zeros
def define_matriz_numpy(tam_matriz):

    matriz = np.zeros((tam_matriz,tam_matriz))

    return matriz


#Atribuindo valores nas posições da matriz com suas coordenadas
def atribui_valores(matriz):
    lista_zeros = matriz.tolist()
    for i in range(matriz.shape[1]):
        for j in range(matriz.shape[0]):
            lista_zeros[i][j] = ([i, j])

    return lista_zeros

#Chama a função de criar a matriz
matriz_zeros = define_matriz_numpy(tam_matriz)

#Chama a função de atribuir valores a matriz
matriz = atribui_valores(matriz_zeros)

print(f"Matriz {matriz} \n")
#validando se o astronauta já saiu
if posi_astro > tam_matriz**2:
    print(f"O astronauta ja saiu em missao ha {posi_astro - (tam_matriz)**2} chamadas.")


#Se não saiu, agora avaliar se está para sair
elif posi_astro == tam_matriz**2:
    if posi_astro % 2 == 0:
        calculo_y = int(tam_matriz / 2)
        calculo_x = (int(tam_matriz / 2) -1)


        print(f"O astronauta esta na posicao: {matriz[calculo_x][calculo_y][0]} {matriz[calculo_x][calculo_y][1]}\nPreste atencao, astronauta, chegou a sua vez!")
    else:
        calculo_x_y = int((tam_matriz / 2) - 0.5)

        print(f"O astronauta esta na posicao: {matriz[calculo_x_y][calculo_x_y][0]} {matriz[calculo_x_y][calculo_x_y][1]}\nPreste atencao, astronauta, chegou a sua vez!")

#Então agora é encontrar sua posição na fila e quantas chamadas faltam
else:
    print(f"O astronauta esta na posicao: {0} {0}\nAinda faltam {tam_matriz**2-posi_astro} chamadas para a sua vez!")
