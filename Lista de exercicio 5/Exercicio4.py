# Exercício 4: 
# Peça ao usuário para digitar 4 números inteiros e armazene-os em uma tupla. Depois, exiba: - Quantos números são pares. - Se o número 10 está na tupla.


numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1

tem_dez = 10 in numeros

print("\nNúmeros digitados:", numeros)
print("Quantidade de números pares:", pares)
print("O número 10 está na tupla?", "Sim" if tem_dez else "Não")

