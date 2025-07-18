# Exercício 6: Verificador de maioridade

# Passos: 1. Pedir a idade da pessoa. 2. Verificar se a idade é maior ou igual a 18. 3. Mostrar uma mensagem dizendo se é maior ou menor de idade.

print('Verificador de maioridade')

idade = int(input('Digite a sua idade: '))
if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')