<<<<<<< HEAD
material = input()
pontoFusao = float(input())
pontoEbuliçao = float(input())
temperaturaAtual = float(input())
atualCelsius = round(float(5 * (temperaturaAtual-32)/9), 2)
print("Material:", material)
print("Ponto de fusao (Celsius):", format(pontoFusao,".2f"))
print("Ponto de ebulicao (Celsius):", format(pontoEbuliçao, ".2f"))
print("Temperatura atual (Celsius):", format(atualCelsius, ".2f"))
if (atualCelsius < pontoFusao):
    print("Estado fisico do material: Solido")
elif atualCelsius < pontoEbuliçao:
    print("Estado fisico do material: Liquido")
else:
    print("Estado fisico do material: Gasoso")
=======
material = input()
pontoFusao = float(input())
pontoEbuliçao = float(input())
temperaturaAtual = float(input())
atualCelsius = round(float(5 * (temperaturaAtual-32)/9), 2)
print("Material:", material)
print("Ponto de fusao (Celsius):", format(pontoFusao,".2f"))
print("Ponto de ebulicao (Celsius):", format(pontoEbuliçao, ".2f"))
print("Temperatura atual (Celsius):", format(atualCelsius, ".2f"))
if (atualCelsius < pontoFusao):
    print("Estado fisico do material: Solido")
elif atualCelsius < pontoEbuliçao:
    print("Estado fisico do material: Liquido")
else:
    print("Estado fisico do material: Gasoso")
>>>>>>> 49b15bf86efb2ad9861cb0a9968382c7def61cee
