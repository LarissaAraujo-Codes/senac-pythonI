# · Exercício 2:

# · Peça para o usuário digitar a temperatura em graus Celsius e mostre:
# · • Se a temperatura é menor que 0, mostre “Está congelando!”
# · • Entre 0 e 25, “Temperatura amena.”
# · • Acima de 25, “Está quente!”

print('Analisar a temperatura')
graus = float(input('Digite a temperatura '))

if graus <0:
    print('Esta congelando')
elif graus >=0 and graus <25:
    print('Temperatura amena')
else:
    print('Está quente')