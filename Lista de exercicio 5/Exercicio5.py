# Exercício 5: 
# Crie dois conjuntos: um com as vogais e outro com as letras de uma palavra digitada pelo usuário. Mostre as letras em comum entre os dois conjuntos.

vogais = set("aeiou")
palavra = input("Digite uma palavra: ").lower()
letras = set(palavra)

comum = vogais & letras  # interseção

print("Letras em comum com as vogais:", comum)
