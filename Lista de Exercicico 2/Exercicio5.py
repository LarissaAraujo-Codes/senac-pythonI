# Exercício 5: Conversor de temperatura

# Passos: 1. Pedir ao usuário a temperatura em graus Celsius. 2. Usar a fórmula de conversão: Celsius × 9 ÷ 5 + 32. 3. Mostrar a temperatura convertida para Fahrenheit.

print("Convesor de tempreatura, de Fahrenheit para Celsius")

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = celsius*9/5+32
print(f'{celsius} graus Celsius convertico para Fahrenheit fica: {fahrenheit} graus Fahrenheit ')
