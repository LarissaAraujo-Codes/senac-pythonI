# · Exercício 5 – Classificar horário do dia

# · • Peça ao usuário para digitar a hora (um número entre 0 e 23) dentro da função.

# · • Use if/else para decidir se é “Bom dia” (ex: 5-12), “Boa tarde” (13-18) ou “Boa noite” (19-4).

# · • Mostre a saudação adequada na tela.

def saudacao_horario():
    hora = int(input("Digite a hora atual (0 a 23): "))
    if 5 <= hora <= 12:
        print("Bom dia!")
    elif 13 <= hora <= 18:
        print("Boa tarde!")
    else:
        print("Boa noite!")

saudacao_horario()
