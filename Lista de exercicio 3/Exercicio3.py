# · Exercício 3:

# · Leia uma letra do teclado e informe se ela é uma vogal ou uma consoante.


print('Vogal ou consoante')
letra = input('Digite uma letra: ')
vogal = ["a", "e", "i", "o", "u"]

if letra in vogal:
    print(f' A letra {letra} é uma vogal!')
else:
    print(f'A letra {letra} é uma consoante!')
