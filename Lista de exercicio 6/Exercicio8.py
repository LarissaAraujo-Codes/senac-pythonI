# · Exercício 8 – Maior número da lista

# · • A função recebe uma lista de números.

# · • Use uma forma de comparar cada elemento para encontrar o maior.

# · • Retorne esse maior valor.

# · • O cálculo pode ser feito com um laço que verifica elemento por elemento.

def maior_numero(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

numeros = [3, 8, 1, 22, 7]
print("Maior número da lista:", maior_numero(numeros))
