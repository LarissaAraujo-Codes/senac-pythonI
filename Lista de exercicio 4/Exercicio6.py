# Exercício 6 (while): 
# Peça ao usuário para digitar palavras até ele escrever a palavra “fim”. Em seguida, mostre todas as palavras digitadas.

print('Mostrar palavras digitadas')
palavras = []

while True:
    palavra = input("Digite uma palavra (ou 'fim' para encerrar): ")
    if palavra.lower() == "fim":
        break
    palavras.append(palavra)

print("Palavras digitadas:")
for i in palavras:
    print(i)
