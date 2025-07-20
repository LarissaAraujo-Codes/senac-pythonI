# · Exercício 9:

# · Escreva um programa que leia uma letra e informe se é uma letra maiúscula, minúscula ou um caractere especial.

print('Verificar se é ua letra maiúscula, minuscula ou caractere especial')
letra = input("Digite um único caractere: ")

if len(letra) != 1:
    print("Digite uma letra: ")
elif letra.isupper():
    print("É uma letra MAIÚSCULA.")
elif letra.islower():
    print("É uma letra minúscula.")
else:
    print("É um caractere especial.")