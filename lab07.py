<<<<<<< HEAD
def codificar_impar(linha):
    '''
    codifica a linha impar de uma mensagem de acordo com as regras de codificacao
    '''
    lista_codificada = []
    linha_em_lista = list(linha)
    for x in range(len(linha_em_lista)):
        valor_do_caracter = ord(linha_em_lista[x])
        caracter_codificado = hex(valor_do_caracter)
        lista_caracter_codificado = list(caracter_codificado)
        lista_caracter_codificado.remove("0")
        lista_caracter_codificado.remove("x")
        for k in range(len(lista_caracter_codificado)):
            if lista_caracter_codificado[k] == 'a' or 'b' or 'c' or 'd' or 'e' or 'f':
                lista_caracter_codificado[k] = lista_caracter_codificado[k].upper()
        caracter_codificado_atualizado = "".join(lista_caracter_codificado)
        lista_codificada.append(formata_caracter(caracter_codificado_atualizado,int(enxerto)))  
        linha_codificada = "".join(lista_codificada)
    return linha_codificada 

def codificar_par(linha):
    '''
    codifica a linha par de uma mensagem de acordo com as regras de codificacao para linha par
    '''
    lista_codificada= []
    linha_em_lista = list(linha)
    inverte_linha = linha_em_lista[::-1]
    for x in range(len(inverte_linha)):
        valor_do_caracter = ord(inverte_linha[x])
        caracter_codificado = oct(valor_do_caracter)
        lista_caracter_codificado = list(caracter_codificado)
        lista_caracter_codificado.remove("0")
        lista_caracter_codificado.remove("o")
        caracter_codificado_atualizado = "".join(lista_caracter_codificado)
        lista_codificada.append(formata_caracter(caracter_codificado_atualizado,int(enxerto)))
    linha_codificada = "".join(lista_codificada)  
    return linha_codificada

def formata_caracter(caracter,E):
    '''
    insere zeros ou não para o codigo ter numero de caracteres igual ao parâmetro E (enxerto)
    '''
    if len(list(caracter)) < E:
         str_preenchida =caracter.zfill(E)
         return str_preenchida
    return caracter

def decodificar(linha_codificada):
    '''
    separa a mensagem codificada em codigos de numero de caracteres igual ao enxerto
    '''
    lista_caracteres_codificados = []
    lista_codigos_sep = []
    lista_codificada = list(linha_codificada)
    for x in range(0,len(linha_codificada),int(enxerto)):
        for k in range(x,x+int(enxerto)):
            codigo = lista_codificada[k] 
            lista_codigos_sep.append(codigo)
        caracter_codificado = "".join(lista_codigos_sep) 
        lista_caracteres_codificados.append(caracter_codificado) 
        lista_codigos_sep = []
    return(lista_caracteres_codificados)    

def decodificar_impar(linha):
    '''
    decodifica cada codigo da(s) linha(s) impares achando o caracter que corresponde a ele
    '''
    lista_linha_descodificada = []
    lista_caracteres_codificados = decodificar(linha)
    for x in range(len(lista_caracteres_codificados)):
        sep_codigo = list(lista_caracteres_codificados[x])
        if sep_codigo[0] == '0':    
            sep_codigo.remove('0')
        for k in range(len(sep_codigo)):
            if sep_codigo[k] == 'A' or 'B' or 'C' or 'D' or 'E' or 'F':
                sep_codigo[k] = sep_codigo[k].lower()   
        lista_caracteres_codificados[x] = "".join(sep_codigo)
        num_base_10 = int(lista_caracteres_codificados[x],16)
        caracter_descodificado = chr(num_base_10)
        lista_linha_descodificada.append(caracter_descodificado)
    linha_descodificada = "".join(lista_linha_descodificada)    
    return linha_descodificada
        

def decodificar_par(linha):
    '''
    decodifica cada codigo da(s) linha(s) pares achando o caracter que corresponde a ele
    '''
    lista_linha_descodificada = []
    lista_caracteres_codificados = decodificar(linha)
    for x in range(len(lista_caracteres_codificados)):
        sep_codigo = list(lista_caracteres_codificados[x])  
        if sep_codigo[0] == '0':  
            sep_codigo.remove('0')
        lista_caracteres_codificados[x] = "".join(sep_codigo)
        num_base_10 = int(lista_caracteres_codificados[x],8)
        caracter_descodificado = chr(num_base_10)
        lista_linha_descodificada.append(caracter_descodificado)
        lista_desinvertida =lista_linha_descodificada[::-1]
    linha_descodificada = "".join(lista_desinvertida)    
    return linha_descodificada

#entrada:
modo, enxerto, linhas = input().split(" ")
if modo == "1" :
    for i in range (1,int(linhas)+1):
        if i % 2 != 0:
            print(codificar_impar(input()))
        else:
            print(codificar_par(input()))

else:
    for i in range (1,int(linhas)+1):
        if i % 2 != 0:
            print(decodificar_impar(input()))
        else:
            print(decodificar_par(input()))
=======
def codificar_impar(linha):
    '''
    codifica a linha impar de uma mensagem de acordo com as regras de codificacao
    '''
    lista_codificada = []
    linha_em_lista = list(linha)
    for x in range(len(linha_em_lista)):
        valor_do_caracter = ord(linha_em_lista[x])
        caracter_codificado = hex(valor_do_caracter)
        lista_caracter_codificado = list(caracter_codificado)
        lista_caracter_codificado.remove("0")
        lista_caracter_codificado.remove("x")
        for k in range(len(lista_caracter_codificado)):
            if lista_caracter_codificado[k] == 'a' or 'b' or 'c' or 'd' or 'e' or 'f':
                lista_caracter_codificado[k] = lista_caracter_codificado[k].upper()
        caracter_codificado_atualizado = "".join(lista_caracter_codificado)
        lista_codificada.append(formata_caracter(caracter_codificado_atualizado,int(enxerto)))  
        linha_codificada = "".join(lista_codificada)
    return linha_codificada 

def codificar_par(linha):
    '''
    codifica a linha par de uma mensagem de acordo com as regras de codificacao para linha par
    '''
    lista_codificada= []
    linha_em_lista = list(linha)
    inverte_linha = linha_em_lista[::-1]
    for x in range(len(inverte_linha)):
        valor_do_caracter = ord(inverte_linha[x])
        caracter_codificado = oct(valor_do_caracter)
        lista_caracter_codificado = list(caracter_codificado)
        lista_caracter_codificado.remove("0")
        lista_caracter_codificado.remove("o")
        caracter_codificado_atualizado = "".join(lista_caracter_codificado)
        lista_codificada.append(formata_caracter(caracter_codificado_atualizado,int(enxerto)))
    linha_codificada = "".join(lista_codificada)  
    return linha_codificada

def formata_caracter(caracter,E):
    '''
    insere zeros ou não para o codigo ter numero de caracteres igual ao parâmetro E (enxerto)
    '''
    if len(list(caracter)) < E:
         str_preenchida =caracter.zfill(E)
         return str_preenchida
    return caracter

def decodificar(linha_codificada):
    '''
    separa a mensagem codificada em codigos de numero de caracteres igual ao enxerto
    '''
    lista_caracteres_codificados = []
    lista_codigos_sep = []
    lista_codificada = list(linha_codificada)
    for x in range(0,len(linha_codificada),int(enxerto)):
        for k in range(x,x+int(enxerto)):
            codigo = lista_codificada[k] 
            lista_codigos_sep.append(codigo)
        caracter_codificado = "".join(lista_codigos_sep) 
        lista_caracteres_codificados.append(caracter_codificado) 
        lista_codigos_sep = []
    return(lista_caracteres_codificados)    

def decodificar_impar(linha):
    '''
    decodifica cada codigo da(s) linha(s) impares achando o caracter que corresponde a ele
    '''
    lista_linha_descodificada = []
    lista_caracteres_codificados = decodificar(linha)
    for x in range(len(lista_caracteres_codificados)):
        sep_codigo = list(lista_caracteres_codificados[x])
        if sep_codigo[0] == '0':    
            sep_codigo.remove('0')
        for k in range(len(sep_codigo)):
            if sep_codigo[k] == 'A' or 'B' or 'C' or 'D' or 'E' or 'F':
                sep_codigo[k] = sep_codigo[k].lower()   
        lista_caracteres_codificados[x] = "".join(sep_codigo)
        num_base_10 = int(lista_caracteres_codificados[x],16)
        caracter_descodificado = chr(num_base_10)
        lista_linha_descodificada.append(caracter_descodificado)
    linha_descodificada = "".join(lista_linha_descodificada)    
    return linha_descodificada
        

def decodificar_par(linha):
    '''
    decodifica cada codigo da(s) linha(s) pares achando o caracter que corresponde a ele
    '''
    lista_linha_descodificada = []
    lista_caracteres_codificados = decodificar(linha)
    for x in range(len(lista_caracteres_codificados)):
        sep_codigo = list(lista_caracteres_codificados[x])  
        if sep_codigo[0] == '0':  
            sep_codigo.remove('0')
        lista_caracteres_codificados[x] = "".join(sep_codigo)
        num_base_10 = int(lista_caracteres_codificados[x],8)
        caracter_descodificado = chr(num_base_10)
        lista_linha_descodificada.append(caracter_descodificado)
        lista_desinvertida =lista_linha_descodificada[::-1]
    linha_descodificada = "".join(lista_desinvertida)    
    return linha_descodificada

#entrada:
modo, enxerto, linhas = input().split(" ")
if modo == "1" :
    for i in range (1,int(linhas)+1):
        if i % 2 != 0:
            print(codificar_impar(input()))
        else:
            print(codificar_par(input()))

else:
    for i in range (1,int(linhas)+1):
        if i % 2 != 0:
            print(decodificar_impar(input()))
        else:
            print(decodificar_par(input()))
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
