# · Exercício 7 – Multiplicação

# · • Crie uma função que receba dois números como parâmetros.

# · • Calcule o produto desses números.

# · • Retorne o resultado para quem chamou a função.

# · • Fora da função, peça os números ao usuário e mostre o resultado usando print.

def multiplicar(a, b):
    return a * b

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
resultado = multiplicar(x, y)
print("Resultado da multiplicação:", resultado)
