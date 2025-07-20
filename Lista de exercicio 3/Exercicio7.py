# · Exercício 7:

# · Um programa que pede três lados de um triângulo e informe se ele é:
# · • Equilátero (todos os lados iguais)
# · • Isósceles (dois lados iguais)
# · • Escaleno (todos os lados diferentes)
# · • Se não formar um triângulo (soma de dois lados deve ser maior que o terceiro)

print('Tipo do triângulo')
lado1 = float(input('Digite as medidas do lado 1 do triangulo'))
lado2 = float(input('Digite as medidas do lado 2 do triangulo'))
lado3 = float(input('Digite as medidas do lado 3 do triangulo'))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero ")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles ")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores informados não formam um triângulo.")