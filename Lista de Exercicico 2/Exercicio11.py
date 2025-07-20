# Exercício 11: Pode votar?

# Passos: 
# 1. Pedir a idade da pessoa. 
# 2. Verificar se a idade é maior ou igual a 16. 
# 3. Informar se a pessoa pode ou não votar.

print('Verificação de idade para votar')

idade = int(input('Digite a sua idade:'))
if idade >= 16:
    print('Você ja pode votar!')
else:
    print('Você não pode votar!')