numeros = list()
tent = 0
while tent < 10:
    numeros2 = int(input("Digite um: "))
    numeros.append(numeros2)
    tent += 1
print(numeros[::-1])