#Resolução´
import random
import math

entrada = int(input())
#entrada = random.randint(1, 10)
entrada_2 = [input() for i in range(entrada)]

def lista_inicial(tam):
    lista = [0 for i in range(tam)]
    
    return lista

def atribui_valores(tam, valores):
    a= 0
    while a in range(len(valores)):
        tam[a] = float(valores[a])
        a += 1

    return tam

tam_lista = lista_inicial(entrada)
lista_valores = atribui_valores(tam_lista, entrada_2)

#Exiba o menor valor da lista (maior entre todos os valores lidos e que estão na lista).

valor_minimo =min(lista_valores)

#Exiba o maior valor da lista.

valor_maximo = max(lista_valores)

#Exiba a “amplitude” dos valores, ou seja, o maior valor menos o menor valor da lista.

valor_amplitude = valor_maximo - valor_minimo


#Exiba a soma de todos os valores da lista (somatório).

valor_soma = sum(lista_valores)

#Exiba a média simples dos valores da lista.

valor_media = valor_soma / len(lista_valores)

#Exiba o desvio padrão dos valores da lista.

somatoria = [(n - valor_media) ** 2 for i,n in enumerate(lista_valores)]

valor_desvio = (sum(somatoria)/len(lista_valores)) **(1/2)

#Exiba a variância dos valores da lista (é o desvio padrão ao quadrado, ou, sem a raiz do DP)

valor_variancia = valor_desvio ** 2

print(f"{valor_minimo:.3f}")
print(f"{valor_maximo:.3f}")
print(f"{valor_amplitude:.3f}")
print(f"{valor_soma:.3f}")
print(f"{valor_media:.3f}")
print(f"{valor_desvio:.3f}")
print(f"{valor_variancia:.3f}")

