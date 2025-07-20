# Exercício 2 (for): Peça ao usuário um número e exiba os quadrados dos números de 1 até esse número usando for.

print('Exibir valor ao quadrado: ')

numero = int(input("Digite um número inteiro: "))

for i in range(1, numero + 1):
    print(i ** 2)