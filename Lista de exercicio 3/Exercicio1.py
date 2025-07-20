# · Exercício 1:

# · Peça para o usuário digitar um número inteiro. Informe se ele é positivo, negativo ou zero.


print('Verificar se é impar ou par ou 0')
numero = float(input('Digite um numero para vê se é par ou impar ou zero '))
par_impar = numero%2

if numero ==0:
    print(f'O numero {numero} é zero')

elif par_impar == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')