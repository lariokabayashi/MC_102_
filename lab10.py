<<<<<<< HEAD
lista_dicts = []
dict_susp_ou_ev = {}
lista_suspeitos = []
while True:
    linha = input()
    
    if linha == '-' or linha == '--':
        #armazenando dicionários ou de um suspeito ou das evideências numa lista
        lista_dicts.append(dict_susp_ou_ev) 
        dict_susp_ou_ev = {}
    elif linha == '---':
        lista_dicts.append(dict_susp_ou_ev)
        dict_susp_ou_ev = {}
        break
    else:
        caracteristica, valor = linha.split(":")
        #armazena em um dicionario a caract e seu respectivo valor
        dict_susp_ou_ev[caracteristica] = valor 

dict_evidencia = lista_dicts[-1] #ultimo dicionario da lista é o das evidencias
for i in range(len(lista_dicts)- 1):
    #buscas sequenciais por caracteristicas dos suspeitos que sejam iguais as da evidencia
    for caract_suspeito, valor_suspeito in lista_dicts[i].items():
        for caract_ev, valor_ev in dict_evidencia.items():
            if (caract_suspeito == caract_ev) and (valor_suspeito == valor_ev):
                suspeito = lista_dicts[i]['Nome']
                #toda vez que uma caracterisca é igual a da evidencia, anota-se o nome do suspeito
                lista_suspeitos.append(suspeito)

# vezes que suspeito aparece na lista = vezes que suas caract foram iguais as das evidências
lista_suspeitos_atualizada = []
for i in range(len(lista_suspeitos)):
    n = lista_suspeitos.count(lista_suspeitos[i])
    if n == len(dict_evidencia):
        #para ser o real suspeito todas evidencias devem ser correspondidas (não basta apenas uma ser)
        lista_suspeitos_atualizada.append(lista_suspeitos[i])
lista_suspeitos_atualizada = list(set(lista_suspeitos_atualizada)) #eliminando repetições
if len(lista_suspeitos_atualizada) == 0:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
elif len(lista_suspeitos_atualizada) == 1:
    print('Suspeito(a):')
    print(lista_suspeitos_atualizada[0].strip("'").strip())
else: 
    print('Suspeitos(as):')
    lista_formatada = [x.strip("'").strip() for x in sorted(lista_suspeitos_atualizada)]
    print(*lista_formatada, sep = "\n")
=======
lista_dicts = []
dict_susp_ou_ev = {}
lista_suspeitos = []
while True:
    linha = input()
    
    if linha == '-' or linha == '--':
        #armazenando dicionários ou de um suspeito ou das evideências numa lista
        lista_dicts.append(dict_susp_ou_ev) 
        dict_susp_ou_ev = {}
    elif linha == '---':
        lista_dicts.append(dict_susp_ou_ev)
        dict_susp_ou_ev = {}
        break
    else:
        caracteristica, valor = linha.split(":")
        #armazena em um dicionario a caract e seu respectivo valor
        dict_susp_ou_ev[caracteristica] = valor 

dict_evidencia = lista_dicts[-1] #ultimo dicionario da lista é o das evidencias
for i in range(len(lista_dicts)- 1):
    #buscas sequenciais por caracteristicas dos suspeitos que sejam iguais as da evidencia
    for caract_suspeito, valor_suspeito in lista_dicts[i].items():
        for caract_ev, valor_ev in dict_evidencia.items():
            if (caract_suspeito == caract_ev) and (valor_suspeito == valor_ev):
                suspeito = lista_dicts[i]['Nome']
                #toda vez que uma caracterisca é igual a da evidencia, anota-se o nome do suspeito
                lista_suspeitos.append(suspeito)

# vezes que suspeito aparece na lista = vezes que suas caract foram iguais as das evidências
lista_suspeitos_atualizada = []
for i in range(len(lista_suspeitos)):
    n = lista_suspeitos.count(lista_suspeitos[i])
    if n == len(dict_evidencia):
        #para ser o real suspeito todas evidencias devem ser correspondidas (não basta apenas uma ser)
        lista_suspeitos_atualizada.append(lista_suspeitos[i])
lista_suspeitos_atualizada = list(set(lista_suspeitos_atualizada)) #eliminando repetições
if len(lista_suspeitos_atualizada) == 0:
    print('Nenhum suspeito(a) com essas caracteristicas foi identificado(a).')
elif len(lista_suspeitos_atualizada) == 1:
    print('Suspeito(a):')
    print(lista_suspeitos_atualizada[0].strip("'").strip())
else: 
    print('Suspeitos(as):')
    lista_formatada = [x.strip("'").strip() for x in sorted(lista_suspeitos_atualizada)]
    print(*lista_formatada, sep = "\n")
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
