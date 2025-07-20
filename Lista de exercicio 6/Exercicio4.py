# · Exercício 4 – Perguntar e mostrar animal favorito

# · • Crie uma função que dentro dela use input() para perguntar o animal preferido do usuário.

# · • Depois, imprima uma frase personalizada, como “Eu também gosto de [animal]!”.

# · • Essa função mostra como combinar entrada e saída dentro de uma função.


def animal_favorito():
    animal = input("Qual é o seu animal favorito? ")
    print(f"Eu também gosto de {animal}!")

animal_favorito()
