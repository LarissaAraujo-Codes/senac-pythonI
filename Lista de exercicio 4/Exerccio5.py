# Exercício 5 (for): 
# #Use for para imprimir os números pares de 0 a 20 e ao final mostre quantos foram exibidos.

print('Mostrando numeros pares')

numero = int(input('Digite um numero inteiro: '))

for i in range (1, numero+1):
    if i %2 ==0:
        print(i)