# · Exercício 10 – Verificar palíndromo

# · • A função recebe uma palavra.

# · • Compare a palavra original com a palavra invertida (lida de trás para frente).

# · • Se forem iguais, retorne True; caso contrário, False.

def eh_palindromo(palavra):
    return palavra == palavra[::-1]

texto = input("Digite uma palavra: ")
print("É palíndromo?", eh_palindromo(texto))

