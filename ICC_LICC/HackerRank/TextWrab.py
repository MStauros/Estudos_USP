entrada_string = input()
entrada_tam = int(input())
tam = len(entrada_string)


conca = ""
for a in range(len(entrada_string)):
    for i in range(entrada_tam):
        conca += entrada_string

print(conca)