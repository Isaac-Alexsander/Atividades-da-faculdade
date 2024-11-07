# {Dicionário} (tupla) [lista]

produtos = {}

while True:
    cod = int(input("Códico: "))
    nome = input("Nome: ")
    preco = float(input("R$: "))
    qtde = int(input("Quantidade: "))
    prod = []
    prod.append(nome)
    prod.append(preco)
    prod.append(qtde)
    produtos.update({cod : prod})
    resp = input("Deseja continuar S ou N? ")
    if resp == "N" or resp == "n":
        break

total = 0

for cod, prod in produtos.items():
    subtotal = produtos[cod][1] * produtos[cod][2]
    print(f"{prod[0]}: R$ {subtotal:.2f}")
    total += subtotal
print(20 * "-")
print(f"total : R$ {total:.2f}")