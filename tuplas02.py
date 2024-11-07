p1 = list()
p2 = list()

tamanho = int(input("Digite o Tamanho das turmas: "))
mediap1 = 0 
mediap2 = 0
maior = 0
for i in range(tamanho):
    notasp1 = int(input("Digite as notas da turma p1: "))
    p1.append(notasp1)

somap1 = sum(p1)
mediap1 = somap1 / tamanho

for n in range(tamanho):
    notasp2 = int(input("Digite as notas da turma p2: "))
    p2.append(notasp2)

somap2 = sum(p2)
mediap2 = somap2 / tamanho

print(p1,"notas da turma e",mediap1,"da turma")
print(p2,"notas da turma e",mediap2,"da turma")

if mediap1 > mediap2:
    print("A turma com maior média é a p1")
else:
    print("A turma com maior média é a p2")