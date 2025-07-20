# Exercício 7: 
# Crie um dicionário com as seguintes informações de uma pessoa: nome, idade e cidade. Depois, mostre uma frase com esses dados formatados.

pessoa = {
    "nome": input("Digite o nome: "),
    "idade": int(input("Digite a idade: ")),
    "cidade": input("Digite a cidade: ")
}

print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")
