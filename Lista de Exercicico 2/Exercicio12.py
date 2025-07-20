# Exercício 12: Pode dirigir?

# Passos: 
# 1. Pedir a idade da pessoa. 
# 2. Perguntar se ela possui CNH (responder sim ou não). 
# 3. Verificar se tem 18 anos ou mais e se respondeu “sim” para CNH. 4. Mostrar se pode ou não dirigir.

print('Verificar se você pode dirigir')
idade = int(input('Digite a sua idade: '))
cnh = input('Você possui cnh? sim ou não? ')

if idade >=18 and cnh == "sim":
    print("Você pode dirigir!")
else:
    print('Você não pode dirigir!')