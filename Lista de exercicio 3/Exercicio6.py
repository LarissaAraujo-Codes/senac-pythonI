# · Exercício 6:

# · Peça para o usuário digitar três números diferentes e informe qual é o maior.

print('Numero maior')
numero1 = float(input('Digite um numero: '))
numero2 = float(input('Digite mais um numero: '))
numero3 = float(input('Digite outro numero: '))

if numero1 > numero2 and numero1 > numero3:
    print(f'O numero {numero1} é maior que os numeros {numero2} e {numero3}')

if numero2 > numero1 and numero2 > numero3:
    print(f'O numero {numero2} é maior que os numeros {numero1} e {numero3}')

if numero3 > numero1 and  numero3 > numero2:
    print(f'O numero {numero3} é maior que os numeros {numero1} e {numero2}')

