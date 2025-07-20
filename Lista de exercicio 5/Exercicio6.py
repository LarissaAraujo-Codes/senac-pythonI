# Exercício 6: 
# Peça ao usuário para digitar 5 números, podendo repetir. Armazene-os em um set e mostre: - Quais números foram digitados (sem repetições). - Quantos valores únicos foram inseridos.

numeros = set()

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.add(num)

print("\nNúmeros digitados (sem repetição):", numeros)
print("Quantidade de valores únicos:", len(numeros))
