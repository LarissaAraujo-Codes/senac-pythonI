# Exercício 4 (for): 
# #Crie um programa que pergunte um número ao usuário e use um laço for para verificar quais números entre 1 e ele são divisíveis por 7.

print('Mostrar numeros divisiveis por 7')

numero = int(input('Digite umm numero inteiro: '))

for i in range (1,numero +1):
    if i %7 ==0:
        print(i)
else:
    print('Numeros não divisiveis por 7')