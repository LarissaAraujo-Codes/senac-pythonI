# Exercício 8: Par ou ímpar

# Passos: 1. Pedir um número ao usuário. 2. Verificar se o número dividido por 2 tem resto 0. 3. Se tiver, é par; senão, é ímpar. 4. Mostrar o resultado.

print('Par ou ímpar')
numero1 = int(input('Digite um numero inteiro para ver se é par ou ímpar: '))
divisao = numero1/2
if divisao == 0:
    print(f'O numero {numero1} é par!')
else:
    print(f'O numero {numero1} é impar!')