# Academico: Rodrigo Estevao Rottava - RA: 60001962
# Academico: Kevyn Samuel Barboza - RA: 60000906
# Academico: Fabricio Cazarotto - RA: 60000165
#============================================================

print("\n")

import random

def calcularDesconto():
    print("\n|===_CALCULO DE DESCONTO_===|")
    preco = float(input("Coloque o preço do produto escolhido: R$ "))
    percentual = float(input("Coloque o percentual de seu desconto: % "))
    valorDesconto = (percentual / 100) * preco
    precoFinal = preco - valorDesconto
    print(f"Desconto: R$ {valorDesconto:.2f}")
    print(f"Preco final com desconto: R$ {precoFinal:.2f}\n")

def realizarSorteio():
    print("\n|===_SORTEIO DE NÚMEROS_===|")
    inicio = int(input("Coloque o número inicial: "))
    fim = int(input("Coloque o número final: "))
    if inicio >= fim:
        print("Intervalo invalido seu numero inicial precisa ser menor que o final\n")
    else:
        sorteio = random.randint(inicio, fim)
        print(f"Número sorteado: {sorteio}\n")

def menu():
    while True:
        print("|===_MENU PRINCIPAL_===|")
        print("\n")
        print("1) Calcular Desconto")
        print("2) Sortear numero aleatorio")
        print("3) Sair")
        opcao = input("Escolha uma das opcoes acima: ")
        if opcao == "1":
            calcularDesconto()
        elif opcao == "2":
            realizarSorteio()
        elif opcao == "3":
            print("Programa sendo encerrado ate a proxima")
            break
        else:
            print("Putz! essa opcao e invalida! Tente novamente haha\n")
menu()

