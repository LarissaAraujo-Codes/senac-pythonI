# · Exercício 6 – Mostrar letras de uma palavra

# · • Dentro da função, peça para o usuário digitar uma palavra.

# · • Percorra cada letra da palavra usando um laço for.

# · • Em cada ciclo, imprima a letra atual em uma linha separada.

def mostrar_letras():
    palavra = input("Digite uma palavra: ")
    for letra in palavra:
        print(letra)

mostrar_letras()
