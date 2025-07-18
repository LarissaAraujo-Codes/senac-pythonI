# Exercício 2: Preço com desconto

# Passos: 1. Pedir ao usuário o valor de um produto (com decimal). 2. Calcular 10% de desconto sobre o valor. 3. Subtrair esse desconto do valor original. 4. Mostrar o valor final com desconto.

print('Somar valor do desconto')
valorProduto = float(input('Digite o valor do produto com decimal: '))
desconto = 0.10
valorDesconto = valorProduto*desconto
valorFinal = valorProduto-valorDesconto
print(f'O produto com desconto custa {valorFinal} reais.')