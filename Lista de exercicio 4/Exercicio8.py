# Exercício 8 (while): 
# Peça ao usuário para digitar uma senha. Enquanto ele errar, diga “Senha incorreta”. Se acertar (“liberar123”), diga “Bem-vindo”.

print('Acerte a senha')

senha = ""

while senha != "liberar123":
    senha = input("Digite a senha: ")
    if senha != "liberar123":
        print("Senha incorreta.")

print("Bem-vindo!")
