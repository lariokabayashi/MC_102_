<<<<<<< HEAD
class Medalutador:
    def __init__(self, ID, habilidade_atual, recuperacao): #sem função "obter", pois a init já supre todas necessidades 
        self.ID = ID
        self.habilidade_atual = habilidade_atual
        self.recuperacao = recuperacao
    def __repr__(self):
        return str(self.ID) #para que ao printar o medalutador apareça seu ID
class Medabot:
    def __init__(self, medapecas, ataque, defesa, bonus_de_ataque, bonus_de_defesa):
        self.medapecas = medapecas
        self.ataque = ataque
        self.defesa = defesa
        self.bonus_de_ataque = bonus_de_ataque
        self.bonus_de_defesa = bonus_de_defesa
class Medapecas:
    def __init__(self, pontos_do_torso, pontos_do_braco_e, pontos_do_braco_d, pontos_das_pernas):
        self.pontos_do_torso = pontos_do_torso
        self.pontos_do_braco_e = pontos_do_braco_e
        self.pontos_do_braco_d = pontos_do_braco_d
        self.pontos_das_pernas = pontos_das_pernas
      
def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem  = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID])
  print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores
    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0) 
        j = lista_de_medalutadores.pop(0)
        if i.ID > j.ID:
            i, j = j, i
        if lista_de_repescagem != None:
           print('Cyberluta do Torneio Principal')
        else:
             print('Cyberluta da Repescagem')
        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)
        k = batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID])
        medapeca_ganhada = peca_ganhada(i, j)
        print(f'Medalutador {k} venceu e recebeu a {medapeca_ganhada}\n')
        atualiza_a_habilidade(i, j)
        atualiza_pontos(lista_de_medapecas[i.ID], lista_de_medapecas[j.ID], lista_de_medabot[i.ID], lista_de_medabot[j.ID])
        if lista_de_repescagem != None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)
        lista_de_vencedores.append(k)
    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores

def batalhar(i, j, medabot_i, medabot_j):
    '''
    retorna o vencedor da batalha
    '''
    Ai, Di, Hi = medabot_i.ataque, medabot_i.defesa, i.habilidade_atual
    Aj, Dj, Hj =  medabot_j.ataque, medabot_j.defesa, j.habilidade_atual
    if (Ai > Dj or Aj > Di) and Ai - Dj != Aj - Di:
        if Ai - Dj > Aj - Di:
            return i
        elif Ai - Dj < Aj - Di:
            return j
    elif Hi != Hj:
        if Hi > Hj:
            return i
        elif Hi < Hj:
            return j
    elif i.ID < j.ID:
        return i
    elif i.ID > j.ID:
        return j
def altera_habilidade (vencedor, perdedor):
    '''
    atualiza o H do perdedor e ganhador para a próxima batalha(já contando com os pontos de recuperacao)
    '''
    H_venceu, H_perdeu, K_venceu, K_perdeu = vencedor.habilidade_atual, perdedor.habilidade_atual, vencedor.recuperacao, perdedor.recuperacao
    H_inicial_v, H_iniciaL_p = lista_habilidades_iniciais[vencedor.ID], lista_habilidades_iniciais[perdedor.ID]
    h_atual_v = H_venceu - H_perdeu
    if h_atual_v < 0: #habilidade não pode ser negativa
        h_atual_v = 0
    if h_atual_v + K_venceu <= H_inicial_v: # habilidade não pode ser maior que a inicial
        vencedor.habilidade_atual = h_atual_v + K_venceu
    elif h_atual_v + K_venceu > H_inicial_v:
        vencedor.habilidade_atual = H_inicial_v #como habilidade atual não pode ser maior que inicial, quando isso acontece ela simplesmente volta a ser igual inicial
    h_atual_p = H_perdeu//2
    if h_atual_p + K_perdeu <= H_iniciaL_p:
        perdedor.habilidade_atual = h_atual_p + K_perdeu
    elif h_atual_p + K_perdeu > H_iniciaL_p:
        perdedor.habilidade_atual = H_iniciaL_p

def atualiza_a_habilidade(i, j):
    if batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == i: 
        altera_habilidade(i, j)
    elif batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == j:
        altera_habilidade(j, i)

def tira_peca_do_perdedor (perdedor, pontos_perdidos, tipo_da_peca_perdida):
    '''
    remove a peca que perdedor deu e retorna os pontos da peca que substituirá a perdida 
    '''
    ID_perdedor = perdedor.ID
    pontos_atualizado = 0
    lista_medapecas = lista_de_medabot[ID_perdedor].medapecas
    lista_medapecas.remove(tipo_da_peca_perdida + " " + str(pontos_perdidos)) #tire da lista de medapeças a medapeça perdida
    for k in range(len(lista_medapecas)):
        if lista_medapecas[k].split(" ")[0] == tipo_da_peca_perdida: #se o tipo de peça na lista de medapeças do perdedor for igual ao tipo da medapeça perdida
            if int(lista_medapecas[k].split(" ")[1]) > pontos_atualizado:
                pontos_atualizado =  int(lista_medapecas[k].split(" ")[1]) #pegue ,como substituto da peça perdida, uma outra do mesmo tipo e com o máximo de pontos possível
    return pontos_atualizado  

def define_medapeca_ganhada(vencedor, perdedor, pecas_v, pecas_p):
    '''
    retorna a peça ganha e os pontos ela dá, define se o vencedor usará a peca ou não na próx batalha
    tira a peca do perdedor ao chamar outra funcaoinsere a peca na lista de medapecas do vencedor
    '''
    ID_v, ID_p = vencedor.ID, perdedor.ID
    t_v, br_e_v, br_d_v, p_v, b_a_v, b_d_v, t_p, br_e_p, br_d_p, p_p, b_a_p, b_d_p = atualiza_pontos(lista_de_medapecas[ID_v], lista_de_medapecas[ID_p], lista_de_medabot[ID_v], lista_de_medabot[ID_p])
    l_pecas_v = [t_v, br_e_v, br_d_v, p_v]
    l_pecas_p = [t_p, br_e_p, br_d_p, p_p]
    diferenca_listas = [n2 - n1 for (n1, n2) in zip(l_pecas_v, l_pecas_p)] 
    maior_pontos = max (diferenca_listas, key=int) #encontrando a peça que dará mais vantagem pro vencedor na próx partida, de acordo com as peças do perdedor
    posicao = diferenca_listas.index(maior_pontos) 
    pontos_da_medapeca_ganha = l_pecas_p[posicao]
    if posicao == 0: #significa que a medapeça ganha é o torso 
        if pontos_da_medapeca_ganha > t_v: # não é possível transformar essas partes repetidas em função, pois precisa-se atualizar os pontos das medapeças nas classes
            pecas_v.pontos_do_torso = pontos_da_medapeca_ganha
        pecas_p.pontos_do_torso = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha,"T")
        tipo_da_medapeca_ganha = "T"
    elif posicao == 1:#significa que a medapeça ganha é o braço esquerdo
        if pontos_da_medapeca_ganha > br_e_v:
            pecas_v.pontos_do_braco_e= pontos_da_medapeca_ganha
        pecas_p.pontos_do_braco_e = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "E")
        tipo_da_medapeca_ganha = "E"
    elif posicao == 2: 
        if pontos_da_medapeca_ganha > br_d_v:#significa que a medapeça ganha é o braço direito
            pecas_v.pontos_do_braco_d = pontos_da_medapeca_ganha
        pecas_p.pontos_do_braco_d = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "D")
        tipo_da_medapeca_ganha = "D"
    else:
        if pontos_da_medapeca_ganha > p_v:#significa que a medapeça ganha é a perna
            pecas_v.pontos_das_pernas = pontos_da_medapeca_ganha
        pecas_p.pontos_das_pernas = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "P")
        tipo_da_medapeca_ganha = "P"
    lista_de_medabot[ID_v].medapecas.append(tipo_da_medapeca_ganha + " " + str(pontos_da_medapeca_ganha)) #colocar na lista de medapeças do vencedor a peça nova ganhada
    return(tipo_da_medapeca_ganha + str(pontos_da_medapeca_ganha))

def peca_ganhada(i, j):
    if batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == i:
        return(define_medapeca_ganhada(i, j, lista_de_medapecas[i.ID], lista_de_medapecas[j.ID]))
    else:
        return(define_medapeca_ganhada(j, i, lista_de_medapecas[j.ID], lista_de_medapecas[i.ID]))

def atualiza_pontos(peca_i, peca_j, medabot_i, medabot_j):
    '''
    atualiza o ataque e defesa para próx batalha, pois os robos perderam e/ou ganharam pecas, também retorna os pontos de cada peça atualizados, pois assim fica mais simples de definir as variaveis nas outras funções que as utilizam
    '''
    torso_i, braco_e_i, braco_d_i, pernas_i = peca_i.pontos_do_torso, peca_i.pontos_do_braco_e, peca_i.pontos_do_braco_d, peca_i.pontos_das_pernas
    bonus_ataque_i, bonus_defesa_i = medabot_i.bonus_de_ataque, medabot_i.bonus_de_defesa
    torso_j,  braco_e_j, braco_d_j, pernas_j = peca_j.pontos_do_torso, peca_j.pontos_do_braco_e, peca_j.pontos_do_braco_d, peca_j.pontos_das_pernas
    bonus_ataque_j, bonus_defesa_j = medabot_j.bonus_de_ataque, medabot_j.bonus_de_defesa
    medabot_i.ataque,  medabot_i.defesa = (braco_d_i + braco_e_i + bonus_ataque_i), (torso_i + pernas_i + bonus_defesa_i)
    medabot_j.ataque, medabot_j.defesa = (braco_d_j + braco_e_j + bonus_ataque_j), (torso_j + pernas_j + bonus_defesa_j)
    return (torso_i, braco_e_i, braco_d_i, pernas_i, bonus_ataque_i, bonus_defesa_i, torso_j ,braco_e_j, braco_d_j, pernas_j, bonus_ataque_j, bonus_defesa_j)

def imprimir_ficha_tecnica(i,j):
    I, J = i.ID, j.ID
    t_i, br_e_i, br_d_i, p_i, b_a_i, b_d_i, t_j, br_e_j, br_d_j, p_j, b_a_j, b_d_j = atualiza_pontos(lista_de_medapecas[I], lista_de_medapecas[J], lista_de_medabot[I], lista_de_medabot[J])
    print(f'\tA{I} = E{br_e_i} + D{br_d_i} + {b_a_i} = {br_e_i + br_d_i + b_a_i}')
    print(f'\tD{I} = T{t_i} + P{p_i} + {b_d_i} = {t_i + p_i + b_d_i}')
    print(f'\tH{I} = {i.habilidade_atual}')
    print(f'\tA{J} = E{br_e_j} + D{br_d_j} + {b_a_j} = {br_e_j + br_d_j + b_a_j}')
    print(f'\tD{J} = T{t_j} + P{p_j} + {b_d_j} = {t_j + p_j + b_d_j}')
    print(f'\tH{J} = {j.habilidade_atual}')

N = int(input())
lista_habilidades_iniciais = [0] #para index ser igual da lista de medalutadores
lista_de_medalutadores = []
lista_de_medabot = [0] #para index ser igual da lista de medalutadores
lista_de_medapecas = [0]
for k in range(N):
    lista_de_pecas, lista_torso, lista_braco_e, lista_braco_d, lista_perna = [], [], [], [], []
    h_k_numeropecas= input().split(" ")
    pontos_de_habilidade, pontos_de_recuperacao, numero_de_pecas = int(h_k_numeropecas[0]), int(h_k_numeropecas[1]), int(h_k_numeropecas[2])
    lista_habilidades_iniciais.append(pontos_de_habilidade)
    medalha = input().split(" ")
    bonus_de_ataque, bonus_de_defesa = int(medalha[0]), int(medalha[1]) 
    for i in range(numero_de_pecas):
          medapeca = input()
          lista_de_pecas.append(medapeca)
          tipo, pontos = medapeca.split(" ")[0], medapeca.split(" ")[1]
          if tipo == "T":
              lista_torso.append(pontos)
          if tipo == "E":
              lista_braco_e.append(pontos)
          if tipo == "D":
              lista_braco_d.append(pontos)
          if tipo == "P":
              lista_perna.append(pontos) 
    pontos_do_torso = int(max(lista_torso,key=int))
    pontos_do_braco_e = int(max(lista_braco_e, key=int))
    pontos_do_braco_d = int(max(lista_braco_d, key=int))
    pontos_das_pernas = int(max(lista_perna, key=int))
    A = pontos_do_braco_d + pontos_do_braco_e + bonus_de_ataque
    D = pontos_do_torso + pontos_das_pernas + bonus_de_defesa
    medalutador = Medalutador(k+1, pontos_de_habilidade, pontos_de_recuperacao)
    lista_de_medalutadores.append(medalutador) #armazenando os medalutadores que correspondem a classe Medalutador numa lista
    medabot = Medabot(lista_de_pecas, A, D, bonus_de_ataque, bonus_de_defesa) #outras classes são necessárias, pois há atributos que não são do medalutador
    lista_de_medabot.append(medabot)
    medapecas = Medapecas(pontos_do_torso, pontos_do_braco_e, pontos_do_braco_d, pontos_das_pernas)
    lista_de_medapecas.append(medapecas)
=======
class Medalutador:
    def __init__(self, ID, habilidade_atual, recuperacao): #sem função "obter", pois a init já supre todas necessidades 
        self.ID = ID
        self.habilidade_atual = habilidade_atual
        self.recuperacao = recuperacao
    def __repr__(self):
        return str(self.ID) #para que ao printar o medalutador apareça seu ID
class Medabot:
    def __init__(self, medapecas, ataque, defesa, bonus_de_ataque, bonus_de_defesa):
        self.medapecas = medapecas
        self.ataque = ataque
        self.defesa = defesa
        self.bonus_de_ataque = bonus_de_ataque
        self.bonus_de_defesa = bonus_de_defesa
class Medapecas:
    def __init__(self, pontos_do_torso, pontos_do_braco_e, pontos_do_braco_d, pontos_das_pernas):
        self.pontos_do_torso = pontos_do_torso
        self.pontos_do_braco_e = pontos_do_braco_e
        self.pontos_do_braco_d = pontos_do_braco_d
        self.pontos_das_pernas = pontos_das_pernas
      
def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem  = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i} vs {j}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID])
  print(f'Campeao: medalutador {k}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
    if len(lista_de_medalutadores) < 2:
        return lista_de_medalutadores
    lista_de_vencedores = []
    while len(lista_de_medalutadores) >= 2:
        i = lista_de_medalutadores.pop(0) 
        j = lista_de_medalutadores.pop(0)
        if i.ID > j.ID:
            i, j = j, i
        if lista_de_repescagem != None:
           print('Cyberluta do Torneio Principal')
        else:
             print('Cyberluta da Repescagem')
        print(f'Medalutadores: {i} vs {j}')
        imprimir_ficha_tecnica(i, j)
        k = batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID])
        medapeca_ganhada = peca_ganhada(i, j)
        print(f'Medalutador {k} venceu e recebeu a {medapeca_ganhada}\n')
        atualiza_a_habilidade(i, j)
        atualiza_pontos(lista_de_medapecas[i.ID], lista_de_medapecas[j.ID], lista_de_medabot[i.ID], lista_de_medabot[j.ID])
        if lista_de_repescagem != None:
            if i == k:
                lista_de_repescagem.append(j)
            else:
                lista_de_repescagem.append(i)
        lista_de_vencedores.append(k)
    lista_de_vencedores.extend(lista_de_medalutadores)
    return lista_de_vencedores

def batalhar(i, j, medabot_i, medabot_j):
    '''
    retorna o vencedor da batalha
    '''
    Ai, Di, Hi = medabot_i.ataque, medabot_i.defesa, i.habilidade_atual
    Aj, Dj, Hj =  medabot_j.ataque, medabot_j.defesa, j.habilidade_atual
    if (Ai > Dj or Aj > Di) and Ai - Dj != Aj - Di:
        if Ai - Dj > Aj - Di:
            return i
        elif Ai - Dj < Aj - Di:
            return j
    elif Hi != Hj:
        if Hi > Hj:
            return i
        elif Hi < Hj:
            return j
    elif i.ID < j.ID:
        return i
    elif i.ID > j.ID:
        return j
def altera_habilidade (vencedor, perdedor):
    '''
    atualiza o H do perdedor e ganhador para a próxima batalha(já contando com os pontos de recuperacao)
    '''
    H_venceu, H_perdeu, K_venceu, K_perdeu = vencedor.habilidade_atual, perdedor.habilidade_atual, vencedor.recuperacao, perdedor.recuperacao
    H_inicial_v, H_iniciaL_p = lista_habilidades_iniciais[vencedor.ID], lista_habilidades_iniciais[perdedor.ID]
    h_atual_v = H_venceu - H_perdeu
    if h_atual_v < 0: #habilidade não pode ser negativa
        h_atual_v = 0
    if h_atual_v + K_venceu <= H_inicial_v: # habilidade não pode ser maior que a inicial
        vencedor.habilidade_atual = h_atual_v + K_venceu
    elif h_atual_v + K_venceu > H_inicial_v:
        vencedor.habilidade_atual = H_inicial_v #como habilidade atual não pode ser maior que inicial, quando isso acontece ela simplesmente volta a ser igual inicial
    h_atual_p = H_perdeu//2
    if h_atual_p + K_perdeu <= H_iniciaL_p:
        perdedor.habilidade_atual = h_atual_p + K_perdeu
    elif h_atual_p + K_perdeu > H_iniciaL_p:
        perdedor.habilidade_atual = H_iniciaL_p

def atualiza_a_habilidade(i, j):
    if batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == i: 
        altera_habilidade(i, j)
    elif batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == j:
        altera_habilidade(j, i)

def tira_peca_do_perdedor (perdedor, pontos_perdidos, tipo_da_peca_perdida):
    '''
    remove a peca que perdedor deu e retorna os pontos da peca que substituirá a perdida 
    '''
    ID_perdedor = perdedor.ID
    pontos_atualizado = 0
    lista_medapecas = lista_de_medabot[ID_perdedor].medapecas
    lista_medapecas.remove(tipo_da_peca_perdida + " " + str(pontos_perdidos)) #tire da lista de medapeças a medapeça perdida
    for k in range(len(lista_medapecas)):
        if lista_medapecas[k].split(" ")[0] == tipo_da_peca_perdida: #se o tipo de peça na lista de medapeças do perdedor for igual ao tipo da medapeça perdida
            if int(lista_medapecas[k].split(" ")[1]) > pontos_atualizado:
                pontos_atualizado =  int(lista_medapecas[k].split(" ")[1]) #pegue ,como substituto da peça perdida, uma outra do mesmo tipo e com o máximo de pontos possível
    return pontos_atualizado  

def define_medapeca_ganhada(vencedor, perdedor, pecas_v, pecas_p):
    '''
    retorna a peça ganha e os pontos ela dá, define se o vencedor usará a peca ou não na próx batalha
    tira a peca do perdedor ao chamar outra funcaoinsere a peca na lista de medapecas do vencedor
    '''
    ID_v, ID_p = vencedor.ID, perdedor.ID
    t_v, br_e_v, br_d_v, p_v, b_a_v, b_d_v, t_p, br_e_p, br_d_p, p_p, b_a_p, b_d_p = atualiza_pontos(lista_de_medapecas[ID_v], lista_de_medapecas[ID_p], lista_de_medabot[ID_v], lista_de_medabot[ID_p])
    l_pecas_v = [t_v, br_e_v, br_d_v, p_v]
    l_pecas_p = [t_p, br_e_p, br_d_p, p_p]
    diferenca_listas = [n2 - n1 for (n1, n2) in zip(l_pecas_v, l_pecas_p)] 
    maior_pontos = max (diferenca_listas, key=int) #encontrando a peça que dará mais vantagem pro vencedor na próx partida, de acordo com as peças do perdedor
    posicao = diferenca_listas.index(maior_pontos) 
    pontos_da_medapeca_ganha = l_pecas_p[posicao]
    if posicao == 0: #significa que a medapeça ganha é o torso 
        if pontos_da_medapeca_ganha > t_v: # não é possível transformar essas partes repetidas em função, pois precisa-se atualizar os pontos das medapeças nas classes
            pecas_v.pontos_do_torso = pontos_da_medapeca_ganha
        pecas_p.pontos_do_torso = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha,"T")
        tipo_da_medapeca_ganha = "T"
    elif posicao == 1:#significa que a medapeça ganha é o braço esquerdo
        if pontos_da_medapeca_ganha > br_e_v:
            pecas_v.pontos_do_braco_e= pontos_da_medapeca_ganha
        pecas_p.pontos_do_braco_e = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "E")
        tipo_da_medapeca_ganha = "E"
    elif posicao == 2: 
        if pontos_da_medapeca_ganha > br_d_v:#significa que a medapeça ganha é o braço direito
            pecas_v.pontos_do_braco_d = pontos_da_medapeca_ganha
        pecas_p.pontos_do_braco_d = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "D")
        tipo_da_medapeca_ganha = "D"
    else:
        if pontos_da_medapeca_ganha > p_v:#significa que a medapeça ganha é a perna
            pecas_v.pontos_das_pernas = pontos_da_medapeca_ganha
        pecas_p.pontos_das_pernas = tira_peca_do_perdedor(perdedor, pontos_da_medapeca_ganha, "P")
        tipo_da_medapeca_ganha = "P"
    lista_de_medabot[ID_v].medapecas.append(tipo_da_medapeca_ganha + " " + str(pontos_da_medapeca_ganha)) #colocar na lista de medapeças do vencedor a peça nova ganhada
    return(tipo_da_medapeca_ganha + str(pontos_da_medapeca_ganha))

def peca_ganhada(i, j):
    if batalhar(i, j, lista_de_medabot[i.ID], lista_de_medabot[j.ID]) == i:
        return(define_medapeca_ganhada(i, j, lista_de_medapecas[i.ID], lista_de_medapecas[j.ID]))
    else:
        return(define_medapeca_ganhada(j, i, lista_de_medapecas[j.ID], lista_de_medapecas[i.ID]))

def atualiza_pontos(peca_i, peca_j, medabot_i, medabot_j):
    '''
    atualiza o ataque e defesa para próx batalha, pois os robos perderam e/ou ganharam pecas, também retorna os pontos de cada peça atualizados, pois assim fica mais simples de definir as variaveis nas outras funções que as utilizam
    '''
    torso_i, braco_e_i, braco_d_i, pernas_i = peca_i.pontos_do_torso, peca_i.pontos_do_braco_e, peca_i.pontos_do_braco_d, peca_i.pontos_das_pernas
    bonus_ataque_i, bonus_defesa_i = medabot_i.bonus_de_ataque, medabot_i.bonus_de_defesa
    torso_j,  braco_e_j, braco_d_j, pernas_j = peca_j.pontos_do_torso, peca_j.pontos_do_braco_e, peca_j.pontos_do_braco_d, peca_j.pontos_das_pernas
    bonus_ataque_j, bonus_defesa_j = medabot_j.bonus_de_ataque, medabot_j.bonus_de_defesa
    medabot_i.ataque,  medabot_i.defesa = (braco_d_i + braco_e_i + bonus_ataque_i), (torso_i + pernas_i + bonus_defesa_i)
    medabot_j.ataque, medabot_j.defesa = (braco_d_j + braco_e_j + bonus_ataque_j), (torso_j + pernas_j + bonus_defesa_j)
    return (torso_i, braco_e_i, braco_d_i, pernas_i, bonus_ataque_i, bonus_defesa_i, torso_j ,braco_e_j, braco_d_j, pernas_j, bonus_ataque_j, bonus_defesa_j)

def imprimir_ficha_tecnica(i,j):
    I, J = i.ID, j.ID
    t_i, br_e_i, br_d_i, p_i, b_a_i, b_d_i, t_j, br_e_j, br_d_j, p_j, b_a_j, b_d_j = atualiza_pontos(lista_de_medapecas[I], lista_de_medapecas[J], lista_de_medabot[I], lista_de_medabot[J])
    print(f'\tA{I} = E{br_e_i} + D{br_d_i} + {b_a_i} = {br_e_i + br_d_i + b_a_i}')
    print(f'\tD{I} = T{t_i} + P{p_i} + {b_d_i} = {t_i + p_i + b_d_i}')
    print(f'\tH{I} = {i.habilidade_atual}')
    print(f'\tA{J} = E{br_e_j} + D{br_d_j} + {b_a_j} = {br_e_j + br_d_j + b_a_j}')
    print(f'\tD{J} = T{t_j} + P{p_j} + {b_d_j} = {t_j + p_j + b_d_j}')
    print(f'\tH{J} = {j.habilidade_atual}')

N = int(input())
lista_habilidades_iniciais = [0] #para index ser igual da lista de medalutadores
lista_de_medalutadores = []
lista_de_medabot = [0] #para index ser igual da lista de medalutadores
lista_de_medapecas = [0]
for k in range(N):
    lista_de_pecas, lista_torso, lista_braco_e, lista_braco_d, lista_perna = [], [], [], [], []
    h_k_numeropecas= input().split(" ")
    pontos_de_habilidade, pontos_de_recuperacao, numero_de_pecas = int(h_k_numeropecas[0]), int(h_k_numeropecas[1]), int(h_k_numeropecas[2])
    lista_habilidades_iniciais.append(pontos_de_habilidade)
    medalha = input().split(" ")
    bonus_de_ataque, bonus_de_defesa = int(medalha[0]), int(medalha[1]) 
    for i in range(numero_de_pecas):
          medapeca = input()
          lista_de_pecas.append(medapeca)
          tipo, pontos = medapeca.split(" ")[0], medapeca.split(" ")[1]
          if tipo == "T":
              lista_torso.append(pontos)
          if tipo == "E":
              lista_braco_e.append(pontos)
          if tipo == "D":
              lista_braco_d.append(pontos)
          if tipo == "P":
              lista_perna.append(pontos) 
    pontos_do_torso = int(max(lista_torso,key=int))
    pontos_do_braco_e = int(max(lista_braco_e, key=int))
    pontos_do_braco_d = int(max(lista_braco_d, key=int))
    pontos_das_pernas = int(max(lista_perna, key=int))
    A = pontos_do_braco_d + pontos_do_braco_e + bonus_de_ataque
    D = pontos_do_torso + pontos_das_pernas + bonus_de_defesa
    medalutador = Medalutador(k+1, pontos_de_habilidade, pontos_de_recuperacao)
    lista_de_medalutadores.append(medalutador) #armazenando os medalutadores que correspondem a classe Medalutador numa lista
    medabot = Medabot(lista_de_pecas, A, D, bonus_de_ataque, bonus_de_defesa) #outras classes são necessárias, pois há atributos que não são do medalutador
    lista_de_medabot.append(medabot)
    medapecas = Medapecas(pontos_do_torso, pontos_do_braco_e, pontos_do_braco_d, pontos_das_pernas)
    lista_de_medapecas.append(medapecas)
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
simular_torneios_de_cyberlutas(lista_de_medalutadores)