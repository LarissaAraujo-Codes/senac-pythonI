# Exercício 7 (while): 
# Crie um contador que some todos os números de 1 até 50 com while. Exiba o total ao final.

print('Somando ate 50')
contador = 1
soma = 0

while contador <= 50:
    soma += contador
    contador += 1

print(f"A soma de todos os números de 1 até 50 é: {soma}")

