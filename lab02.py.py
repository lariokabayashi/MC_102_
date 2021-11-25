canal = input()
n = int(input())
lista = []
lista2018 = []
lista2019 = []
lista2020 = []
for j in range(1, n + 1):
    data = input().split('-')
    views = input()
    lista.append(data[0])
    lista.append(int(views))
for i in range(0, 2 * n, 2):
    if lista[i] == "2018":
        lista2018.append(int(lista[i + 1]))
    elif lista[i] == "2019":
        lista2019.append(int(lista[i + 1]))
    elif lista[i] == "2020":
        lista2020.append(int(lista[i + 1]))
x = sum(lista2018) + sum(lista2019) + sum(lista2020)
y = len(lista2018) + len(lista2019) + len(lista2020)
print("Canal:", canal)
print("Total de views do trienio:", x)
print("Media de views do trienio:", format((x/y), ".2f"), "\n")

print("2018")
print("Total:", sum(lista2018))
if x == 0:
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(100*(sum(lista2018) / x), ".2f"))
if sum(lista2018) == 0:
    print("Media: 0.00", "\n")
else:
    print("Media:", format(sum(lista2018) / int(len(lista2018)), ".2f"), "\n")

print("2019")
print("Total:", sum(lista2019))
if x == 0:
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(100*(sum(lista2019) / x), ".2f"))
if sum(lista2019) == 0:
    print("Media: 0.00", "\n")
else:
    print("Media:", format(sum(lista2019) / int(len(lista2019)), ".2f"), "\n")

print("2020")
print("Total:", sum(lista2020))
if x == 0:
    print("Porcentagem das views do trienio: indeterminada")
else:
    print("Porcentagem das views do trienio:", format(100*(sum(lista2020) / x), ".2f"))
if sum(lista2020) == 0:
    print("Media: 0.00")
else:
    print("Media:", format(sum(lista2020) / int(len(lista2020)), ".2f"))
