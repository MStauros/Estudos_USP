#Marcos Santos LICC Estatística

entrada_1 = input().split(" ")
entrada_2 = input().split(" ")


def define_retangulo(entrada: list[int]):

    xy_1, la_1= ([int(entrada[0]), int(entrada[1])]), ([int(entrada[2]), int(entrada[3])])

    return xy_1, la_1


def define_pontos_retangulo(retangulo):
    pontos = []
    pontos.append(retangulo[0])
    pontos.append([retangulo[0][0] + retangulo[1][0], retangulo[0][1]])
    pontos.append([pontos[1][0], pontos[1][1] + retangulo[1][1]])
    pontos.append([retangulo[0][0], retangulo[0][1] + retangulo[1][1]])

    return pontos

def define_logica_interseccao(pontos_r_1, pontos_r_2):
    y = True
    if pontos_r_2[0][0] > pontos_r_1[1][0]:
        y = False
    elif pontos_r_2[0][1] > pontos_r_1[2][1]:
        y = False
    elif pontos_r_2[1][0] < pontos_r_1[0][0]:
        y = False
    elif pontos_r_2[2][1] < pontos_r_1[0][1]:
        y = False

    return y


def interseccao(pontos_r_1, pontos_r_2):
    inter = []
    if pontos_r_2[0][0] > pontos_r_1[0][0]:
        inter.append(pontos_r_2[0][0])
    else:
        inter.append(pontos_r_1[0][0])

    if pontos_r_2[0][1] > pontos_r_1[0][1]:
        inter.append(pontos_r_2[0][1])
    else:
        inter.append(pontos_r_1[0][1])

    if pontos_r_2[1][0] > pontos_r_1[1][0]:
        inter.append(pontos_r_1[1][0] - inter[0])
    else:
        inter.append(pontos_r_2[1][0] - inter[0])

    if pontos_r_2[2][1] > pontos_r_1[2][1]:
        inter.append(pontos_r_1[2][1] - inter[1])
    else:
        inter.append(pontos_r_2[2][1] - inter[1])
    
    return inter



r_1 = list(define_retangulo(entrada_1))
r_2 = list(define_retangulo(entrada_2))

p1 = define_pontos_retangulo(r_1)


pontos_r_1 = define_pontos_retangulo(r_1)
pontos_r_2 = define_pontos_retangulo(r_2)


teste = define_logica_interseccao(pontos_r_1, pontos_r_2)

if teste is False:
    print("MISS")
else:
    inter = interseccao (pontos_r_1,pontos_r_2)
    print(f"HIT: {inter[0]} {inter[1]} {inter[2]} {inter[3]}")
