import math
#importando a biblioteca math

ent_raio = float(input()) #recebendo str e convertendo para float

if ent_raio > 0:
    var_area = math.pi * ent_raio ** 2 #aplicando fórmula matemática
    var_perim = 2 * math.pi * ent_raio #aplicando fórmula matemática

    print(f"{var_area:.2f}") #imprimindo o valor da área formatando seu resultado com o format "f" e a estrutura :.2f que indica a limitação das casas decimais
    print(f"{var_perim:.2f}") #imprimindo o valor da área formatando seu resultado com o format "f" e a estrutura :.2f que indica a limitação das casas decimais
else:
    print("Nao existe circunferencia de raio negativo!")