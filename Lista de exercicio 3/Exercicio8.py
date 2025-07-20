# · Exercício 8:

# · Peça para o usuário digitar um número entre 1 e 12 e mostre o mês correspondente. Caso o número seja inválido, mostre “Número inválido”.

print('Mes do Ano')
numero = int(input('Digite um número inteiro de 1 a 12: '))

dias = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= numero <= 12:
    print(dias[numero - 1])
else:
    print('Número inválido. Digite um número de 1 a 12.')