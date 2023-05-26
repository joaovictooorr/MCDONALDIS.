# if nome_cliente bug que deixa o usario passar mesmo escrevendo numeros
# whiles não estão funcionando se escrever letras ao inves dos numeros da erro, tentar colocar uma mesangem de erro e retornar ao pedido
# a crescentar valores aos produtos e mostrar os valores no final
# Fazer uma função para o while (diminuir o codigo)
# Fazer descontos vc pode criar uma variável que recebe o preço menos o desconto e fazer um if q se tiver o desconto mostra essa variável no lugar do preço
# validar cartão de credito ou debito

import random

numero_aleatorio = random.randint(100, 999)

def hamburguer():
    escolha = 0
    escolha_hambur = ""
    while escolha == 0:
        print("Escolha um dos hamburgueres")
        print("1 - mc peixe")
        print("2 - mc carne de gato")
        print("3 - mc galinha")
        print("4 - mc lanche feliz")
        escolha = int(input(" : "))
        if escolha == 1:
            escolha_hambur = "MC PEIXE"
        elif escolha == 2:
            escolha_hambur = "MC CARNE DE GATO"
        elif escolha == 3:
            escolha_hambur = "MC GALINHA"
        elif escolha == 4:
            escolha_hambur = "MC LANCHE FELIZ" 
        else:
            print("Escolha uma opção válida")
            escolha = 0

    return escolha_hambur


def batata():
    escolha_batata = 0
    batatinha = ""
    while escolha_batata == 0:
        print("Escolha sua batata")
        print("1 - P ")
        print("2 - M ")
        print("3 - G ")
        escolha_batata = int(input(" : "))
        if escolha_batata == 1:
            batatinha = "PEQUENA"
        elif escolha_batata == 2:
            batatinha = "MEDIA"
        elif escolha_batata == 3:
            batatinha = "GRANDE"
        else:
            print("Escolha uma opção válida")
            escolha_batata = 0

    return batatinha


def refrigerante():
    escolha_refri = 0
    refri = ""
    while escolha_refri == 0:
        print("Escolha seu refrigerante")
        print("1 - P ")
        print("2 - M ")
        print("3 - G ")
        escolha_refri = int(input(" : "))
        if escolha_refri == 1:
            refri = "PEQUENO"
        elif escolha_refri == 2:
            refri = "MEDIO"
        elif escolha_refri == 3:
            refri = "GRANDE"
        else:
            print("Escolha uma opção válida")
            escolha_refri = 0

    return refri


def verificar_nome():
    nome_cliente = ""
    while not nome_cliente:
        nome_cliente = input("Digite o nome do Cliente: ")
        if nome_cliente.isnumeric():
            print("Erro: Você digitou um número.")
            nome_cliente = ""
    return nome_cliente


def nota_fiscal(escolha_hambur, batatinha, refri, nome_cliente):
    print(f" NÚMERO DO PEDIDO: {numero_aleatorio} ")
    print(f" CLIENTE: {nome_cliente}")
    print(f" HAMBURGUER: {escolha_hambur}")
    print(f" TAMANHO DA BATATA: {batatinha}")
    print(f" TAMANHO DO REFRIGERANTE: {refri}")


escolha_hambur = hamburguer()
batatinha = batata()
refri = refrigerante()
nome_cliente = verificar_nome()
nota_fiscal(escolha_hambur, batatinha, refri, nome_cliente)
