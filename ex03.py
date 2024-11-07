x = int(input("Digite um numero: "))
y = int(input("Digite um numero: "))
numeros = 0
lista = list()
if x > y :
      y,x = x,y

for numeros in range(x,y+1):
    
    lista.append(numeros)
print(lista)