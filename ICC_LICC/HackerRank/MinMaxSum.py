lista = list(map(int,input().split()))

lista_cres = lista.sort()
lista_decr = lista.sort(reverse=True)

print(lista_cres)
print(lista_decr)
'''
soma_min = 0
soma_max = 0
for i in range(4):
    soma_min += lista_cres[i]
    soma_max += lista_decr[i]

print(soma_min,soma_max)'''