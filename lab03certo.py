<<<<<<< HEAD
n = int(input())
while n != 0:
    coordenada = input().split(' ')
    peca = coordenada[0]
    coluna = ord(coordenada[1])-ord('a')
    linha = int(coordenada[2])
    print(f"Movimentos para a peca {peca} a partir da casa {coordenada[1]}{coordenada[2]}.")
    for i in range(n,0,-1):
        print(i, end='')
        for j in range(n):
            if i == linha and j == coluna:
                print(" o",end='')
            elif peca == 'Torre' and (i == linha or j == coluna):
                 print(" x", end='')
            elif peca == 'Rei' and ((i == linha + 1 or i == linha - 1 or i == linha) and (j == coluna + 1 or j == coluna-1 or j==coluna)):
                print(" x", end='')
            elif peca == 'Dama'and ((i == linha or j == coluna) or (i + j == linha + coluna or i - j == linha - coluna)):
                print(" x", end='')
            elif peca == 'Peao'and linha == 2 and j == coluna and (i == 3 or i == 4) :
                print(" x", end='')
            elif peca == 'Peao' and j == coluna and i == linha + 1:
                print(" x", end='')
            elif peca == 'Cavalo' and (((i == linha + 2  or i == linha - 2) and (j == coluna + 1 or j == coluna - 1)) or ((i == linha + 1 or i == linha - 1) and (j == coluna + 2 or j == coluna - 2))):
                print(" x", end='')
            elif peca == 'Bispo' and (i + j == linha + coluna or i - j == linha - coluna):
                print(" x", end='')
            else:
                print(" -", end='')
        print()
    print(" ", end='')
    for k in range(n):
        letra = chr(ord('a')+k)
        print(f" {letra}",end='')
    print()
    print()
    n = int(input())

=======
n = int(input())
while n != 0:
    coordenada = input().split(' ')
    peca = coordenada[0]
    coluna = ord(coordenada[1])-ord('a')
    linha = int(coordenada[2])
    print(f"Movimentos para a peca {peca} a partir da casa {coordenada[1]}{coordenada[2]}.")
    for i in range(n,0,-1):
        print(i, end='')
        for j in range(n):
            if i == linha and j == coluna:
                print(" o",end='')
            elif peca == 'Torre' and (i == linha or j == coluna):
                 print(" x", end='')
            elif peca == 'Rei' and ((i == linha + 1 or i == linha - 1 or i == linha) and (j == coluna + 1 or j == coluna-1 or j==coluna)):
                print(" x", end='')
            elif peca == 'Dama'and ((i == linha or j == coluna) or (i + j == linha + coluna or i - j == linha - coluna)):
                print(" x", end='')
            elif peca == 'Peao'and linha == 2 and j == coluna and (i == 3 or i == 4) :
                print(" x", end='')
            elif peca == 'Peao' and j == coluna and i == linha + 1:
                print(" x", end='')
            elif peca == 'Cavalo' and (((i == linha + 2  or i == linha - 2) and (j == coluna + 1 or j == coluna - 1)) or ((i == linha + 1 or i == linha - 1) and (j == coluna + 2 or j == coluna - 2))):
                print(" x", end='')
            elif peca == 'Bispo' and (i + j == linha + coluna or i - j == linha - coluna):
                print(" x", end='')
            else:
                print(" -", end='')
        print()
    print(" ", end='')
    for k in range(n):
        letra = chr(ord('a')+k)
        print(f" {letra}",end='')
    print()
    print()
    n = int(input())

>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
