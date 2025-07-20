# Exercício 15: Calculadora de IMC


# Passos:

# 1. Pedir o peso (em kg) e altura (em metros).
# 2. Calcular o IMC usando a fórmula: peso dividido pela altura ao quadrado.
# 3. Comparar o valor do IMC com as faixas:
# o Menor que 18.5: Abaixo do peso
# o Entre 18.5 e 24.9: Peso normal
# o Entre 25 e 29.9: Sobrepeso
# o 30 ou mais: Obesidade
# 4. Mostrar a classificação.

print('Calculo do IMC')
peso = float(input('Digite seu peso em kg '))
altura = int(input('Digite sua altura em cm '))
imc = (peso/altura)**2

if imc >= 30:
    print('Obesidade')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso')
elif imc >= 18.5 and imc <=24.9:
    print('Peso normal')
else:
    print('Baixo peso')