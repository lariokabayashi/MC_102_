<<<<<<< HEAD
entrada = input().split(" ")
senha_mestre = int(entrada[0])
n = int(entrada[1])
lista_invertida = []
def digitos_sep(senha):
        '''separa os digitos de um numero na ordem invertida, colocando-os em uma lista
        '''
        lista_invertida = []
        while senha % 10 != 0:
            lista_invertida.append(senha % 10)
            senha = senha // 10
        return lista_invertida

def inverte(lista):
    ''' devolve a lista invertida
    '''
    nova_lista = []
    tam_lista = int(len(lista))
    for w in range(tam_lista - 1, -1, -1):
        nova_lista.append(lista[w])
    return nova_lista


for i in range(1, n + 1):
      tentativa = int(input())
      lista_mestre = inverte(digitos_sep(senha_mestre))
      lista_tentativa = inverte(digitos_sep(tentativa))
      tam_l_mestre = int(len(lista_mestre))
      tam_l = int(len(lista_tentativa))
    
      if lista_mestre == lista_tentativa: 
          print("Senha reconhecida. Desativando defesas...")
          break
          
      else:
          if tam_l_mestre == tam_l:
            digito_igual = 0
            for x in range(0, tam_l):
                 if lista_mestre[x] == lista_tentativa[x]:
                    digito_igual += 1
            print("Senha incorreta")
            print("Semelhanca:", digito_igual)
            print("Tentativas restantes:", n - i, "\n")
          else:
            print("Senha incorreta")
            print("Semelhanca: Erro: quantidade de digitos incongruente")
            print("Tentativas restantes:", n - i, "\n")
if lista_mestre != lista_tentativa:
  print("Tentativas esgotadas. Acionando defesas...")

=======
entrada = input().split(" ")
senha_mestre = int(entrada[0])
n = int(entrada[1])
lista_invertida = []
def digitos_sep(senha):
        '''separa os digitos de um numero na ordem invertida, colocando-os em uma lista
        '''
        lista_invertida = []
        while senha % 10 != 0:
            lista_invertida.append(senha % 10)
            senha = senha // 10
        return lista_invertida

def inverte(lista):
    ''' devolve a lista invertida
    '''
    nova_lista = []
    tam_lista = int(len(lista))
    for w in range(tam_lista - 1, -1, -1):
        nova_lista.append(lista[w])
    return nova_lista


for i in range(1, n + 1):
      tentativa = int(input())
      lista_mestre = inverte(digitos_sep(senha_mestre))
      lista_tentativa = inverte(digitos_sep(tentativa))
      tam_l_mestre = int(len(lista_mestre))
      tam_l = int(len(lista_tentativa))
    
      if lista_mestre == lista_tentativa: 
          print("Senha reconhecida. Desativando defesas...")
          break
          
      else:
          if tam_l_mestre == tam_l:
            digito_igual = 0
            for x in range(0, tam_l):
                 if lista_mestre[x] == lista_tentativa[x]:
                    digito_igual += 1
            print("Senha incorreta")
            print("Semelhanca:", digito_igual)
            print("Tentativas restantes:", n - i, "\n")
          else:
            print("Senha incorreta")
            print("Semelhanca: Erro: quantidade de digitos incongruente")
            print("Tentativas restantes:", n - i, "\n")
if lista_mestre != lista_tentativa:
  print("Tentativas esgotadas. Acionando defesas...")

>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
