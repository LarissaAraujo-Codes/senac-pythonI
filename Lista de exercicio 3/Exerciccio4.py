# · Exercício 4:

# · Peça para o usuário digitar um número inteiro de 1 a 7 e mostre o dia da semana correspondente (1 = domingo, 2 = segunda, etc.). Caso o número não seja entre 1 e 7, informe “Número inválido”.

print('Dias da semana')
numero = int(input('Digite um número inteiro de 1 a 7: '))

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

if 1 <= numero <= 7:
    print(dias[numero - 1])
else:
    print('Número inválido. Digite um número de 1 a 7.')
