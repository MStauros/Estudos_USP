#Marcos Santos LICC Estatística

entrada_dia = int(input())
entrada_mes = int(input())
entrada_ano = int(input())
ano_atual = 2023

dia = False
mes = False
ano = False


if entrada_ano <= ano_atual and entrada_ano >= 0:
    ano = True
    if entrada_mes > 0 and entrada_mes <= 12:
        mes = True
        if entrada_dia > 0 and entrada_dia <= 31:
            if entrada_mes == 2:
                if entrada_dia <=28:
                    dia = True
            elif entrada_mes <= 7:
                if entrada_mes % 2 == 1:
                    dia = True
                else:
                    if entrada_dia <=30:
                        dia = True
            else:
                if entrada_mes % 2 == 0:
                    dia = True
                else:
                    if entrada_dia <=30:
                        dia = True

validacao = "OK" if ano is True and mes is True and dia is True else "ERRO"

print(validacao)