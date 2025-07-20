# · Exercício 12 – Média de 3 notas

# · • Receba três números (notas).

# · • Some as três notas e divida o total por 3 para calcular a média.

# · • Retorne o valor da média.

def media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))
print("Média:", media(a, b, c))
