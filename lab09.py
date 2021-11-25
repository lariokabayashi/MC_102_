<<<<<<< HEAD
def leia(ordem):
    '''
    transforma entrada em matriz
    '''
    matriz = []
    for i in range(ordem):
        matriz.append([])
        linha = input().split(" ")
        for j in range(ordem): 
            matriz[i].append(int(linha[j]))
    return(matriz)
def matriz_em_lista(A):
    '''
    transforma matriz em lista (lineariza)
    '''
    lista = []
    for i in range (len(A)):
        for j in range(len(A)):
            lista.append(A[i][j])
    return(lista)
def info_elem_iguais(maior, menor):
    '''
    encontra a linha e a coluna ,respectiva à matriz menor, dos elementos comuns às matrizes 
    encontra também quem é os elementos
    '''
    lista_elem_iguais = []
    linha_dos_iguais = []
    coluna_dos_iguais = []
    l_menor = matriz_em_lista(menor)
    l_maior = matriz_em_lista(maior)
    set_maior = set(l_maior)
    set_menor = set(l_menor)
    elem_iguais = set_maior.intersection(set_menor) #encontra intersecção de M com N
    lista_elem_iguais = list(elem_iguais)
    for i in range(len(lista_elem_iguais)):
        y = l_menor.index(lista_elem_iguais[i]) #posição do elem igual na lista
        linha_dos_iguais.append(y // len(menor)) #descobre i,j dos elementos que são comuns a M e N através das formulas de deslinearização
        coluna_dos_iguais.append(y % len(menor))
    return([lista_elem_iguais, linha_dos_iguais, coluna_dos_iguais])

def encontra_p_q(maior,menor):
    '''
    encontra o numero de linhas e colunas da supermatriz (matriz que é a sobreposição de M e N)
    '''
    lista_linhas = info_elem_comuns[1]
    lista_col = info_elem_comuns[2]
    p = len(maior) + (len(menor) - len(list(set(lista_linhas)))) #a sobreposição de matrizes adiciona o numero de linhas e colunas dos elementos, que não são comuns à M e N, da matriz menor à matriz maior 
    q = len(maior) + (len(menor) - len(list(set(lista_col))))   
    return(f'{p} x {q}')

lista_ordens = input().split(" ")
m = int(lista_ordens[0])
n = int(lista_ordens[1])
while m != 0 and n != 0:
    M = leia(m)
    N = leia(n)
    if len(M) > len(N):
        maior_matriz = M
        menor_matriz = N
    else:
        maior_matriz = N
        menor_matriz = M
    ordem_da_maior = len(maior_matriz)
    ordem_da_menor = len(menor_matriz)
    info_elem_comuns = list(info_elem_iguais(maior_matriz,menor_matriz))
    if info_elem_comuns[0] == matriz_em_lista(menor_matriz):
        print(f'{ordem_da_maior} x {ordem_da_maior}')
    else:
        print(encontra_p_q(maior_matriz,menor_matriz))
    lista_ordens = input().split(" ")
    m = int(lista_ordens[0])
=======
def leia(ordem):
    '''
    transforma entrada em matriz
    '''
    matriz = []
    for i in range(ordem):
        matriz.append([])
        linha = input().split(" ")
        for j in range(ordem): 
            matriz[i].append(int(linha[j]))
    return(matriz)
def matriz_em_lista(A):
    '''
    transforma matriz em lista (lineariza)
    '''
    lista = []
    for i in range (len(A)):
        for j in range(len(A)):
            lista.append(A[i][j])
    return(lista)
def info_elem_iguais(maior, menor):
    '''
    encontra a linha e a coluna ,respectiva à matriz menor, dos elementos comuns às matrizes 
    encontra também quem é os elementos
    '''
    lista_elem_iguais = []
    linha_dos_iguais = []
    coluna_dos_iguais = []
    l_menor = matriz_em_lista(menor)
    l_maior = matriz_em_lista(maior)
    set_maior = set(l_maior)
    set_menor = set(l_menor)
    elem_iguais = set_maior.intersection(set_menor) #encontra intersecção de M com N
    lista_elem_iguais = list(elem_iguais)
    for i in range(len(lista_elem_iguais)):
        y = l_menor.index(lista_elem_iguais[i]) #posição do elem igual na lista
        linha_dos_iguais.append(y // len(menor)) #descobre i,j dos elementos que são comuns a M e N através das formulas de deslinearização
        coluna_dos_iguais.append(y % len(menor))
    return([lista_elem_iguais, linha_dos_iguais, coluna_dos_iguais])

def encontra_p_q(maior,menor):
    '''
    encontra o numero de linhas e colunas da supermatriz (matriz que é a sobreposição de M e N)
    '''
    lista_linhas = info_elem_comuns[1]
    lista_col = info_elem_comuns[2]
    p = len(maior) + (len(menor) - len(list(set(lista_linhas)))) #a sobreposição de matrizes adiciona o numero de linhas e colunas dos elementos, que não são comuns à M e N, da matriz menor à matriz maior 
    q = len(maior) + (len(menor) - len(list(set(lista_col))))   
    return(f'{p} x {q}')

lista_ordens = input().split(" ")
m = int(lista_ordens[0])
n = int(lista_ordens[1])
while m != 0 and n != 0:
    M = leia(m)
    N = leia(n)
    if len(M) > len(N):
        maior_matriz = M
        menor_matriz = N
    else:
        maior_matriz = N
        menor_matriz = M
    ordem_da_maior = len(maior_matriz)
    ordem_da_menor = len(menor_matriz)
    info_elem_comuns = list(info_elem_iguais(maior_matriz,menor_matriz))
    if info_elem_comuns[0] == matriz_em_lista(menor_matriz):
        print(f'{ordem_da_maior} x {ordem_da_maior}')
    else:
        print(encontra_p_q(maior_matriz,menor_matriz))
    lista_ordens = input().split(" ")
    m = int(lista_ordens[0])
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
    n = int(lista_ordens[1])