# Exercício 9: Entrada no evento

# Passos: 
#1. Pedir a idade da pessoa.
# 2. Verificar se está entre 16 e 65 anos (inclusive). 
# #3. Mostrar se a entrada é permitida ou negada.

print ('Verificar entrada no evento')
idade = int(input('Digite a sua idade: '))

if idade >=16 and idade <=65:
    print('Entrada permitida!')
else:
    print('Entrada negada!')