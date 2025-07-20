# Exercício 8: 
# Crie um dicionário onde as chaves são nomes de alunos e os valores são suas notas. Depois: - Mostre o dicionário completo. - Mostre apenas os alunos com nota maior ou igual a 7.

alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do {i + 1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos[nome] = nota

print("\nDicionário completo:")
print(alunos)

print("\nAlunos com nota maior ou igual a 7:")
for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome}: {nota}")
