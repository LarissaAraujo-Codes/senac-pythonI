# · Exercício 5:

# · Peça a nota de um aluno (0 a 10). Mostre:
# · • “Reprovado” se nota < 5
# · • “Recuperação” se nota entre 5 e 6.9
# · • “Aprovado” se nota >= 7

print('Verificação de nota')
nota = float(input('Digite a nota do aluno '))
if nota >=7:
    print('Aprovado')
elif nota >= 5 and nota <= 6.9:
    print('Recuperação')
else:
    ('Reprovado')