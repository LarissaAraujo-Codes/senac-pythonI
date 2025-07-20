# · Exercício 11 – Nome completo

# · • Receba dois parâmetros: nome e sobrenome.

# · • Junte os dois com um espaço entre eles.

# · • Retorne essa nova string formatada.

def nome_completo(nome, sobrenome):
    return f"{nome} {sobrenome}"

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Nome completo:", nome_completo(nome, sobrenome))
