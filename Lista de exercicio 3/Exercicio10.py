# · Exercício 10:

# · Peça para o usuário digitar o número de horas trabalhadas e o valor da hora. Calcule o salário bruto e informe se o salário está:
# · • Até 1000: “Salário baixo”
# · • Entre 1001 e 3000: “Salário médio”
# · • Acima de 3000: “Salário alto”

print('Calculo de salario')
horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada:  "))

salario_bruto = horas * valor_hora
print(f"Salário bruto: R$ {salario_bruto}")

if salario_bruto <= 1000:
    print("Salário baixo.")
elif 1001 <= salario_bruto <= 3000:
    print("Salário médio.")
else:3                                                                                                                                                                              
print("Salário alto.")