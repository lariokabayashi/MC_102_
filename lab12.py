<<<<<<< HEAD
def cria_matriz(M, N):
    return [['-F'] * N for _ in range(M)] #cria matriz e indica que elementos dela ainda não foram visitados(F)
 
def desenhe_quadrado(x, y, i, j, l, matriz):
    '''
    (x, y) = coordenadas
    (j, i) = centro do quadrado
    l = lado
    '''
    if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]): #a partir daí apenas coordenadas válidas
            if abs(i - x) <= l and abs(j - y) <= l: #a partir dessa linha só coordenadas válidas pro quadrado
                if matriz[x][y][1] == "F": #a partir daí só elementos não visitados
                    matriz[x][y] = "xT"
                    desenhe_quadrado(x - 1, y, i, j, l, matriz) #percorrendo pra cima da matriz
                    desenhe_quadrado(x + 1, y, i, j, l, matriz) #percorrendo para baixo
                    desenhe_quadrado(x, y - 1, i, j, l, matriz) #percorrendo à esquerda
                    desenhe_quadrado(x, y + 1, i, j, l, matriz) #percorrendo à direita

def desenhe_circulo (x, y, i, j, r, matriz):  
     if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]): #a partir daí apenas coordenadas válidas
            if (x - i)**2 + (y - j)**2 <= r**2: #a partir dessa linha só coordenadas válidas pro circulo
                if matriz[x][y][1] == "F": #a partir daí só elementos não visitados
                    matriz[x][y] = "xT"
                    desenhe_circulo(x - 1, y, i, j, r, matriz)
                    desenhe_circulo(x + 1, y, i, j, r, matriz)
                    desenhe_circulo(x, y - 1, i, j, r, matriz)
                    desenhe_circulo(x, y + 1, i, j, r, matriz)        

def reset_matriz(matriz):
    '''
    permite que outras figuras sejam impressas no quadro
    '''
    for i in range(len(matriz)):    
        for j in range(len(matriz[0])):
                matriz[i][j] = matriz[i][j][0] + "F" #para as coordenadas da matriz poderem ser percorridas novamente para desenhar outras figuras                   

def imprime_matriz(matriz):
    '''
    transforma matriz em string com espaços e imprime a string
    '''
    s = ''
    for i in range(len(matriz)):    
        for j in range(len(matriz[0])):
            s += matriz[i][j][0] + ' '
        if i != len(matriz) - 1:   
            s += '\n'
    print(s)    

instrucoes = []
linha = input().split(" ")
M = int(linha[0])
N = int(linha[1])
Q = int(input()) #quantidade de figuras que vão ser desenhadas
for i in range(Q):
    instrucao_entrada = input().split(" ")
    forma, i, j, r_l = instrucao_entrada
    instrucoes.append((forma, int(i), int(j), int(r_l)))
matriz_do_quadro = cria_matriz(M, N)
for instrucao in instrucoes:
    x, i = instrucao[1], instrucao[1]
    y, j = instrucao[2], instrucao[2]
    if instrucao[0] == "quadrado":
        desenhe_quadrado(x, y, i, j, instrucao[3]/2, matriz_do_quadro)
    else:
        desenhe_circulo(x, y, i, j, instrucao[3], matriz_do_quadro)
    reset_matriz(matriz_do_quadro)
imprime_matriz(matriz_do_quadro)

=======
def cria_matriz(M, N):
    return [['-F'] * N for _ in range(M)] #cria matriz e indica que elementos dela ainda não foram visitados(F)
 
def desenhe_quadrado(x, y, i, j, l, matriz):
    '''
    (x, y) = coordenadas
    (j, i) = centro do quadrado
    l = lado
    '''
    if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]): #a partir daí apenas coordenadas válidas
            if abs(i - x) <= l and abs(j - y) <= l: #a partir dessa linha só coordenadas válidas pro quadrado
                if matriz[x][y][1] == "F": #a partir daí só elementos não visitados
                    matriz[x][y] = "xT"
                    desenhe_quadrado(x - 1, y, i, j, l, matriz) #percorrendo pra cima da matriz
                    desenhe_quadrado(x + 1, y, i, j, l, matriz) #percorrendo para baixo
                    desenhe_quadrado(x, y - 1, i, j, l, matriz) #percorrendo à esquerda
                    desenhe_quadrado(x, y + 1, i, j, l, matriz) #percorrendo à direita

def desenhe_circulo (x, y, i, j, r, matriz):  
     if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]): #a partir daí apenas coordenadas válidas
            if (x - i)**2 + (y - j)**2 <= r**2: #a partir dessa linha só coordenadas válidas pro circulo
                if matriz[x][y][1] == "F": #a partir daí só elementos não visitados
                    matriz[x][y] = "xT"
                    desenhe_circulo(x - 1, y, i, j, r, matriz)
                    desenhe_circulo(x + 1, y, i, j, r, matriz)
                    desenhe_circulo(x, y - 1, i, j, r, matriz)
                    desenhe_circulo(x, y + 1, i, j, r, matriz)        

def reset_matriz(matriz):
    '''
    permite que outras figuras sejam impressas no quadro
    '''
    for i in range(len(matriz)):    
        for j in range(len(matriz[0])):
                matriz[i][j] = matriz[i][j][0] + "F" #para as coordenadas da matriz poderem ser percorridas novamente para desenhar outras figuras                   

def imprime_matriz(matriz):
    '''
    transforma matriz em string com espaços e imprime a string
    '''
    s = ''
    for i in range(len(matriz)):    
        for j in range(len(matriz[0])):
            s += matriz[i][j][0] + ' '
        if i != len(matriz) - 1:   
            s += '\n'
    print(s)    

instrucoes = []
linha = input().split(" ")
M = int(linha[0])
N = int(linha[1])
Q = int(input()) #quantidade de figuras que vão ser desenhadas
for i in range(Q):
    instrucao_entrada = input().split(" ")
    forma, i, j, r_l = instrucao_entrada
    instrucoes.append((forma, int(i), int(j), int(r_l)))
matriz_do_quadro = cria_matriz(M, N)
for instrucao in instrucoes:
    x, i = instrucao[1], instrucao[1]
    y, j = instrucao[2], instrucao[2]
    if instrucao[0] == "quadrado":
        desenhe_quadrado(x, y, i, j, instrucao[3]/2, matriz_do_quadro)
    else:
        desenhe_circulo(x, y, i, j, instrucao[3], matriz_do_quadro)
    reset_matriz(matriz_do_quadro)
imprime_matriz(matriz_do_quadro)

>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
