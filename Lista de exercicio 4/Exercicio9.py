# Exercício 9 (while): 
# Peça ao usuário dois números: um inicial e um final. Use while para contar de um até o outro, somando de 2 em 2.

print('Mostrando numero de 2 em 2')
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

while inicio <= fim:
    print(inicio)
    inicio += 2
