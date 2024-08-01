#!/usr/bin/env python3

email_tmpl = """ 
    Olá, %(nome)s 
    Tem interesse em comprar %(produto)s? 
    Este produto é ótimo para resolver %(texto)s 
    Clique agora em %(link)s 
    Apenas %(quantidade)d disponiveis! 
    Preço promocional %(preco).2f 
    """                               

clientes = ["Maria", "João", "Bruno"]   

for cliente in clientes: 
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "escrever muito bem", 
        "link": "https://canetaslegais.com", "quantidade": 1, "preco": 50.5}) 


"""
    Para saber mais informações sobre formatações como no exemplo acima podemos no IPYTHON3 no terminal digitar o seguinte comando
    -$ help("FORMATTING")

    Tipo de INTERPOLAÇÃO PODE SER FEITA DA SEGUINTE FORMA
    
    TIPO CONCATENAÇÃO %s

    msg = "Olá, %s você é o player n %03d e você tem %.3f pontos"

    print(msg % ("Bruno", 2, 987.3))

    -----------------------------------------------------------------------------
    TIPO STR.FORMAT {}

    msg = "Olá, {} você é o player n {} e você tem {} pontos"

    print(msg.format("Bruno", 2, 2987.3))

    Para ficar igual o exemplo do TIPO CONCATENAÇÃO usando as {} chaves fazemos da seguinte forma
    msg = "Olá, {} você é o player n {:03d} e você tem {:.3f} pontos"

    print(msg.format("Bruno", 2, 987.3))

    Para formatar de outra maneira podemos fazer da seguinte forma

    msg = "Olá, {nome} você é o player n {num:03d} e você tem {pont:.3f} pontos"

    print(msg.format(nome = "Bruno", num = 2, pont = 987.3))

    -----------------------------------------------------------------------------
    TIPO F-STRINGS

    nome = "João"
    saldo = 89

    print(f"Olá {nome}")
    print(f"Olá {nome} seu saldo é de {saldo:.2f}")

    -----------------------------------------------------------------------------

    PARA QUAIS OCASIÕES DEVEMOS USAR AS INTERPOLAÇÕES

    CONCATENAÇÃO %s --> Para casos de logging

    STR.FORMAT {} --> Para mensagens longas, como exemplo e-mails

    F-STRAINGS --> Para todo os tipos de mensagens como, msg, print, error
    
    -----------------------------------------------------------------------------

    Para alterar a posição do textos na tela usamos o seguinte comando
    Centralizar
    print("{:^50}".format("Romullo"))
    Centralizar a ESQUERDA
    print("{:<50}".format("Romullo"))
    Centralizar a DIREITA
    print("{:>50}".format("Romullo"))

    Para preencher os espaços vazios podemos fazer dessa forma
    Centralizar
    print("{:-^50}".format("Romullo"))
    OBS: Pode usar qualquer tipo de caracteres (- _ * $ # etc....) letras também, será preenchido os espaços

    Para cortar letras do texto veja no exemplo abaixo 
    print("{:*^50.3}".format("Romullo"))

    -----------------------------------------------------------------------------
    PARA IMPRIMIR EMOJI
    Quando você acessar o site para pegar um emoji devemos copiar o código UTF do emoji e fazer da seguinte maneira
    
    print("\U0001F43C") --> Os primerios caracteres ("Barra U000") são obrigatórios depois inserimos o código do emoji 

    Para buscar pelo nome do emoji usamos a seguinte forma 
    print("\N{panda face}")

"""

nome = "João"
saldo = 89

print(f"Olá {nome} seu saldo é de {saldo:.2f}")

print("\U0001F349")

print("\N{party popper}")