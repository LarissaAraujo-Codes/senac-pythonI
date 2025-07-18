# Exercício 3: Divisão inteira e resto

# Passos: 1. Pedir dois números inteiros ao usuário. 2. Dividir o primeiro número pelo segundo. 3. Mostrar o resultado da divisão inteira (sem casas decimais). 4. Mostrar o resto da divisão entre os dois números.

print('Divisão inteira e resto')
numero1 = int(input('Digite um nueero inteiro para ser divido: '))
numero2 = int(input('Digite um nuemro inteiro para ser o divisor: '))
resultadoInteiro = numero1//numero2
resultadoResto = numero1%numero2
print(f'O resultado interio da divisão é {resultadoInteiro} e o resto é {resultadoResto}')