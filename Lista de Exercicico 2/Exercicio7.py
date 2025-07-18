# Exercício 7: Verificação de senha

# Passos: 1. Definir uma senha correta no programa. 2. Pedir que o usuário digite uma senha. 3. Comparar a senha digitada com a correta. 4. Mostrar mensagem de acesso permitido ou negado.

print('Verificador de senha')
senha = "123456"

senha2 = input('Digite a senha correta: ')

if senha2 == senha:
    print('Acesso permitido!')
else:
    print('Acesso negado!')