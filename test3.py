notas = list()
nu = 0
while nu < 3:
    notas2 = int(input("Digite uma nota: "))
    notas.append(notas2)
    nu += 1
media = sum(notas) / 3
notas.sort()
print(notas,min(notas),max(notas),media)