# Exercício 14: Maior número

# Passos:
# 1. Pedir dois números.
# 2. Comparar os dois valores.
# 3. Informar qual número é maior, ou se são iguais.

print('Verificar o maior numero')
numero1 = float(input('Digite um numero para comparar: '))
numero2 = float(input('digite mais um numero para comparar: '))

if numero1 > numero2:
    print(f'O numero {numero1} é maior que o numero {numero2}')
else:
    print(f'O nuemro {numero2} é mairo que o nuemro {numero1}')