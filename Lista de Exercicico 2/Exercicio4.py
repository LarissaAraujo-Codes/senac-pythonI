# Exercício 4: Potência

# Passos: 1. Pedir dois números ao usuário: base e expoente. 2. Calcular a potência (base elevada ao expoente). 3. Mostrar o resultado da operação.

print('Calculo de potência')

numero1 = int(input('Digite um numero inteiro para o calculo de potencia: '))
numero2 = int(input('Digite um nuemro inteiro para ser o expoente no calculo de potência: '))

resultado = numero1**numero2

print(f'O resultado do calculo de potência é {resultado}')
