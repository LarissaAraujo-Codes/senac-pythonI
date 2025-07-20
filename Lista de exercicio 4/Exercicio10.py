# Exercício 10 (while): 
# Peça ao usuário para digitar nomes de frutas. O programa deve continuar até que o nome digitado tenha mais de 10 letras. Ao final, exiba quantas frutas foram inseridas

print('Contador de frutas')
contador = 0

while True:
    fruta = input("Digite o nome de uma fruta: ")
    if len(fruta) > 10:
        break
    contador += 1

print(contador)
