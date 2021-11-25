<<<<<<< HEAD

def BuscaBinaria(l):
    e = 0
    d = Y #variavel global
    m = 1 #meio na lista com len(l) = 3 é 1 
    while e <=d:
        meio = (e + d)//2 
        l = dist_esconderijo_max(meio, meio + 3) #lista com o meio e elementos adjacentes ao meio
        if l[m] < l[m - 1] and l[m] < l[m + 1]: #se o meio é o menor valor da lista, imprima o index dele na lista com todas as distâncias
            return(m + meio) 
        elif l[m] > l[m - 1]: #se o elem antes do meio é menor valor, calcule a metade de 0 até meio atual, essa metade será o novo meio
            d = meio - 1
        elif l[m] > l[m + 1]:#se elem dps de meio for menor valor, novo meio é a metade de meio atual até Y(final da lista com todas distâncias) 
            e = meio + 1
            
def dist_esconderijo_max(p,q):
    '''calcula a distância do esconderijo mais distante'''
    lista = []
    for y in range(p, q):
        for e in range(len(lista_y_values)): 
            dist_ao_quadrado = (lista_x_values[e] - 0)**2 + (lista_y_values[e] - y)**2
            if e == 0:
                esconderijo_mais_dist = dist_ao_quadrado
            else:
                if dist_ao_quadrado > esconderijo_mais_dist:
                    esconderijo_mais_dist = dist_ao_quadrado 
        lista.append(esconderijo_mais_dist)
    return(lista)

linha = input().split(" ")
N = int(linha[0])
Y = int(linha[1])
while N != 0 and Y != 0:
    lista_x_values = []
    lista_y_values = []
    lista_escond_mais_dist = []
    for i in range(N):
        coordenada = input().split(" ")
        x = int(coordenada[0])
        y = int(coordenada[1])
        if y > 0 : #primeiro e segundo quadrantes
            lista_x_values.append(x)
            lista_y_values.append(y)
    print(BuscaBinaria(lista_escond_mais_dist))  #lista gerada na função
    linha = input().split(" ")
    N = int(linha[0])
    Y = int(linha[1])
=======

def BuscaBinaria(l):
    e = 0
    d = Y #variavel global
    m = 1 #meio na lista com len(l) = 3 é 1 
    while e <=d:
        meio = (e + d)//2 
        l = dist_esconderijo_max(meio, meio + 3) #lista com o meio e elementos adjacentes ao meio
        if l[m] < l[m - 1] and l[m] < l[m + 1]: #se o meio é o menor valor da lista, imprima o index dele na lista com todas as distâncias
            return(m + meio) 
        elif l[m] > l[m - 1]: #se o elem antes do meio é menor valor, calcule a metade de 0 até meio atual, essa metade será o novo meio
            d = meio - 1
        elif l[m] > l[m + 1]:#se elem dps de meio for menor valor, novo meio é a metade de meio atual até Y(final da lista com todas distâncias) 
            e = meio + 1
            
def dist_esconderijo_max(p,q):
    '''calcula a distância do esconderijo mais distante'''
    lista = []
    for y in range(p, q):
        for e in range(len(lista_y_values)): 
            dist_ao_quadrado = (lista_x_values[e] - 0)**2 + (lista_y_values[e] - y)**2
            if e == 0:
                esconderijo_mais_dist = dist_ao_quadrado
            else:
                if dist_ao_quadrado > esconderijo_mais_dist:
                    esconderijo_mais_dist = dist_ao_quadrado 
        lista.append(esconderijo_mais_dist)
    return(lista)

linha = input().split(" ")
N = int(linha[0])
Y = int(linha[1])
while N != 0 and Y != 0:
    lista_x_values = []
    lista_y_values = []
    lista_escond_mais_dist = []
    for i in range(N):
        coordenada = input().split(" ")
        x = int(coordenada[0])
        y = int(coordenada[1])
        if y > 0 : #primeiro e segundo quadrantes
            lista_x_values.append(x)
            lista_y_values.append(y)
    print(BuscaBinaria(lista_escond_mais_dist))  #lista gerada na função
    linha = input().split(" ")
    N = int(linha[0])
    Y = int(linha[1])
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
