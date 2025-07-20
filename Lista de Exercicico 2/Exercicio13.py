# Exercício 13: Nota do aluno

# Passos: 
# 1. Pedir a nota (entre 0 e 10).
# 2. Se for 7 ou mais, o aluno está aprovado.
# 3. Se estiver entre 5 e 6.9, está em recuperação.
# 4. Se for menor que 5, está reprovado.
# 5. Mostrar o resultado.


print('Verificar nota do aluno')
nota = float(input('Digite a nota do aluno: '))

if nota >= 7:
    print('O aluno está aprovado')
elif nota >=5 and nota <=6.9:
    print(' O aluno esta em recuperação')
else:
    print('O aluno está reprovado')