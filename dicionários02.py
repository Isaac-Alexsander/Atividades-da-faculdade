Nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
endereco = input("Digite seu endereço: ")
telefone = int(input("Dgite seu telefone: "))


d = {"nome" : Nome, "idade" : idade, "Endereço" : endereco, "Telefone" : telefone}
print(d)
print(d.get("idade"))


