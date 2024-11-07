d= {}
tent= 0

while tent < 3:
    nomeprod = input("nome do produto: ")
    preco = int(input("Preço : "))
    d[nomeprod] = preco
    tent += 1

print(d) 