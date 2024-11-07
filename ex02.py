# Inicializa um vetor para armazenar as médias dos alunos
medias_alunos = []

# Loop para coletar as notas de 10 alunos
for aluno in range(1, 11):
    print(f"Aluno {aluno}:")
    notas_aluno = []  # Lista para armazenar as notas do aluno
    soma_notas = 0  # Inicializa a soma das notas do aluno
    for nota_num in range(1, 5):
        nota = float(input(f"Digite a {nota_num}ª nota: "))
        notas_aluno.append(nota)
        soma_notas += nota
    # Calcula a média do aluno e armazena no vetor de médias
    media_aluno = soma_notas / 4
    medias_alunos.append(media_aluno)

# Conta o número de alunos com média maior ou igual a 7
alunos_aprovados = sum(1 for media in medias_alunos if media >= 7)

# Imprime o resultado
print(f"Número de alunos com média maior ou igual a 7: {alunos_aprovados}")
