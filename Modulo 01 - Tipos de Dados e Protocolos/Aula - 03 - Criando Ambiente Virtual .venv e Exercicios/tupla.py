#!/usr/bin/env python3

"""
    Para trabalhar com tuplas podemos fazer dessa forma usando IPYTHON3
    -$ dados = ("Bruno", 15, True, None, 45.3)

    Para verificar se essa variável é uma tupla usamos o comando 
    -$ type(dados)

    OBS: A TUPLA não pode ser alterado os valores informados

    Para saber os tipos de funções a tuple suporta digite o comando no terminal
    -$ dir(tuple) 

    Para desempacotar uma tuple podemos fazer da seguinte maneira
    -$ pontos = 2, 1, 99

    Desempacotando
    -$ x = pontos[0]
    -$ y = pontos[1]
    -$ z = pontos[2]

    Após criar novas variáves e pegar o resultado dos indices da tupla agora fica mais fácil o manejo dos valores

    OUTRA FORMA MAIS SIMPLES USANDO UNPACKING, SPREAD NOME USADO PARA ESSA FORMATAÇÃO

    -$ x, y, z = pontos
    -$ x, *_ = pontos --> O asteristico * significa que após o x ele vai pegar tudo e colocar no _ 
    e quando for chamado ele irá printar na tela os dois valores juntos, como no exemplo abaixo 
    -$ print(_)

    Usado os nomes especiais para pegar os valores dos pontos
    -$ head, *body, tail = dados

    PARA CONTAR QUANTOS NÚMEROS PASSADO NA TUPLE EXISTE E QUANTAS VEZES ELE REPETE NA TUPLE
    Usamos o seguinte comando
    -$ pontos.count(2) --> o valor 2 pode ser qualquer valor que você precise verificar quantos números 2 existem na tuple

    Para fatiar uma tuple um elemento podemos fazer dessa maneira 
    -$ pontos[2:] --> Do elemento 2 até o final que seria a mesma coisa do indice 2 até o final
    -$ pontos[1:] --> Do elemento 1 até o final que seria a mesma coisa do indice 1 até o final

    Para saber o tamanho do elemento usamos o seguinte comando LEN
    -$ len(pontos)

"""
print("Exemplo 01")
dados = "Romullo", 15, True, None, 45.3
nome, idade, casado, filhos, peso = dados

print(idade)

print("-" * 20)

print("Exemplo 02")
pontos = 2, 1, 99
x, y, z = pontos
x, *_ = pontos
print(_)
print(pontos.count(2))
print(pontos[2:])
print(pontos[1:])
print(pontos[0:2])

print("-" * 20)

print("Exemplo 03")
head, *body, tail = pontos
print(head)
print(*body)
print(tail)

print("-" * 20)

print("Exemplo 04")
print(len(pontos))
