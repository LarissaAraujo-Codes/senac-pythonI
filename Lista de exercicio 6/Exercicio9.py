# · Exercício 9 – Contar letras em frase

# · • Receba uma frase como parâmetro.

# · • Conte quantas letras existem, desconsiderando espaços.

# · • Para isso, percorra cada caractere e conte apenas os que não são espaço.

# · • Retorne o total encontrado.

def contar_letras(frase):
    total = 0
    for caractere in frase:
        if caractere != " ":
            total += 1
    return total

frase = input("Digite uma frase: ")
print("Quantidade de letras (sem contar espaços):", contar_letras(frase))
