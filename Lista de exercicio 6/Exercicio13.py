# · Exercício 13 – Converter Celsius para Fahrenheit

# · • Receba a temperatura em Celsius.

# · • Use a fórmula: Fahrenheit = (Celsius × 1.8) + 32.

# · • Retorne o valor convertido.

def celsius_para_fahrenheit(celsius):
    return (celsius * 1.8) + 32

temp = float(input("Digite a temperatura em Celsius: "))
print("Temperatura em Fahrenheit:", celsius_para_fahrenheit(temp))
