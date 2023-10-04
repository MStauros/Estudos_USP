#Marcos Santos ICC Estatística Arquivo CSV

"""
menor
maior
medglob
media <ano_inicial> <ano_final>
meddec <ano_inicial>
varini
"""
with open("dados.csv", "r") as a:
    resultado = []
    for i in a:
        dados = i.split(",")
        resultado.append([int(dados[0]),float(dados[1])])

entrada = input()

def cal_menor(dados):
    atual = dados[0]
    for i, k in enumerate(dados):
        if atual[1] > k[1]:
            atual = k
    return atual

def cal_maior(dados):
    atual = dados[0]
    for i, k in enumerate(dados):
        if atual[1] < k[1]:
            atual = k

    return atual

def cal_medglob(dados): 
    for i,k in enumerate(dados):
        dados_totais = k[1]
    valor_soma = sum(dados_totais)
    mediaglob = valor_soma / len(dados_totais)

    return mediaglob

def cal_med(dados, inicio, fim):
    tabela = []
    for i,k in enumerate(dados):
        if dados[i][0] >= inicio:
                if dados[i][0] <= fim:
                    tabela.append(k[1])
    tabela_soma = sum(tabela)
    media = tabela_soma / len(tabela_soma)

    return media

def calc_meddec(dados, inicial):
    tabela = []
    count = 0
    for i,k in enumerate(dados):
        if dados[i][0] >= inicial:
            if count <= 9:
                tabela.append(k[1])
                count += 1
    tabela_soma = sum(tabela)
    media_dec = tabela_soma / len(tabela_soma)

    return media_dec

def calc_varini(dados):
    inicial = dados[0][1]
    lista = []

    for i,k in enumerate(dados):
        lista.append(inicial - k[1])

    return lista


if entrada == "menor":
    faz_menor= cal_menor(resultado)
    print(f"{faz_menor[0]} {faz_menor[1]}")

elif entrada == "maior":
    faz_maior= cal_maior(resultado)
    print(f"{faz_maior[0]} {faz_maior[1]}")
elif entrada == "medglob":
    faz_medglob= cal_medglob(resultado)
    print(faz_medglob)
elif entrada == "media":
    data_inicio = int(input())
    data_final = int(input())
    print(cal_med(resultado, data_inicio, data_final))

elif entrada == "meddec":
    data_decada = input()
    print(calc_meddec(resultado, data_decada))
elif entrada == "varini":
    dados_varini = calc_varini(resultado)
    for p in range(len(resultado)):
        print(f"{dados_varini[p]}")