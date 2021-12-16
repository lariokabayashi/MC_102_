import sys
sys.setrecursionlimit(1500)

def calculo_do_nivel_maior(area, i): 
    while (area - 2**(2*i) >= 0) and (area - 2**(2*(i+1)) >= 0):
        i += 1
    return i
def comparacao(M, N):
    if M < N:
        return M
    else:
        return N
def encontre_nova_dimensao(i, M, N): #divide resto do campo em 1 ou 2 outros campo (m , n) 
    M1, N1 = M - 2**i, 2**i 
    M2, N2 = M, N - 2**i
    menor_lado_1, menor_lado_2 = comparacao(M1, N1), comparacao(M2, N2) #importante que se tivermos 2 campos pegar primeiro aquele que tiver menor dimensão maior
    if menor_lado_1 > menor_lado_2:
        return (M1, N1, M2, N2) 
    else:
        return(M2, N2, M1, N1)
def cria_areas_de_efeito(M, N, i, dict):
        if M >= 2**i and N >= 2**i: #indo do i maior para o menor de modo que o nivel seja maior e o numero de submagias menor #se dim do campo suporta lado 2**i por 2**i, campo terá nova dim
            dict[i] += 1
            M1, N1, M2, N2 = encontre_nova_dimensao(i, M, N) #função gera dois novos campos onde criaremos areas de efeito também
            cria_areas_de_efeito(M1, N1, i, dict) #ver se novo campo suporta lado 2**i por 2**i
            cria_areas_de_efeito(M2, N2, i, dict)
        elif i > 0: 
            cria_areas_de_efeito(M, N, i-1, dict) #se lado 2**i é muito, diminua o i
def total_de_submagias(dict, k):
    if k > nivel:
        return 0
    else:
        return dict[k] + total_de_submagias(dict, k + 1)
def total_de_PM(dict, k):
    if k > nivel:
        return 0
    else:
        return dict[k]*(2**k) + total_de_PM(dict, k + 1)

dict_submagias = {}  
G = 0
T = 0   
linha = input().split(" ")
m = int(linha[0])
n = int(linha[1])
nivel = calculo_do_nivel_maior(m*n, 0) #calculando a maior area de efeito (maior nivel)
for i in range(nivel + 1): #criando dicionario com todas areas de efeitos possiveis para o campo do jogo
    dict_submagias[i] = 0 #o nivel é a chave e as vezes que a submagia é conjurada é o valor 
cria_areas_de_efeito(m, n, nivel, dict_submagias)

print("---")
print("Grimorio de Teraf L'are")
print("---")
for i in dict_submagias:
    if dict_submagias[i] != 0:
        print(f"{dict_submagias[i]} submagia(s) de nivel {i}") 
print("---")
print(f"Total de submagia(s) conjurada(s): {total_de_submagias(dict_submagias, 0)}")    
print(f"Total de PM gasto: {total_de_PM(dict_submagias, 0)}")
=======
import sys
sys.setrecursionlimit(1500)

def calculo_do_nivel_maior(area, i): 
    while (area - 2**(2*i) >= 0) and (area - 2**(2*(i+1)) >= 0):
        i += 1
    return i
def comparacao(M, N):
    if M < N:
        return M
    else:
        return N
def encontre_nova_dimensao(i, M, N): #divide resto do campo em 1 ou 2 outros campo (m , n) 
    M1, N1 = M - 2**i, 2**i 
    M2, N2 = M, N - 2**i
    menor_lado_1, menor_lado_2 = comparacao(M1, N1), comparacao(M2, N2) #importante que se tivermos 2 campos pegar primeiro aquele que tiver menor dimensão maior
    if menor_lado_1 > menor_lado_2:
        return (M1, N1, M2, N2) 
    else:
        return(M2, N2, M1, N1)
def cria_areas_de_efeito(M, N, i, dict):
        if M >= 2**i and N >= 2**i: #indo do i maior para o menor de modo que o nivel seja maior e o numero de submagias menor #se dim do campo suporta lado 2**i por 2**i, campo terá nova dim
            dict[i] += 1
            M1, N1, M2, N2 = encontre_nova_dimensao(i, M, N) #função gera dois novos campos onde criaremos areas de efeito também
            cria_areas_de_efeito(M1, N1, i, dict) #ver se novo campo suporta lado 2**i por 2**i
            cria_areas_de_efeito(M2, N2, i, dict)
        elif i > 0: 
            cria_areas_de_efeito(M, N, i-1, dict) #se lado 2**i é muito, diminua o i
def total_de_submagias(dict, k):
    if k > nivel:
        return 0
    else:
        return dict[k] + total_de_submagias(dict, k + 1)
def total_de_PM(dict, k):
    if k > nivel:
        return 0
    else:
        return dict[k]*(2**k) + total_de_PM(dict, k + 1)

dict_submagias = {}  
G = 0
T = 0   
linha = input().split(" ")
m = int(linha[0])
n = int(linha[1])
nivel = calculo_do_nivel_maior(m*n, 0) #calculando a maior area de efeito (maior nivel)
for i in range(nivel + 1): #criando dicionario com todas areas de efeitos possiveis para o campo do jogo
    dict_submagias[i] = 0 #o nivel é a chave e as vezes que a submagia é conjurada é o valor 
cria_areas_de_efeito(m, n, nivel, dict_submagias)

print("---")
print("Grimorio de Teraf L'are")
print("---")
for i in dict_submagias:
    if dict_submagias[i] != 0:
        print(f"{dict_submagias[i]} submagia(s) de nivel {i}") 
print("---")
print(f"Total de submagia(s) conjurada(s): {total_de_submagias(dict_submagias, 0)}")    
print(f"Total de PM gasto: {total_de_PM(dict_submagias, 0)}")
print("---")
