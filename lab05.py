def Segunda(elemento):
    '''devolve o numero de letras minusculas em um endereço
    '''
    letra_l = list(elemento)
    n = 0
    for k in range(0, len(letra_l)):
        if letra_l[k].islower():
            n += 1
    return n
def Terca(elemento):
    '''devolve o numero de letras maiusculas em um endereço
    '''
    letra_l = list(elemento)
    n = 0
    for k in range(0, len(letra_l)):
        if letra_l[k].isupper():
            n += 1
    return n
def Quarta(elemento):
    '''devolve o numero de caracteres que são letras no endereço
    '''
    letra_l = list(elemento)
    n = 0
    for k in range(0, len(letra_l)):
        if letra_l[k].isalpha():
            n += 1
    return n
def Quinta(elemento):
    '''devolve o numero de palavras no endereço
    '''
    letra_l = list(elemento)
    n = 1
    for k in range(0, len(letra_l)):
        if letra_l[k] == " ":
            n += 1
    return n
def Sexta(elemento):
    '''devolve a soma dos valores ASCII dos caracteres de um endereço
    '''
    n = 0
    letra_l = list(elemento)
    for k in range(0, len(letra_l)):
       n1 = ord(letra_l[k])
       n += n1
    return n
entrada = input().split(" ")
dia = entrada[0]
N = int(entrada[1])
endereco_l = []
for i in range(N):
    endereco = input()
    endereco_l.append(endereco)
if dia == "Segunda":
    lista_ordenada = sorted(endereco_l, key=Segunda, reverse=False)
elif dia == "Terca":
    lista_ordenada = sorted(endereco_l, key=Terca, reverse=True)
elif dia == "Quarta":
    lista_ordenada = sorted(endereco_l, key=Quarta, reverse=False)
elif dia == "Quinta":
    lista_ordenada = sorted(endereco_l, key=Quinta, reverse=False)
else:
    lista_ordenada = sorted(endereco_l, key=Sexta, reverse=True)
for v in range(len(lista_ordenada)):
    print(lista_ordenada[v], end="\n")