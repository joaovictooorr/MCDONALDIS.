# adicionar descontos

import random

numero_aleatorio = random.randint(100,999)

def obter_escolha(opcoes):
    escolha = 0
    while escolha not in opcoes:
        print("Escolha uma opção Válida")
        for key, value in opcoes.items():
            print(f"{key} - {value}")
        escolha = int(input(" : "))
    return escolha 

def hamburguer():
    opcoes = {
        1: "MC PEIXE = R$ 15,90",
        2: "MC CARNE DE GATO = 10,50",
        3: "MC GALINHA = 12,40",
        4: "MC LANCHE FELIZ = R$ 20,00"
    } 
    escolha = obter_escolha(opcoes)
    return escolha

def batata():
    opcoes = {
        1: "BATATA PEQUENA = 5,00",
        2: "BATATA MEDIA = 8,00",
        3: "BATATA GRANDE = 10,00"
    }
    escolha = obter_escolha(opcoes)
    return escolha

def refrigerante():
    opcoes = {
        1: "REFRIGERANTE PEQUENO = 3,00",
        2: "REFRIGERANTE MEDIO = 5,00",
        3: "REFRIGERANTE GRANDE = 7,00"
    }
    escolha = obter_escolha(opcoes)
    return escolha

def valores(escolha_hambur, escolha_batata, escolha_refri):
    valores_hamburguer = {
        1: 15.90,
        2: 10.50,
        3: 12.40,
        4: 20.00 
    }

    valores_batata = {
        1: 5.0,
        2: 8.0,
        3: 10.0
    }

    valores_refrigerante = {
        1: 3.0,
        2: 5.0,
        3: 7.0
    }

    valor_hamburguer = valores_hamburguer.get(escolha_hambur, 0)
    valor_batata = valores_batata.get(escolha_batata, 0)
    valor_refri = valores_refrigerante.get(escolha_refri, 0)

    valor_total = valor_hamburguer + valor_batata + valor_refri
    return valor_total

def verificar_nome():
    nome_cliente = ""
    while not nome_cliente:
        nome_cliente = input("Digite o nome do cliente: ")
        if nome_cliente.isnumeric():
            print("Apenas são aceitos letras e acentuações")
            nome_cliente = ""
    return nome_cliente

def nota_fiscal(valor_escolha_hamburguer, valor_escolha_batata, valor_escolha_refrigerante, nome_cliente, valor_total):
    opcoes_hamburguer = {
        1: "MC PEIXE - R$ 15,90",
        2: "MC CARNE DE GATO - R$ 10,50",
        3: "MC GALINHA - R$ 12,40",
        4: "MC LANCHE FELIZ - R$ 20,00"
    }

    opcoes_batata = {
        1: " BATATA PEQUENA - R$ 5,00",
        2: " BATATA MEDIA - R$ 8,00",
        3: " BATATA GRANDE - R$ 10,00"        
    }

    opcoes_refri = {
        1: " REFRIGERANTE PEQUENO - R$ 3,00",
        2: " REFRIGERANTE MEDIO - R$ 5,00",
        3: " REFRIGERANTE GRANDE - R$ 7,00"
    }

    print(f" NÚMERO DO PEDIDO: {numero_aleatorio}")
    print(f" CLIENTE: {nome_cliente}")
    print(f" HAMBURGUER: {opcoes_hamburguer[valor_escolha_hamburguer]}")
    print(f" BATATA: {opcoes_batata[valor_escolha_batata]}")
    print(f" REFRIGERANTE: {opcoes_refri[valor_escolha_refrigerante]} ")
    print(f" VALOR TOTAL DA COMPRA: R$ {valor_total:.2f}")

valor_escolha_hamburguer = hamburguer()
valor_escolha_batata = batata()
valor_escolha_refrigerante = refrigerante()
valor_total = valores(valor_escolha_hamburguer,valor_escolha_batata,valor_escolha_refrigerante)
nome_cliente = verificar_nome()
nota_fiscal (valor_escolha_hamburguer,valor_escolha_batata,valor_escolha_refrigerante, nome_cliente, valor_total)